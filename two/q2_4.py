import matplotlib.pyplot as plt
import math


r = 100.0
s = 10000.0
n = math.inf
a = [r + s]
while a[-1] > (1.0e-3 * sum(a) + 1.0e-13):
    a.append(r + s * a[-1] / (s + a[-1]))

b = [r + s]
for i in range(49):
    b.append(r + s * b[-1] / (s + b[-1]))


c = []
for i in range(len(b)):
    c.append(math.log(b[i]) / math.log(a[i]))


plt.plot(c)
plt.savefig('q2_4.png')
