#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
from multiprocessing import Process
from time import sleep


def control_x(x):
    return -1*x


def control_y(x):
    return x


def func1(x):
    y = math.cos(x)
    EPS = 1e-07
    a = 1
    S, n = 0.0, 0
    while math.fabs(a) > EPS:
        S += ((-1)**n*x**(2*n))/(math.factorial(2*n))
        a = S - y 
        n += 1
        print(f"Функция 1 - S={S}")
        sleep(0.2)
    return S
    

def func2(x):
    y = math.log(x+1)
    EPS = 1e-07
    a = 1
    S, n = 0.0, 1
    while math.fabs(a) > EPS:
        S += ((-1)**(n-1)*x**n)/n
        a = S - y
        n += 1
        print(f"Функция 2 - S={S}")
        sleep(0.2)
    return S


def compare(first, second, x):
    result = first(x) - second(x)
    print(f"Результат сравнения {result}")


if __name__ == "__main__":
    proc1 = Process(target=compare(func1, control_x, 0.3))
    proc2 = Process(target=compare(func2, control_y, 0.4))
    proc1.start()
    proc2.start()
