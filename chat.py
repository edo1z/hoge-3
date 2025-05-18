from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.tools import tool

from video_tools import clip_video, overlay_text, change_speed


def main() -> None:
    """OpenAI GPT-4o と moviepy を使ったチャットベースの動画編集"""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY が設定されていません")

    llm = ChatOpenAI(model_name="gpt-4o", openai_api_key=api_key)

    # ツールを LangChain 用にラップする
    clip_tool = tool(clip_video)
    overlay_tool = tool(overlay_text)
    speed_tool = tool(change_speed)
    tools = [clip_tool, overlay_tool, speed_tool]

    # 動画ファイルがなければテスト用メッセージを表示
    if not os.path.exists("shapes.mp4"):
        print("注意: テスト用の動画ファイル 'shapes.mp4' が見つかりません。")
        print("create_movie/create_shapes_video.py を実行すると作成できます。")
        print("動画ファイルのパスは必ず 'shapes.mp4' を指定して実行してください。")

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "あなたは動画編集アシスタントです。moviepy を用いて依頼された編集を実行してください。\n"
                "入力ファイルは 'shapes.mp4' を使用してください。",
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
    print("入力例: 「shapes.mp4の動画を2倍速にして、中央に「テスト」というテキストを追加してください」")

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
