#!/usr/bin/env python

"""
Напишите программу, которая кодирует и декодирует текст шифром Атбаш.
В этом шифре каждая i-ая буква алфавита заменяется i-ой буквой с его конца, например, для латинского алфавита: a - z, b - y и т.д.

- заглавные буквы переводятся в строчные
- пробельные символы и знаки препинания опускаются
- шифр идёт блоками по 5 символов, между ними пробел

Пример:

`Bambarbia, Kirgudu` -> `yznyz iyrzp ritfw f`
"""

BLOCK_SIZE = 5


def atbash_encode(text: str) -> str:
    pass


def atbash_decode(cipher: str) -> str:
    pass

import string

def atbash_code(j: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    y = j.lower().replace(' ','').translate(str.maketrans(' ', ' ', string.punctuation + '—'))

    return y.translate(str.maketrans(alphabet + alphabet.upper(), alphabet[::-1] + alphabet.upper()[::-1]))
def len_5(b: str):

    for i in range(0, len(b), 5):
        print(b[i: i + 5], end=' ')
        
 print(len_5(atbash_code("Bambarbia, Kirgudu")))
