from math import sqrt, fabs


def gmin(f,a,c,tol=3.0e-8):
    """Golden section minimisation.

    Find minimum of f(x) known to have a single minimum
    between a and c, using golden section search. Returns
    minimum position, xmin, and minimum value, f(xmin).
    Suggest set tol to 1.0e-4 for single precision, 3.0e-8
    for double precision."""
    if (c<=a):
        raise ValueError('gmin(f,a,c) requires c>a')
    w=(3.0-sqrt(5.0))/2.0 # golden ratio
    b=a+w*(c-a) # set initial abscissas in interval
    bp=c-w*(c-a)
    while(fabs(c-a)>tol*(c+a)/2.0): # loop to refine
        if(f(b)<f(bp)):            # bracketing of minimum
            c=bp
            bp=b
            b=a+w*(c-a)
        else:
            a=b
            b=bp
            bp=c-w*(c-a)
    # finished looping, return best answer
    fb=f(b)
    fbp=f(bp)
    if (fb<fbp): return b, fb
    else: return bp, fbp
