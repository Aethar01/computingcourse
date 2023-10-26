from numpy import sum as npsm


def discrepancy(r, dn):
    '''where r is the residuals,
    and dn is the error on the residuals'''
    return npsm([(r[i] / dn[i]) ** 2 for i in range(len(r))])
