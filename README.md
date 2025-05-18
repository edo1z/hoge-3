# 簡易AIチャット

このリポジトリには、LangChain と OpenAI GPT-4o を利用した簡単なチャットプログラム `chat.py` が含まれています。

## 使い方

1. 必要なパッケージをインストールします。
   ```bash
   pip install -r requirements.txt
   ```
2. `.env` ファイルを作成し、`OPENAI_API_KEY` を設定します。サンプルとして `.env.example` を用意しています。
3. チャットを起動します。
   ```bash
   python chat.py
   ```
4. `exit` または `quit` を入力すると終了します。

## 機械学習チュートリアル

`ml_tutorial` ディレクトリに、機械学習の基本的な事項と数学的解説をまとめた Markdown ファイルを用意しています。まずは [index.md](ml_tutorial/index.md) から参照してください。

## 動画生成スクリプト

プロジェクトルートの `create_movie` ディレクトリに、図形が動く 20 秒の動画を生成
するスクリプト `create_shapes_video.py` を用意しています。以下のコマンドで実行でき
ます。

```bash
cd create_movie
python create_shapes_video.py
```

実行すると `create_movie` ディレクトリ内に `shapes.mp4` が作成されます。
