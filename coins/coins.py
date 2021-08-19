#!/usr/bin/env python

# Бабушка Зина даёт своему любимому внуку Васе 3 монеты и разрешает оставить 2 из них.
# Найдите максимальную сумму из любых двух монет.
# Номинальная стоимость монет: a, b и с тугриков.

a = int(input('Moneta 1: '))
b = int(input('Moneta 2: '))
c = int(input('Moneta 3: '))
if (a + b) > (a + c) and (a + b) > (b + c):
    print(a + b)
elif (a + c) > (b + c):
    print(a + c)
else:
    print(b + c)
