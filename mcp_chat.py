from __future__ import annotations

import os
import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.tools import tool

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://localhost:3322")

@tool
def open_page(url: str) -> str:
    """MCPサーバで指定したURLを開きます"""
    requests.post(f"{MCP_SERVER_URL}/open", json={"url": url})
    return f"{url} を開きました"

@tool
def click(selector: str) -> str:
    """MCPサーバでCSSセレクタを指定してクリックします"""
    requests.post(f"{MCP_SERVER_URL}/click", json={"selector": selector})
    return f"{selector} をクリックしました"


def main() -> None:
    """OpenAI GPT-4o と MCP サーバを使ったブラウザ操作チャット"""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY が設定されていません")

    llm = ChatOpenAI(model_name="gpt-4o", openai_api_key=api_key)
    tools = [open_page, click]

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "あなたはブラウザ操作アシスタントです。指示に従い、MCPサーバを介してPlaywrightでブラウザを操作してください。",
            ),
            MessagesPlaceholder("chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        ]
    )

    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    chat_history: list = []
    print("'exit' または 'quit' で終了します。")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            break
        result = agent_executor.invoke({"input": user_input, "chat_history": chat_history})
        print("AI:", result["output"])
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=result["output"]))


if __name__ == "__main__":
    main()
