from numpy import linspace, arange
from numpy import sum as npsm
from numpy.random import normal
from scipy.optimize import curve_fit
from numpy import array
import matplotlib.pyplot as plt
from minimise import gmin
from statistics import stdev


def discrepancy(r, dn):
    '''where r is the residuals,
    and dn is the error on the residuals'''
    return npsm([(r[i] / dn[i]) ** 2 for i in range(len(r))])


def theory(e: float, w: float):
    th = [(1.4767e7 / (w ** 2 / 4 + (i - 1232) ** 2)) for i in e]
    return th


def parse_data(file: str):
    ea = []
    na = []
    dn = []
    with open(file, 'r') as f:
        for line in f:
            estr, nstr, errstr = line.split()
            ea.append(float(estr))
            na.append(float(nstr))
            dn.append(float(errstr))
        ea = array(ea)
        na = array(na)
        dn = array(dn)
    return [ea, na, dn]


def minimum_discrepancy(ea: list, na: list, dn: list):
    r = []
    minimum = []
    ranger = arange(80, 120, 0.01)

    for i in ranger:
        w = i
        r = [(na - theory(ea, w))]
        minimum.append(discrepancy(r, dn))

    mindiscrep = min(minimum)
    w = ranger[minimum.index(min(minimum))]
    return (w, mindiscrep)


def one():
    ea, na, dn = parse_data('./data1.txt')

    def discrep(w: float):
        r = [(na - theory(ea, w))]
        return discrepancy(r, dn)

    # print('minimum discrepancy and w: ' + f'{minimum_discrepancy(ea, na, dn)}')
    # print('gmin discrepancy and w: ' + f'{gmin(discrep, 80, 120, tol=3.0e-8)}')
    w = 111.8916236

    plt.title('Plot of n(E) with error')
    plt.plot(ea, na)
    plt.errorbar(ea, na, dn)
    plt.xlabel('E')
    plt.ylabel('n(E)')
    plt.savefig('2_1.png', dpi=300)

    plt.title('Plot of n(E) with error and theoretical curve using w = ' + f'{w}')
    plt.plot(ea, theory(ea, w))
    plt.savefig('2_3th.png', dpi=300)
    plt.clf()


def one_theory():
    ea, na, dn = parse_data('./data1.txt')

    def discrep(w):
        r = [(na - theory(ea, w))]
        return discrepancy(r, dn)

    plt.title('Theoretical calculation of n(E) with w from gmin(discrep, ...)')
    plt.plot(ea, na)
    plt.errorbar(ea, na, dn)
    plt.xlabel('E')
    plt.ylabel('n(E)')
    plt.plot(ea, theory(ea, gmin(discrep, 80, 120, tol=3.0e-8)[0]))
    plt.savefig('2_5.png', dpi=300)

    x = linspace(start=ea[0], stop=ea[-1], num=len(theory(ea, gmin(discrep, 80, 120, tol=3.0e-8)[0])))
    popt, pcov = curve_fit(theory, x, theory(ea, gmin(discrep, 80, 120, tol=3.0e-8)[0]), sigma=dn, absolute_sigma=True)
    # print('Theory: curve fit w: ' + f'{popt}' + ' +- ' + f'{pcov}')
    plt.clf()


def six():

    def random_sample(na, dn) -> float:
        return normal(na, dn)

    def student(ea: list, na: list, dn: list) -> float:
        m = []
        for j, k in zip(na, dn):
            m.append(random_sample(j, k))
        popt, pcov = curve_fit(theory, ea, m)
        return float(popt[0])

    def all_students(ea: list, na: list, dn: list, students: int) -> list:
        w = []
        for i in range(students):
            w.append(student(ea, na, dn))
        sigma = stdev(w)
        return (sum(w) / students, sigma, w)

    students: float = 1000
    ea, na, dn = parse_data('./data1.txt')
    w, sigma, wlist = all_students(ea, na, dn, students)
    # print('q6: w: ' + f'{w}' + ' +- ' + f'{sigma}')
    plt.xlabel('w')
    plt.ylabel('count')
    plt.title('Histogram of w ensemble values for 1000 students')
    plt.hist(wlist, bins=20)
    plt.savefig('2_7.png', dpi=300)
    plt.clf()

    standard_error = sigma / (students ** 0.5)
    # print(standard_error)


if __name__ == "__main__":
    one()
    one_theory()
    six()
