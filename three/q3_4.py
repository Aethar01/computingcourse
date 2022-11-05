from numpy import sum as sm


def discrepancy(r, dn):
    '''where r is the residuals,
    and dn is the error on the residuals'''
    return sm([(r[i] / dn[i]) ** 2 for i in range(len(r))])
