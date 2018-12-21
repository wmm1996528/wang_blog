import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(num=3, figsize=(8, 5))
# 设置X轴范围
plt.xlim((-1, 2))
# 设置Y轴范围
plt.ylim((-2, 3))
# 设置XY轴标题
plt.xlabel(u'价格', fontproperties='SimHei')
plt.ylabel(u'利润', fontproperties='SimHei')
# 设置刻度
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
'''
设置对应坐标用汉字或英文表示，后面的属性fontproperties表示中文可见，不乱码，
内部英文$$表示将英文括起来，r表示正则匹配，通过这个方式将其变为好看的字体
如果要显示特殊字符，比如阿尔法，则用转意符\alpha,前面的\ 表示空格转意
'''
plt.yticks([-2, -1.8, -1, 1.22, 3.],
           ['非常糟糕', '糟糕', r'$good\ \alpha$', r'$really\ good$', '超级好'], fontproperties='SimHei')
# plot 绘制线条
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
# 显示绘图
plt.show()
