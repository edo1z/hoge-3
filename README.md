# 簡易AIチャット

このリポジトリには、LangChain と OpenAI GPT-4o を利用した簡単なチャットプログラム `chat.py` が含まれています。moviepy を使った動画編集もチャットから実行できます。

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

### 動画編集への応用

`chat.py` には MoviePy を使った簡単な動画編集機能が組み込まれています。
`create_movie/shapes.mp4` など編集したい動画を用意した上で、
チャット内で以下のように依頼することで自動編集が可能です。

```
動画を5秒から10秒まで切り出して output.mp4 に保存して
```

その他テキストの重ね合わせや再生速度変更にも対応しています。

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

## 動画編集アシスタント

`chat.py` は MoviePy を利用した簡単な動画編集ツールを備えています。編集したい動画を用意したうえで起動してください。サンプル動画として前節の `create_shapes_video.py` で作成した `shapes.mp4` を利用できます。

1. `chat.py` を起動します。
   ```bash
   python chat.py
   ```
2. チャット上で編集内容を指示すると、自動的に動画を加工します。
   例:
   - `shapes.mp4` の 0 秒から 5 秒までを `cut.mp4` に保存
   - `shapes.mp4` に文字を 2 秒間重ねて `text.mp4` に保存
   - `shapes.mp4` を 2 倍速にして `fast.mp4` に保存
3. `exit` または `quit` で終了します。

## Playwright MCP サーバとブラウザ操作チャット

`mcp-server` ディレクトリに Playwright MCP を利用した簡易サーバを用意しました。
`ts-node` で起動できます。

```bash
cd mcp-server
npm install        # 依存パッケージをインストール
npm run start      # MCP サーバを起動
```

起動後、`mcp_chat.py` を実行すると MCP サーバをツールとして利用した
ブラウザ操作チャットが起動します。

```bash
python mcp_chat.py
```

`exit` または `quit` で終了します。
