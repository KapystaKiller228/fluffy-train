#print(math.pi) лан это шутка

import decimal  #это вот чтобы флоат нормально работал
def door(знак):
    decimal.getcontext().prec= знак
    if знак==1: return 3
    else: return sum((decimal.Decimal(1/16**i))*(decimal.Decimal(4/(8*i+1))-decimal.Decimal(2/(8*i+4))-decimal.Decimal(1/(8*i+5))-decimal.Decimal(1/(8*i+6))) for i in range(знак+1))

print("Число пи= ", door(int(input("Знак после запятой: "))))

#Формула Бэйли — Боруэйна — Плаффа