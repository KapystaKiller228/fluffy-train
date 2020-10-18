import math, matplotlib.pyplot

def f(x):
    return math.cos(x)-x**3

def newton(accuracy, x0):
    eps=10**(accuracy*-1)
    n=1
    array_x=[]
    array_y=[]
    while abs((x0-(f(x0)/((f(x0+0.1)-(f(x0)))/0.1)))-x0) > eps:
        array_x.append(x0)
        array_y.append(f(x0))
        x0=x0-(f(x0)/((f(x0+0.1)-(f(x0)))/0.1))
        print('x%s = %s' %(n,x0))
        n=n+1
        matplotlib.pyplot.plot(array_x,array_y)
    matplotlib.pyplot.show()
    return x0

print('This programm solves function by Newton method')
print('Function cos(x)-x^3=0 if x =', newton(int(input('Enter accuracy(decimal place): ')), float(input('Enter x0: '))))
#0.865 474 033 102
#поганые буржуи победили все таки и теперь задачи пишутся для них((((
