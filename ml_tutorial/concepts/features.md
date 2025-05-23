# 特徴量とは - データから価値ある情報を抽出する

機械学習において「特徴量」（features）は、データから抽出される測定可能な特性や属性のことで、モデルの入力として使用されます。特徴量の選択と加工は、モデルの性能に大きく影響する重要なステップです。この章では、特徴量の基本概念から応用までを初心者にもわかりやすく解説します。

## 1. 特徴量とは何か

### 基本的な定義

特徴量とは、機械学習モデルが学習や予測に使用する個々の測定可能な特性や属性のことです。これらは通常、数値データとして表現されます。

例えば、家の価格予測モデルでは以下のような特徴量が考えられます：
- 床面積（平方メートル）
- 部屋の数
- 築年数
- 最寄り駅からの距離（分）
- エリアの治安レベル（数値化されたもの）

### 特徴量と目標変数の関係

機械学習では：
- **特徴量（X）**: モデルへの入力値（説明変数、独立変数とも呼ばれる）
- **目標変数（y）**: モデルが予測しようとする値（被説明変数、従属変数、ラベルとも呼ばれる）

モデルは特徴量と目標変数の関係を学習し、新しい特徴量のデータが与えられたときに目標変数の値を予測します。

### 特徴量の表現方法

データサイエンスでは、特徴量は通常、表形式（テーブル）で表現されます：

| ID | 床面積(m²) | 部屋数 | 築年数 | 駅距離(分) | 価格(万円) |
|----|------------|--------|--------|------------|-----------|
| 1  | 65         | 3      | 15     | 5          | 3,200     |
| 2  | 80         | 4      | 5      | 10         | 4,500     |
| 3  | 50         | 2      | 30     | 3          | 2,800     |

ここで、「価格」が目標変数で、他の列が特徴量です。

## 2. 特徴量の種類

### 数値型特徴量

連続的な値を取る特徴量です。
- **例**: 年齢、収入、温度、重量など
- **特徴**: そのまま数値として使用できる

### カテゴリ型特徴量

限られた数のカテゴリから値を取る特徴量です。
- **例**: 性別（男/女）、血液型（A/B/O/AB）、都道府県名など
- **特徴**: 機械学習で使用するには数値に変換する必要がある

### 順序型特徴量

順序関係のあるカテゴリ型特徴量です。
- **例**: 学歴（小/中/高/大）、満足度（低/中/高）など
- **特徴**: 順序関係を考慮して数値に変換する必要がある

### テキスト型特徴量

文字列や文書からなる特徴量です。
- **例**: 商品レビュー、ツイート、ニュース記事など
- **特徴**: テキスト処理技術を使って数値ベクトルに変換する必要がある

### 画像型特徴量

画像データからなる特徴量です。
- **例**: 写真、医療画像、衛星画像など
- **特徴**: 画像処理技術を使ってピクセル値や抽出特徴を数値化する

### 時系列型特徴量

時間的な順序を持つデータからなる特徴量です。
- **例**: 株価の推移、センサーの測定値の変化、天気の変化など
- **特徴**: 時間的な依存関係を考慮した処理が必要

## 3. 特徴量の前処理と変換

生データをそのまま機械学習モデルに入力することは少なく、通常は何らかの前処理や変換を行います。

### 数値型特徴量の前処理

#### スケーリング（正規化・標準化）

異なるスケールの特徴量を比較可能にするために行います。

- **標準化（Standardization）**: 平均0、標準偏差1にする
  ```
  x_new = (x - mean) / std
  ```

- **正規化（Normalization）**: 0〜1の範囲にする
  ```
  x_new = (x - min) / (max - min)
  ```

例：
```
元データ: [100, 200, 300, 400, 500]
標準化後: [-1.41, -0.71, 0, 0.71, 1.41]
正規化後: [0, 0.25, 0.5, 0.75, 1]
```

#### 対数変換

非常に大きな値の範囲を持つデータや、指数的に分布するデータに対して使用します。

```
x_new = log(x)
```

例：
```
元データ: [1, 10, 100, 1000, 10000]
対数変換後: [0, 2.3, 4.6, 6.9, 9.2]
```

### カテゴリ型特徴量の変換

#### ワンホットエンコーディング

カテゴリをバイナリフラグの組み合わせに変換します。

例：
```
元データ: ['赤', '青', '緑']
変換後：
赤: [1, 0, 0]
青: [0, 1, 0]
緑: [0, 0, 1]
```

#### ラベルエンコーディング

カテゴリに整数値を割り当てます（順序関係がある場合に適切）。

例：
```
元データ: ['小', '中', '高', '大']
変換後: [0, 1, 2, 3]
```

### 特徴量のビニング（離散化）

連続的な数値を区間（ビン）に分割して、カテゴリとして扱います。

例：
```
年齢: [22, 35, 48, 65, 71]
年齢区分に変換: ['若年(~30)', '中年(31-50)', '中年(31-50)', '高年(51~)', '高年(51~)']
```

## 4. 特徴量エンジニアリング

特徴量エンジニアリングとは、生データから機械学習に適した特徴量を作成・選択・変換するプロセスです。モデルの性能向上には、良い特徴量の設計が不可欠です。

### 特徴量の作成

#### 数学的変換

既存の特徴量に数学的操作を適用して新しい特徴量を作ります。

例：
- 面積 = 幅 × 奥行き
- 密度 = 重量 ÷ 体積
- 割合 = 部分 ÷ 全体

#### 交互作用特徴量

複数の特徴量を組み合わせて新しい特徴量を作ります。

例：
- 年齢 × 収入
- 天気（晴れ/雨）× 曜日（平日/休日）

#### 時間ベースの特徴量

日時データから様々な特徴量を抽出します。

例：
- 日付から曜日、月、四半期、年を抽出
- 営業日/休日フラグの作成
- 特定のイベント（休日、セールなど）からの日数

#### 集約特徴量

グループごとの統計量を特徴量とします。

例：
- 顧客ごとの平均購入額
- 商品カテゴリごとの売上合計
- エリアごとの平均家賃

### 特徴量選択

多すぎる特徴量はモデルの過学習を招くことがあります。効果的な特徴量のみを選択することが重要です。

#### フィルター法

統計的な指標に基づいて特徴量を選択します。

- **分散フィルタリング**: 分散が小さすぎる（ほぼ一定値の）特徴量を除外
- **相関フィルタリング**: 目標変数との相関が高い特徴量を選択
- **カイ二乗検定**: カテゴリ型特徴量と目標変数の関連を評価

#### ラッパー法

モデルの性能に基づいて特徴量を選択します。

- **前向き選択法**: 空の特徴量セットから始め、最も性能向上に寄与する特徴量を1つずつ追加
- **後向き消去法**: 全特徴量から始め、最も影響の少ない特徴量を1つずつ削除
- **再帰的特徴量削除**: モデルの重要度に基づいて特徴量を再帰的に削除

#### 埋め込み法

モデルの学習過程で特徴量選択を行います。

- **L1正則化（Lasso）**: 重要でない特徴量の係数を0に近づける
- **決定木ベースの重要度**: ランダムフォレストなどで特徴量の重要度を評価

## 5. 特徴量エンジニアリングの実践例

### 家の価格予測の例

原データ：

| 床面積(m²) | 築年数 | 駅距離(分) | エリア  | 日付       |
|------------|--------|------------|---------|------------|
| 65         | 15     | 5          | 東京    | 2023-01-15 |
| 80         | 5      | 10         | 横浜    | 2023-02-20 |
| 50         | 30     | 3          | 千葉    | 2023-03-10 |

特徴量エンジニアリング後：

| 床面積(m²) | 築年数 | log(築年数) | 駅距離(分) | エリア_東京 | エリア_横浜 | エリア_千葉 | 月      | 四半期 | 面積_駅距離比 |
|------------|--------|-------------|------------|-------------|-------------|-------------|---------|--------|---------------|
| 65         | 15     | 2.71        | 5          | 1           | 0           | 0           | 1       | 1      | 13            |
| 80         | 5      | 1.61        | 10         | 0           | 1           | 0           | 2       | 1      | 8             |
| 50         | 30     | 3.40        | 3          | 0           | 0           | 1           | 3       | 1      | 16.67         |

### テキスト分類の例

原データ：

| 商品レビュー                           | 評価 |
|---------------------------------------|------|
| "とても使いやすく、長持ちします。大満足！" | 5    |
| "普通に使えるけど、特に感動はない"       | 3    |
| "すぐに壊れた。最悪の買い物だった"       | 1    |

特徴量エンジニアリング後（Bag of Words）：

| とても | 使いやすく | 長持ち | 満足 | 普通 | 感動 | すぐに | 壊れ | 最悪 | 買い物 | 評価 |
|--------|------------|--------|------|------|------|--------|------|------|--------|------|
| 1      | 1          | 1      | 1    | 0    | 0    | 0      | 0    | 0    | 0      | 5    |
| 0      | 0          | 0      | 0    | 1    | 1    | 0      | 0    | 0    | 0      | 3    |
| 0      | 0          | 0      | 0    | 0    | 0    | 1      | 1    | 1    | 1      | 1    |

## 6. Pythonによる特徴量エンジニアリングの実装例

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# サンプルデータの作成
data = {
    '床面積': [65, 80, 50, 70, 90],
    '築年数': [15, 5, 30, 10, 20],
    '駅距離': [5, 10, 3, 8, 15],
    'エリア': ['東京', '横浜', '千葉', '東京', '横浜'],
    '価格': [3200, 4500, 2800, 3500, 4000]
}

df = pd.DataFrame(data)
print("元のデータ:")
print(df)

# 特徴量と目標変数の分離
X = df.drop('価格', axis=1)
y = df['価格']

# 数値特徴量のリスト
numeric_features = ['床面積', '築年数', '駅距離']

# カテゴリ特徴量のリスト
categorical_features = ['エリア']

# 前処理パイプラインの構築
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# 特徴量エンジニアリング
# 新しい特徴量の作成
df['log_築年数'] = np.log1p(df['築年数'])
df['面積_駅距離比'] = df['床面積'] / df['駅距離']
print("\n特徴量追加後:")
print(df)

# 前処理の適用
X_processed = preprocessor.fit_transform(X)

# 特徴量選択（上位3特徴）
selector = SelectKBest(f_regression, k=3)
X_selected = selector.fit_transform(X_processed, y)

print("\n前処理後のデータ形状:", X_processed.shape)
print("特徴量選択後のデータ形状:", X_selected.shape)

# 特徴量の重要度（F値）
feature_scores = pd.DataFrame({
    'F値': selector.scores_,
    '特徴量': preprocessor.get_feature_names_out()
})
print("\n特徴量の重要度:")
print(feature_scores.sort_values('F値', ascending=False))
```

## 7. 特徴量エンジニアリングのベストプラクティス

### 特徴量エンジニアリングのプロセス

1. **データの理解**: ドメイン知識を活用し、データの意味を理解する
2. **仮説の立案**: どの特徴量が目標変数に影響を与えそうか仮説を立てる
3. **特徴量の作成**: 仮説に基づいて、新しい特徴量を設計・作成する
4. **特徴量の評価**: 作成した特徴量がモデルの性能向上に寄与するか評価する
5. **反復**: 上記のプロセスを繰り返し、特徴量を改善する

### よくある間違いと注意点

- **データリーク**: テスト時には利用できない情報を特徴量に使用してしまう
- **過度な特徴量エンジニアリング**: 過学習を招く恐れがある
- **次元の呪い**: 特徴量が多すぎると、モデルの性能が低下する可能性がある
- **特徴量選択の無視**: 不要な特徴量を削除せずにモデルに投入してしまう

### 業界別の特徴量エンジニアリング例

#### 金融業界
- 支出/収入比率
- 過去の支払い遅延回数
- クレジットスコア
- 最終取引からの経過日数

#### eコマース
- 購入頻度
- 平均購入金額
- 特定カテゴリの購入比率
- 最後の購入からの日数

#### 医療分野
- 年齢・体重の比率（BMI）
- 特定の症状の組み合わせ
- 過去の診察回数
- 薬の服用期間

## まとめ

特徴量は機械学習モデルの性能を大きく左右する重要な要素です。良い特徴量を設計するには：

1. **データを深く理解する**: ドメイン知識を活用し、データの意味を把握する
2. **適切な前処理を行う**: スケーリング、エンコーディングなどの基本処理を適用する
3. **新しい特徴量を創造する**: 既存データから有益な情報を抽出する特徴量を設計する
4. **関連性の高い特徴量を選択する**: モデルの予測力を高める特徴量のみを使用する
5. **反復的に改善する**: 特徴量の効果を評価し、継続的に改善する

特徴量エンジニアリングは、科学的な方法論だけでなく、創造性や直感も必要とする芸術的な側面も持っています。データの特性や解決しようとする問題に合わせて、適切な特徴量を設計することが、成功する機械学習プロジェクトの鍵となります。

次の章では、[教師あり学習](../supervised_learning.md)の基本的な概念と手法について詳しく見ていきましょう。