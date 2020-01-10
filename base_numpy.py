import numpy as np

data = np.array([[1,2,3],[4,5,6]])

print('******************')
print(f'生データ: {data}')
print('******************')
print(f'データ構造: {data.shape}')
print('******************')
print(f'次元: {data.ndim}')
print('******************')
print(f'サイズ: {data.size}')
print('******************')
print(f'データ型: {data.dtype}')

print('******************')
# 要素"1"の行列
data_b = np.ones((3,3,3))
print(f'要素「1」の行列3*3*3:\n{data_b}')

print('******************')
# 行列の初期化 (0とか1に揃えないので高速)
array_random = np.empty( (2,3) )
print(array_random)
print(f'データ型: {data.dtype}')


print('******************')
# 行列同士の計算
a = np.array( [10,20,30,40] )
b = np.array( [0, 1, 2, 3] )

c = a - b
print(c) # ⇒ [10 19 28 37]

print(b**2) # ⇒ [0 1 4 9]

print(np.sin(a)) # ⇒ [-0.54402111  0.91294525 -0.98803162  0.74511316]

print(a < 25) # ⇒ [ True  True False False]

print(a * b) # ⇒ [  0  20  60 120]


print('******************')
# 行列の軸毎の判定
data_c = np.array(
    [[1,2,3],
    [4,4,6]]
)

# 列方向 any判定
print(np.any(data_c%2==0, axis=0))

# 行方向 any判定
print(np.any(data_c%2==0, axis=1))

print(data_c.ndim)
