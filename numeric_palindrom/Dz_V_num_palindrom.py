#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""


def is_palindrom(n: int) -> bool:
    if n <= 0:
        raise ValueError("Number must be a positive integer")

    pass




def rev(b):
    num = 0
    while b > 0:
        num = num * 10 + b % 10
        b = b // 10
    return num


def num_pal(b: int) -> bool:
    if b == rev(b):
        return True
    else:
        return False

print(num_pal(50505))
