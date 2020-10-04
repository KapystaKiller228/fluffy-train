import sympy, scipy.integrate, numpy

x = sympy.symbols('x')

def integer():
    return sympy.integrate(sympy.cos(x) - x ** 3, x)

def integer_for_scipy():
    return lambda x: numpy.cos(x)-x**3

def definite_integer(beginning, end):
    return sympy.integrate(sympy.cos(x) - x ** 3, (x, beginning, end))

def definite_integer_scipy(beginning, end):
    return scipy.integrate.quad(integer_for_scipy(), beginning,end)

print('This program solves integrals\nFunction ')
beginning=float(input('Enter beginning of integer: '))
end=float(input('Enter end of integer: '))
print('Integer(int_a^b f(x)dx)= ', integer(), '\nDefinite integer by sympy=', definite_integer(beginning, end),'\nDefinite integer by scipy:', definite_integer_scipy(beginning, end))
#почему через scipy и numpy вафельные нужно численно решать если через sympy намного легче и не нужно по 99999 документациям рыться?