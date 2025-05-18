from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage


def main() -> None:
    """OpenAI GPT-4o を使ったシンプルなチャット"""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY が設定されていません")

    chat = ChatOpenAI(model_name="gpt-4o", openai_api_key=api_key)

    system_message = SystemMessage(content="あなたは常に日本語で回答してください。")
    print("'exit' または 'quit' で終了します。")

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            break
        messages = [system_message, HumanMessage(content=user_input)]
        response = chat.invoke(messages)
        print("AI:", response.content)


if __name__ == "__main__":
    main()
