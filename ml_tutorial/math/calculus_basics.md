# 微分の基礎 - 機械学習のための数学

機械学習において微分（微積分学）は、モデルの学習や最適化に欠かせない数学的ツールです。特に勾配降下法などのアルゴリズムは微分の概念に基づいています。この章では、高校数学レベルから微分の基礎概念を分かりやすく解説します。

## 1. 微分とは何か - 変化率を測る道具

### 微分の直感的な理解

微分とは、ある関数の「変化率」や「傾き」を測る方法です。高校数学では「導関数」として習いますが、これは「入力値が少し変わったとき、出力値がどれだけ変わるか」を示すものです。

例えば、車の位置を時間の関数と考えると、その微分は「速度」を表します。さらに速度を微分すると「加速度」になります。

### なぜ機械学習で微分が重要なのか

機械学習では、モデルの性能を測る「損失関数」（エラーの大きさを表す関数）を最小化することが目標です。微分を使うと、どの方向に進めば損失関数の値が小さくなるか（＝モデルが改善するか）を知ることができます。

## 2. 導関数 - 関数の傾きを求める

### 導関数の定義

関数 $f(x)$ の $x$ に関する導関数 $f'(x)$ または $\frac{df}{dx}$ は、点 $x$ における関数の傾きを表します。

数式による定義：
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

これは「$x$ から少し動いたとき（$h$ だけ動いたとき）の $f(x)$ の変化の割合」を意味します。

### 導関数の直感的な意味

導関数 $f'(x)$ は、各点 $x$ における接線の傾きを表します。

- $f'(x) > 0$ のとき：関数は $x$ で増加している（右上がり）
- $f'(x) < 0$ のとき：関数は $x$ で減少している（右下がり）
- $f'(x) = 0$ のとき：関数は $x$ で水平になっている（極大値、極小値、または変曲点）

### 基本的な導関数の公式

以下に、よく使われる関数の導関数を示します：

1. 定数関数: $f(x) = c$ → $f'(x) = 0$
2. 一次関数: $f(x) = ax + b$ → $f'(x) = a$
3. 二次関数: $f(x) = ax^2 + bx + c$ → $f'(x) = 2ax + b$
4. 一般の多項式: $f(x) = x^n$ → $f'(x) = nx^{n-1}$
5. 指数関数: $f(x) = e^x$ → $f'(x) = e^x$
6. 対数関数: $f(x) = \ln(x)$ → $f'(x) = \frac{1}{x}$
7. 三角関数: $f(x) = \sin(x)$ → $f'(x) = \cos(x)$
8. 三角関数: $f(x) = \cos(x)$ → $f'(x) = -\sin(x)$

### 導関数の計算例

例1: $f(x) = 3x^2 + 2x - 5$ の導関数を求める

$$f'(x) = 6x + 2$$

例2: $f(x) = e^{2x} \sin(x)$ の導関数を求める（積の微分法則を使用）

$$f'(x) = e^{2x} \cdot 2 \cdot \sin(x) + e^{2x} \cdot \cos(x) = e^{2x}(2\sin(x) + \cos(x))$$

### 微分の法則

1. **和の微分**: $(f(x) + g(x))' = f'(x) + g'(x)$
2. **差の微分**: $(f(x) - g(x))' = f'(x) - g'(x)$
3. **定数倍の微分**: $(c \cdot f(x))' = c \cdot f'(x)$
4. **積の微分**: $(f(x) \cdot g(x))' = f'(x) \cdot g(x) + f(x) \cdot g'(x)$
5. **商の微分**: $\left(\frac{f(x)}{g(x)}\right)' = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{(g(x))^2}$
6. **合成関数の微分（連鎖律）**: $(f(g(x)))' = f'(g(x)) \cdot g'(x)$

## 3. 偏微分 - 多変数関数の微分

### 偏微分とは

実際の機械学習では、入力変数（特徴量）が複数あることがほとんどです。多変数関数 $f(x, y, z, ...)$ の「偏微分」は、一つの変数だけを変化させて、他の変数を定数として扱ったときの微分です。

$x$ に関する偏微分は $\frac{\partial f}{\partial x}$ と表記します。

### 偏微分の計算方法

多変数関数の偏微分は、微分する変数以外をすべて定数として扱い、通常の導関数と同じように計算します。

例: $f(x, y) = 3x^2y + 2xy^3 - 5y$ の $x$ に関する偏微分

計算では $y$ を定数として扱います：
$$\frac{\partial f}{\partial x} = 6xy + 2y^3$$

同様に、$y$ に関する偏微分は：
$$\frac{\partial f}{\partial y} = 3x^2 + 6xy^2 - 5$$

### 偏微分の直感的な意味

偏微分 $\frac{\partial f}{\partial x}$ は、「他の変数を固定して、$x$ だけを少し変えたとき、関数 $f$ がどれだけ変化するか」を表します。3次元のグラフでは、$x$ 方向の傾きを表します。

## 4. 勾配 - 多変数関数の最も急な方向

### 勾配（グラディエント）とは

勾配は、多変数関数の各変数に関する偏微分をベクトルとしてまとめたものです。関数 $f(x_1, x_2, ..., x_n)$ の勾配 $\nabla f$ は次のように定義されます：

$$\nabla f = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, ..., \frac{\partial f}{\partial x_n} \right)$$

### 勾配の性質

勾配には重要な性質があります：

1. 勾配ベクトルは、関数の値が最も急激に増加する方向を指します
2. 勾配ベクトルの大きさは、その方向での増加率の大きさを表します
3. 勾配ベクトルは常に関数の等高線（同じ関数値を持つ点の集合）に対して垂直です

### 勾配の計算例

例: $f(x, y) = 3x^2y + 2xy^3 - 5y$ の勾配を求める

$x$ に関する偏微分: $\frac{\partial f}{\partial x} = 6xy + 2y^3$

$y$ に関する偏微分: $\frac{\partial f}{\partial y} = 3x^2 + 6xy^2 - 5$

勾配: $\nabla f(x, y) = (6xy + 2y^3, 3x^2 + 6xy^2 - 5)$

特定の点、例えば $(x, y) = (2, 1)$ での勾配を求めると：

$\nabla f(2, 1) = (6 \cdot 2 \cdot 1 + 2 \cdot 1^3, 3 \cdot 2^2 + 6 \cdot 2 \cdot 1^2 - 5) = (12 + 2, 12 + 12 - 5) = (14, 19)$

この点では、関数は $(14, 19)$ の方向に最も急激に増加します。

## 5. 最適化と勾配降下法

### 最適化問題

機械学習では、モデルのパラメータを調整して損失関数を最小化することが目標です。つまり：

$$\theta^* = \arg\min_{\theta} L(\theta)$$

ここで、$\theta$ はモデルのパラメータ、$L(\theta)$ は損失関数、$\theta^*$ は最適なパラメータ値です。

### 勾配降下法の基本的な考え方

勾配降下法は、勾配の反対方向（関数値が減少する方向）に少しずつパラメータを更新することで、損失関数の最小値を見つける方法です。

更新式：
$$\theta_{new} = \theta_{old} - \alpha \nabla L(\theta_{old})$$

ここで、$\alpha$ は学習率（ステップサイズ）と呼ばれるハイパーパラメータで、一度にどれだけパラメータを更新するかを制御します。

### 勾配降下法の直感的な理解

山の頂上（最大値）または谷の底（最小値）を探す登山者をイメージしてください。勾配降下法は、「常に最も急な下り坂の方向に進む」という戦略です。

この方法では、現在地の周りでどの方向が最も急な下り坂かを調べ（勾配を計算し）、その方向に少し進みます（パラメータを更新）。このプロセスを繰り返して、最終的に谷の底（損失関数の最小値）に到達します。

### 勾配降下法の種類

1. **バッチ勾配降下法**：すべての訓練データを使って勾配を計算
2. **確率的勾配降下法（SGD）**：1つのデータ点を使って勾配を計算
3. **ミニバッチ勾配降下法**：データの一部（ミニバッチ）を使って勾配を計算（最も一般的）

### 勾配降下法の実装例

二次関数 $f(x) = x^2$ の最小値を勾配降下法で求める例：

```python
import numpy as np
import matplotlib.pyplot as plt

# 関数とその導関数（勾配）
def f(x):
    return x**2

def df(x):
    return 2*x

# 勾配降下法
def gradient_descent(start_x, learning_rate, num_iterations):
    x = start_x
    x_history = [x]

    for i in range(num_iterations):
        x = x - learning_rate * df(x)
        x_history.append(x)

    return x, x_history

# パラメータ
start_x = 5.0      # 初期値
learning_rate = 0.1  # 学習率
num_iterations = 30  # 繰り返し回数

# 勾配降下法を実行
final_x, x_history = gradient_descent(start_x, learning_rate, num_iterations)

# 結果の表示
print(f"最小値を与えるx: {final_x}")
print(f"f(x)の最小値: {f(final_x)}")

# 可視化
x = np.linspace(-6, 6, 100)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='f(x) = x^2')
plt.scatter(x_history, [f(x_i) for x_i in x_history], c='r', s=100, alpha=0.5)
plt.title('勾配降下法による最適化')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
```

## 6. 多変数関数の最適化

実際の機械学習モデルでは、多数のパラメータを同時に最適化する必要があります。この場合、勾配は多次元ベクトルとなります。

### 二変数関数の例

二変数関数 $f(x, y) = x^2 + 2y^2$ の最小値を勾配降下法で求める例：

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 関数とその勾配
def f(x, y):
    return x**2 + 2*y**2

def grad_f(x, y):
    return np.array([2*x, 4*y])

# 勾配降下法
def gradient_descent_2d(start_point, learning_rate, num_iterations):
    point = np.array(start_point, dtype=float)
    point_history = [point.copy()]

    for i in range(num_iterations):
        gradient = grad_f(point[0], point[1])
        point = point - learning_rate * gradient
        point_history.append(point.copy())

    return point, np.array(point_history)

# パラメータ
start_point = [4.0, 3.0]  # 初期値 (x, y)
learning_rate = 0.1       # 学習率
num_iterations = 20       # 繰り返し回数

# 勾配降下法を実行
final_point, point_history = gradient_descent_2d(start_point, learning_rate, num_iterations)

# 結果の表示
print(f"最小値を与える点 (x, y): {final_point}")
print(f"f(x, y)の最小値: {f(final_point[0], final_point[1])}")

# 可視化 - 3D表面プロット
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure(figsize=(12, 10))

# 3D表面プロット
ax1 = fig.add_subplot(121, projection='3d')
surface = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax1.scatter(point_history[:, 0], point_history[:, 1],
           [f(p[0], p[1]) for p in point_history],
           c='r', s=50, alpha=0.6)
ax1.set_title('勾配降下法の軌跡 (3D)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')

# 等高線プロット
ax2 = fig.add_subplot(122)
contour = ax2.contour(X, Y, Z, 20, cmap='viridis')
ax2.scatter(point_history[:, 0], point_history[:, 1], c='r', s=50, alpha=0.6)
ax2.plot(point_history[:, 0], point_history[:, 1], 'r--', alpha=0.3)
ax2.set_title('勾配降下法の軌跡 (等高線)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

plt.tight_layout()
plt.show()
```

## 7. 微分と機械学習の具体的な関係

### 線形回帰と最小二乗法

線形回帰では、実データ点と予測線の間の平均二乗誤差（MSE）を最小化します：

$$L(w, b) = \frac{1}{n}\sum_{i=1}^{n}(y_i - (wx_i + b))^2$$

この損失関数を $w$ と $b$ に関して偏微分し、勾配を計算：

$$\frac{\partial L}{\partial w} = -\frac{2}{n}\sum_{i=1}^{n}x_i(y_i - (wx_i + b))$$

$$\frac{\partial L}{\partial b} = -\frac{2}{n}\sum_{i=1}^{n}(y_i - (wx_i + b))$$

これらの偏微分を使って、勾配降下法でパラメータを更新します。

### ニューラルネットワークと誤差逆伝播法

ニューラルネットワークでは、誤差逆伝播法（バックプロパゲーション）で勾配を計算します。これは、連鎖律を使って出力層から入力層に向かって勾配を伝播させる方法です。

例えば、単純なニューラルネットワークの損失関数を $L$ とし、ある重み $w_{ij}$ について：

$$\frac{\partial L}{\partial w_{ij}} = \frac{\partial L}{\partial a_j} \cdot \frac{\partial a_j}{\partial z_j} \cdot \frac{\partial z_j}{\partial w_{ij}}$$

ここで：
- $a_j$ はノード $j$ の活性化値
- $z_j$ はノード $j$ の重み付き入力の合計
- 連鎖律を使って複雑な関数の微分を簡単な部分に分解しています

## まとめ

微分（微積分学）は機械学習の核となる数学概念です。この章で学んだ内容：

- **導関数**: 関数の変化率や傾きを表す
- **偏微分**: 多変数関数の一つの変数に関する変化率
- **勾配**: 多変数関数のすべての変数に関する偏微分をまとめたベクトル
- **勾配降下法**: 勾配の反対方向に進むことで関数の最小値を見つける最適化アルゴリズム
- **機械学習への応用**: 損失関数の最小化、線形回帰、ニューラルネットワークの学習

これらの概念は、特に[勾配降下法](../gradient_descent.md)や[ニューラルネットワーク](../neural_networks.md)の理解に不可欠です。

次の章では、機械学習の基本コンセプトである[教師あり学習](../supervised_learning.md)について詳しく見ていきましょう。