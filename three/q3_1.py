from numpy import arange
from numpy import array
import matplotlib.pyplot as plt
from q3_4 import discrepancy
from minimise import gmin
from numpy import exp

f = open('data1.txt', 'r')
ea = []
na = []
dn = []

for line in f:
    estr, nstr, errstr = line.split()
    ea.append(float(estr))
    na.append(float(nstr))
    dn.append(float(errstr))
f.close()
ea = array(ea)
na = array(na)
dn = array(dn)


def theory(e, w):
    th = [(1.4767e7 / (w ** 2 / 4 + (i - 1232) ** 2)) for i in e]
    return th


w = 111.8916236

plt.plot(ea, na)
plt.errorbar(ea, na, dn)
plt.xlabel('E')
plt.ylabel('n(E)')
plt.savefig('q3_1.png')


plt.plot(ea, theory(ea, w))
plt.savefig('q3_1th.png')
global r
global minimum
ranger = arange(80, 120, 0.01)
minimum = []
for i in ranger:
    w = i
    r = [(na - theory(ea, w))]
    minimum.append(discrepancy(r, dn))

print('minimum discrepancy =', min(minimum))
print('which is when w =', ranger[minimum.index(min(minimum))])

w = 112.7052
r = [(na - theory(ea, w))]
print(discrepancy(r, dn))


def f(x):
    return exp(x) + 1 / x


print(gmin(f, 0, 5))



