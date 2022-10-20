import matplotlib.pyplot as plt
import math
import numpy as np


r = 100.0
s = 10000.0
n = math.inf
a = [r + s]
while a[-1] > (1.0e-3 * sum(a) + 1.0e-13):
    a.append(r + s * a[-1] / (s + a[-1]))

print(a[-1])

b = [r + s]
for i in range(50):
    b.append(r + s * b[-1] / (s + b[-1]))


c = []
if len(a) >= len(b):
    for i in range(len(b)):
        c.append(math.log(b[i]) - math.log(a[-1]))
        an = np.arange(len(b))
else:
    for i in range(len(a)):
        c.append(math.log(b[i]) - math.log(a[-1]))
        an = np.arange(0, len(a))


plt.plot(an, c)
plt.ylabel('$log(R_n - R_\infty)$')
plt.xlabel('n')
plt.savefig('q2_4.png')
