import numpy as np
import matplotlib.pyplot as plt

# グラフ描画
data = np.arange(6).reshape(2,3)

print(data)

# 点描画
plt.plot(data[0],data[1],'o')
#plt.show()

# 線描画
plt.plot(data[0],data[1])
#plt.show()

plt.plot(data[0],data[1]**3)
#plt.show()

# figオブジェクト生成して描画
fig, ax = plt.subplots()
data = np.linspace(0,1,100)
ax.plot(data, np.sin(2*np.pi * data), color='tab:green', label='plot1' )
ax.plot(data, np.cos(2*np.pi * data), color='tab:red', label='plot2' )
ax.legend()
ax.grid()
#plt.show()




