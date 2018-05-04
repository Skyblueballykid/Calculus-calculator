def f(x):
    return x**2

def derivative(x):
    h = 1./1000.
    rise = f(x+h) - f(x)
    run = h
    slope = rise/run
    return slope