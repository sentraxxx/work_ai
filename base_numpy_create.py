import numpy as np

# 要素指定
a = np.array([1,2,3])
print('a= ', a)
print('*************************')

# 0からの要素数
b = np.arange(10)
print('b= ',b)
print('*************************')

# start, stop, 公差
c = np.arange(0, 5, 0.5)
print('c= ',c)
print('*************************')

# start, stop, 要素数
d = np.linspace(1,5,9)
print('d= ', d)
print('*************************')


# 逆順
e = d[::-1]
print('e= ',e)
print('*************************')

# 次元変換
f = np.arange(12)
print('f= ', f)

print('f(2*6)=\n', f.reshape(2,6))

print('f(reshapeは変わらない)= ', f)

f.resize(3,4)

print('f(resizeは変わる)= ', f)
print('*************************')

# 乱数生成
g = np.random.rand(2,100)

print('g= ', g)
