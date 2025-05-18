# 機械学習のための環境セットアップ

機械学習を始めるには、適切なソフトウェア環境を準備する必要があります。この章では、Python、Jupyter Notebookなどの基本的なツールと、主要な機械学習ライブラリのインストール方法を解説します。

## Pythonのインストール

Pythonは機械学習において最も広く使われているプログラミング言語です。その理由は、シンプルな構文と豊富な機械学習ライブラリの存在にあります。

### Windowsへのインストール

1. [Python公式サイト](https://www.python.org/downloads/)にアクセスします
2. 最新バージョン（3.9以上推奨）のWindowsインストーラーをダウンロードします
3. ダウンロードしたインストーラーを実行します
4. インストール時に「**Add Python to PATH**」オプションにチェックを入れることを忘れないでください
5. 「Install Now」をクリックしてインストールを完了します

### macOSへのインストール

macOSには通常Pythonがプリインストールされていますが、最新版が必要です。

1. [Python公式サイト](https://www.python.org/downloads/)から最新版のmacOSインストーラーをダウンロード
2. ダウンロードしたパッケージを開き、インストール手順に従います

あるいは、Homebrewを使ってインストールする方法もあります：

```bash
brew install python
```

### Linuxへのインストール

多くのLinuxディストリビューションにはPythonがプリインストールされています。最新版をインストールするには：

Ubuntu/Debian系：
```bash
sudo apt update
sudo apt install python3 python3-pip
```

Fedora/RHEL系：
```bash
sudo dnf install python3 python3-pip
```

### インストール確認

ターミナル（コマンドプロンプト）を開き、以下のコマンドを実行してPythonのバージョンを確認します：

```bash
python --version
```

または

```bash
python3 --version
```

## 仮想環境の作成（オプションですが推奨）

異なるプロジェクトで異なるライブラリバージョンを使用できるよう、仮想環境を作成することをお勧めします。

```bash
# 仮想環境の作成
python -m venv ml_env

# 仮想環境の有効化
# Windowsの場合
ml_env\Scripts\activate

# macOS/Linuxの場合
source ml_env/bin/activate
```

## 主要な機械学習ライブラリのインストール

Python用の優れた機械学習ライブラリがたくさんあります。以下のコマンドで主要なライブラリをインストールできます：

```bash
pip install numpy pandas matplotlib scikit-learn jupyter
```

これでインストールされるライブラリ：

- **NumPy**: 数値計算のための基本ライブラリ
- **pandas**: データ操作と分析のためのライブラリ
- **Matplotlib**: データ可視化のためのライブラリ
- **scikit-learn**: 機械学習アルゴリズムを実装したライブラリ
- **Jupyter**: インタラクティブなノートブック環境

### TensorFlowのインストール（深層学習用）

ニューラルネットワークなどの深層学習に興味がある場合は、TensorFlowもインストールしておくとよいでしょう：

```bash
pip install tensorflow
```

### PyTorchのインストール（深層学習用の代替）

TensorFlowの代わりにPyTorchを使いたい場合：

```bash
pip install torch torchvision
```

## Jupyter Notebookの使い方

Jupyter Notebookは、コードの実行結果やビジュアライゼーション、説明文をひとつのドキュメントにまとめることができる強力なツールです。

### Jupyterの起動

ターミナル（コマンドプロンプト）で以下のコマンドを実行します：

```bash
jupyter notebook
```

これにより、ブラウザが自動的に開き、Jupyterのホーム画面が表示されます。

### 新しいノートブックの作成

1. 右上の「New」ボタンをクリックし、「Python 3」を選択します
2. これで新しいノートブックが作成され、Pythonコードを実行できるようになります

### Jupyterノートブックの基本操作

- **セルの実行**: Shift + Enterキーを押します
- **新しいセルの追加**: 「+」ボタンをクリックするか、Alt + Enterを押します
- **セルタイプの変更**: ツールバーの「Cell Type」ドロップダウンでコード（Code）とテキスト（Markdown）を切り替えられます

### Jupyter Labの使用（代替オプション）

より高度なユーザーインターフェースが必要な場合は、Jupyter Labを使用できます：

```bash
pip install jupyterlab
jupyter lab
```

## Google Colabの利用（クラウドオプション）

ローカル環境のセットアップが難しい場合や、GPUを無料で使いたい場合は、Google Colaboratoryを利用すると便利です。

1. [Google Colabのウェブサイト](https://colab.research.google.com/)にアクセスします
2. Googleアカウントでログインします
3. 新しいノートブックを作成するか、既存のノートブックを開きます

Colabの利点：
- インストール不要でブラウザから利用可能
- 無料でGPUを使用可能
- Googleドライブとの連携が便利

## 動作確認：最初の機械学習コード

環境が正しくセットアップされたことを確認するために、簡単な機械学習プログラムを実行してみましょう。Jupyterノートブックで以下のコードを入力して実行します：

```python
# 必要なライブラリのインポート
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# データセットのロード
iris = load_iris()
X = iris.data
y = iris.target

# データの分割（訓練用と評価用）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# モデルの構築と訓練
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# モデルの評価
accuracy = knn.score(X_test, y_test)
print(f"モデルの正解率: {accuracy:.2f}")

# データの可視化（最初の2つの特徴量のみを使用）
plt.figure(figsize=(10, 6))
for i in range(3):
    plt.scatter(X[y == i, 0], X[y == i, 1], label=iris.target_names[i])
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title("アヤメデータセットの可視化")
plt.legend()
plt.show()
```

このコードが問題なく実行され、グラフが表示されれば、環境のセットアップは成功です！

## トラブルシューティング

### よくあるエラーと解決方法

1. **ModuleNotFoundError**: 必要なライブラリがインストールされていない場合に発生します。
   解決策: `pip install <ライブラリ名>` で必要なライブラリをインストールします。

2. **ImportError: DLL load failed**: Windowsで特定のライブラリのDLLが見つからない場合に発生します。
   解決策: Microsoft Visual C++ Redistributableをインストールします。

3. **PermissionError**: インストール時に権限がない場合に発生します。
   解決策: Windowsならコマンドプロンプトを管理者として実行、macOS/Linuxなら `sudo` コマンドを使用します。

### ヘルプの探し方

- **StackOverflow**: プログラミングの質問回答サイト
- **GitHub Issues**: 各ライブラリのGitHubリポジトリの「Issues」セクション
- **公式ドキュメント**: 各ライブラリの公式ドキュメントを参照する

## 次のステップ

これで機械学習を始めるための環境が整いました。次に、機械学習に必要な[線形代数の基礎](../math/linear_algebra_basics.md)から学んでいきましょう。