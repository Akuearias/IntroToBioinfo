import matplotlib.pyplot as plt
import numpy as np

c = 4 / 9

# 生成 x 值
x_values = np.linspace(-1, 4, 1000)
# 使用 np.piecewise 定义分段函数
y_values = np.piecewise(
    x_values,
    [x_values < 0,
     (x_values >= 0) & (x_values < 1.5),
     (x_values >= 1.5) & (x_values < 3),
     x_values >= 3],
    [0,
     lambda x: c * x,
     lambda x: c * (3 - x),
     0]
)

y2_values = np.piecewise(x_values, [(x_values >= 0) & (x_values <= 3)], [1 / 3])

# 绘制函数图像
plt.plot(x_values, y2_values, label='f(y)', color='red')
plt.plot(x_values, y_values, label='f(x)', color='blue')
plt.title('Graph of f(x) and f(y)')
plt.xlabel('x')
plt.ylabel('f(x) or f(y)')
plt.legend()
plt.grid(True)
plt.show()
