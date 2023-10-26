from numpy import linspace
from numpy import arange
from scipy.optimize import curve_fit
from numpy import array
import matplotlib.pyplot as plt
from minimise import gmin
four = __import__('2_4')


def theory(e, w):
    th = [(1.4767e7 / (w ** 2 / 4 + (i - 1232) ** 2)) for i in e]
    return th


def parse_data(file: str):
    f = open(file, 'r')
    ea = []
    na = []
    dn = []
    for line in f:
        estr, nstr, errstr = line.split()
        ea.append(float(estr))
        na.append(float(nstr))
        dn.append(float(errstr))
    ea = array(ea)
    na = array(na)
    dn = array(dn)
    f.close()
    return [ea, na, dn]


def one():
    ea, na, dn = parse_data('./data1.txt')

    def discrep(w):
        r = [(na - theory(ea, w))]
        return four.discrepancy(r, dn)

    print(gmin(discrep, 80, 120, tol=3.0e-8))
    w = 111.8916236

    # plt.figure(figsize=(3, 3))
    plt.plot(ea, na)
    plt.errorbar(ea, na, dn)
    plt.xlabel('E')
    plt.ylabel('n(E)')
    plt.savefig('2_1.png', dpi=300)

    plt.plot(ea, theory(ea, w))
    plt.savefig('2_3th.png', dpi=300)


def minimum_discrepancy(ea, na, dn):
    r = []
    minimum = []
    ranger = arange(80, 120, 0.01)

    for i in ranger:
        w = i
        r = [(na - theory(ea, w))]
        minimum.append(four.discrepancy(r, dn))

    mindiscrep = min(minimum)
    w = ranger[minimum.index(min(minimum))]
    print('minimum discrepancy =', mindiscrep)
    print('which is when w =', w)
    return (mindiscrep, w)


def one_theory(ea, na, dn):
    ea, na, dn = parse_data('./data1.txt')

    def discrep(w):
        r = [(na - theory(ea, w))]
        return four.discrepancy(r, dn)

    plt.plot(ea, na)
    plt.errorbar(ea, na, dn)
    plt.xlabel('E')
    plt.ylabel('n(E)')
    plt.plot(ea, theory(ea, gmin(discrep, 80, 120, tol=3.0e-8)[0]))
    plt.savefig('2_5.png', dpi=300)

    x = linspace(start=ea[0], stop=ea[-1], num=len(theory(ea, gmin(discrep, 80, 120, tol=3.0e-8)[0])))
    popt, pcov = curve_fit(theory, x, theory(ea, gmin(discrep, 80, 120, tol=3.0e-8)[0]), sigma=dn, absolute_sigma=True)
    print(popt)
    print(pcov)


if __name__ == "__main__":
    one()
    one_theory()
