from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# SIGNATE練習問題を処理してみる

# input data(=説明変数)
df_train = pd.read_csv('./data/SIGNATE/car/train.tsv', delimiter='\t')

print('\n*****************')
# 先頭行だけ表示
print('df_train head(3) \n', df_train.head(3))
print('*****************')

# 末尾行だけ表示
print('df_train tail(3) \n', df_train.tail(3))
print('*****************')

# 欠損を落とす
df_train = df_train.dropna()

# データ数表示
print('df_train shape(行数,カラム数)= ', df_train.shape)
print('*****************')

# データ要約統計表示 (全部が数値じゃないと意味ないっぽい)
# print('df_train describe\n', df_train.describe)
# print('*****************')

# データ数表示
print('df_train index= \n', df_train.index)
print('*****************')

# カラムをリスト型で取得
print('df_train columns= \n', df_train.columns)
print('*****************')

# カラムの要素を集計
print('df_train [class].value_counts\n', df_train['class'].value_counts())
print('*****************')

# カラムの要素のユニークな個数
print('df_train [class].nunique\n', df_train['class'].nunique())
print('*****************')


# カラム毎のtypeを表示
print('df_train dtypes=', df_train.dtypes)
print('*****************')

# 任意のカラムだけ表示
print('df_train [[class, safety]]= \n', df_train[['class', 'safety']].head(3))
print('*****************')

# 特定行だけ表示
print('df_train [100:103]\n', df_train[100:103])
print('*****************')

# 特定条件の行だけ表示
print('df_train [df_train[''class'']==''vgood'']\n',
      df_train[df_train['class'] == 'vgood'].head(3))
print('*****************')

# 特定カラムで複数条件
# 予約語をqueryに入れるとNGっぽい。
# 事前にカラム名を変更する。
df_train.rename(columns={'class':'CLASS'}, inplace=True)
print(df_train.columns)
print('df_train [CLASS, safety].query(class==unacc and safety==low)\n', df_train[['CLASS', 'safety']].query('CLASS == "unacc" and safety == "low"').head(10))
print('*****************')

# pivot表示 (数値じゃないと扱えない)
# print('df_train pivot. CLASS, index=doors, columns=safety\n',pd.pivot_table(df_train, values='CLASS', index='doors', columns='safety'))

### 文字列⇒数値化


conv_class = {'unacc':0, 'acc':1, 'good':2, 'vgood':3}
df_train.CLASS = df_train.CLASS.replace(conv_class)

print(df_train.head(10))
    
