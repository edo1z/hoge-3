# 評価指標

## 概要
モデルの性能を測る指標には、分類精度、適合率、再現率、F1 スコア、回帰での平均二乗誤差などがあります。

## 数学的背景
二値分類における F1 スコアは
\[ \mathrm{F1} = \frac{2 \cdot \mathrm{Precision} \cdot \mathrm{Recall}}{\mathrm{Precision} + \mathrm{Recall}} \]
と定義されます。回帰における平均二乗誤差は \(\mathrm{MSE} = \frac{1}{n} \sum (y_i - \hat{y}_i)^2\) です。
