#! /usr/bin/env python3

""" mymodule.py - an example of Python module """

__counter = 0


def suml(list):
    global __counter
    __counter += 1
    sum = 0
    for el in list:
        sum += el
    return sum


def prodl(list):
    global __counter
    __counter += 1
    prod = 1
    for el in list:
        prod *= el
    return prod


if __name__ == '__main__':
    print('Contexto do modulo')
    l = [i + 1 for i in range(5)]
    print(suml(l) == 15)
    print(prodl(l) == 120)
else:
    print('Fora do contexto do modulo')
