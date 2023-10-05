from numpy import cos, fabs


def g(x):
    n = 1
    total = term = cos(x)  # First term
    while fabs(term) > (1.0e-7 * fabs(total) + 1.0e-13):
        n += 2  # Advance to next term
        term = cos(n * x) / (n * n)
        total += term  # Add term to total
    return total
