from numpy import linspace
from numpy import arange
from scipy.optimize import curve_fit
from numpy import array
import matplotlib.pyplot as plt
from q3_4 import discrepancy
from minimise import gmin


def theory(e, w):
    th = [(1.4767e7 / (w ** 2 / 4 + (i - 1232) ** 2)) for i in e]
    return th


def discrep(w):
    r = [(na - theory(ea, w))]
    return discrepancy(r, dn)


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


w = 111.8916236


# plt.figure(figsize=(3, 3))
plt.plot(ea, na)
plt.errorbar(ea, na, dn)
plt.xlabel('E')
plt.ylabel('n(E)')
plt.savefig('2_1.png', dpi=300)


plt.plot(ea, theory(ea, w))
plt.savefig('2_3th.png', dpi=300)
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

# w = 112.7052
# r = [(na - theory(ea, w))]
# print(discrepancy(r, dn))


# def f(x):
#     return exp(x) + 1 / x
#
#
# print(gmin(f, 0, 50, tol=3.0e-8))


print(gmin(discrep, 80, 120, tol=3.0e-8))

plt.clf()

plt.plot(ea, na)
plt.errorbar(ea, na, dn)
plt.xlabel('E')
plt.ylabel('n(E)')
plt.plot(ea, theory(ea, gmin(discrep, 80, 120, tol=3.0e-8)[0]))
plt.savefig('q3_7.png', dpi=300)

x = linspace(start=ea[0], stop=ea[-1], num=len(theory(ea, gmin(discrep, 80, 120, tol=3.0e-8)[0])))
popt, pcov = curve_fit(theory, x, theory(ea, gmin(discrep, 80, 120, tol=3.0e-8)[0]), sigma=dn, absolute_sigma=True)
print(popt)
print(pcov)
