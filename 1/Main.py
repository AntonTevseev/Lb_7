from numpy import *
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = []
for i in x:
    y.append(5 * math.sin(10 * i) * math.sin(3 * i) / float(i ^ int(1 / 2)))

plt.plot(x, y)
plt.savefig('graph.png', dpi=200)
