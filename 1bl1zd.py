def reshenie(a, b, c):
    if a != 0:
        d = b ** 2 - 4 * a * c
        if d==0: return(((-b)/(2*a)))
        else: return (((-b+d**.5)/(2*a)),((-b-d**.5)/(2*a)))
    elif b==0:
        if c==0: return('любое число')
        else: return('нет решения')
    else: return(-c/b)

print('решение квадратного уравнения вида\nax^2+bx+c=0\nвведите целочисленные коэффициенты a b c через пробел: ')
a,b,c=map(int, input().split())
print('Решение: ',reshenie(a,b,c))
#работает для комплексных корней тоже
#3230 128 4768- тайник егора