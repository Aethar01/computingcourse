from numpy import linspace
from q3_1 import ea, gmin, dn, theory, discrep
from scipy.optimize import curve_fit


x = linspace(start=ea[0], stop=ea[-1], \
        num=len(theory(ea, gmin(discrep, \
        80, 120, tol=3.0e-8)[0])))
popt, pcov = curve_fit(theory, x, \
        theory(ea, gmin(discrep, \
        80, 120, tol=3.0e-8)[0]), \
        sigma=dn, absolute_sigma=True)
print(popt)
print(pcov)
