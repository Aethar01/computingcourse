from numpy import sum as sm


def discrepancy(r, dn):
    '''where r is the residuals,
    dn is the error and e is the input list'''
    return sm([(r[i] / dn[i]) ** 2 for i in range(len(r))])
