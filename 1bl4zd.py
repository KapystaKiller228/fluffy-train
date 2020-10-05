import math, sympy

def f(x):
    return sympy.cos(x)-x**3

def derivative():
    x = sympy.symbols('x')
    return sympy.diff(sympy.cos(x) - x ** 3, x)

def newton(accuracy, x0):
    eps=10**(accuracy*-1)
    n=1
    while abs((x0-(f(x0)/derivative()))-x0) > eps:
        x0=x0-(f(x0)/derivative())
        print('x%s = %s' %(n,x0))
        n=n+1
    return x0

print('This programm solves function by Newton method')
print('Function cos(x)-x^3=0 if x =', newton(int(input('Enter accuracy(decimal place): ')), int(input('Enter x0: '))))
#0.865 474 033 102
#поганые буржуи победили все таки и теперь задачи пишутся для них((((
#Matplotlib нужон для графика
