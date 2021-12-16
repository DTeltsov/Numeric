import math
import numpy as np
from sympy import Symbol
from sympy.solvers import solve
from sympy import Interval



def f(x):
    return pow(x,4) + pow(x,3) - 6 * pow(x,2) + 20 * x - 16 * math.cos(x)


def vyz(a,b):
    h = (b-a)/9
    x = []
    fx = []
    k = 0
    while True:
        x.append(round(a, 2))
        a = x[k] + h
        fx.append(round(f(x[k]), 2))
        k = k + 1
        if k == 10:
            return x, fx


def lagranz(x,y):
        t = Symbol('x')
        z=0
        for j in range(len(y)):
            p1=1; p2=1
            for i in range(len(x)):
                if i==j:
                    p1=p1*1; p2=p2*1   
                else: 
                    p1=p1*(t-x[i])
                    p2=p2*(x[j]-x[i])
            z=z+y[j]*p1/p2
        return z


def polCheb(a, b):
    x = []
    fx = []
    k=0
    while True:
        x.append(round((a + b)/2 + ((b - a)/2) * math.cos((((2 * k + 1) * math.pi)/20)), 2))
        fx.append(round(f(x[k]), 2))
        k = k + 1
        if k == 10:
            return x, fx


def solvepol(p):
    x = Symbol('x')
    xk = solve(p, x)
    for i in range(len(xk)):
        g = Interval(-4, 1).contains(xk[i])
        if g == True and xk[i] < 0:
            print(xk[i])


def main():
    #x,y = polCheb(-4, 1)
    x = np.array([-1, 1, 2, 3, 4, 5], dtype=float)
    y = np.array([-4, -2, 5, 16, 31, 50], dtype=float)
    p = lagranz(x, y).simplify()
    print(p)
    '''
    x,y = vyz(-4, 1)
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    d = lagranz(x, y).simplify()
    print('\nПолином по узлам Чебышева: \n\n' + str(p) + '\n\nНаибольший отрицательный корень:')
    solvepol(p)
    print('\n\nПолином по равноудалённым узлам: \n\n' + str(d) + '\n\nНаибольший отрицательный корень:')
    solvepol(d)
    '''


if __name__ == '__main__':
    main()