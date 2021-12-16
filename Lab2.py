import math
import numpy as np
from numpy import linalg



def condition_method_Zeydelya(x):
    minor_1 = x[0][0]
    minor_2 = linalg.det(np.array([ [x[0][0], x[0][1]],
                                    [x[1][0], x[1][1]]]))

    minor_3 = linalg.det(np.array([ [x[0][0], x[0][1], x[0][2]],
                                    [x[1][0], x[1][1], x[1][2]],
                                    [x[2][0], x[2][1], x[2][2]]]))

    if minor_1 < 0 or minor_2 < 0 or minor_3 < 0:
        return 1
    else:
        return 0



def condition_method_Progonky(a, b, c):
    for i in range(len(c)):
        if abs(c[i]) < ( abs(a[i]) + abs(b[i])):
            return 1
    return 0
     


def method_Progonky(a, b, c, y):
    if condition_method_Progonky(a, b, c) == 0:
        Sum = 1
        alpha = -b[0]/c[0]
        beta = y[0]/c[0]
        beta_arr = []
        alpha_arr = []
        for i in range(len(c)):
            if i == 0:
                z = c[i]
            else:
                z = c[i] + alpha * a[i]
                alpha = -b[i] / z
                beta = (y[i] - a[i] * beta) / z
            Sum *= z
            beta_arr.append(beta)
            alpha_arr.append(alpha)
        print('detA = {}'.format(Sum))
        alpha_arr.reverse()
        beta_arr.reverse()
        for i in range(len(c)):
            if i == 0:
                x = round(beta_arr[i])
            else:
                x = round(alpha_arr[i] * x + beta_arr[i])
            print('x = {}'.format(x))
    else:
        print('Не выполнены условия стойкости')


            

def method_Zeydelya(A, f):
    if condition_method_Zeydelya(A) == 0:
        m = len(A)
        x = [.0 for i in range(m)]
        Iteration = 0
        converge = False
        pogr = 0.
        while not converge:
            x_new = np.copy(x)
            for i in range(m):
                s1 = sum(A[i][j] * x_new[j] for j in range(i))
                s2 = sum(A[i][j] * x[j] for j in range(i + 1, m))
                x_new[i] = (f[i] - s1 - s2) / A[i][i]
            pogr = sum(abs(x_new[i] - x[i])  for i in range(m))
            converge =  pogr < 1e-4
            Iteration += 1
            x = x_new
        print('Количество итераций :', Iteration)
        print('Решение системы уравнений :', np.round(x))
        print('Погрешность :', pogr)
    else:
        print('Не выполнены условия стойкости')


def cond(m):
    norm_m = round(np.linalg.norm(m))
    norm_inv_m = round(np.linalg.norm(np.linalg.inv(m)))
    print(norm_m * norm_inv_m)



def main():
    m = np.array(  [[1,-1,0],
                    [1,-2,-1],
                    [0,1,2]])
    f = np.array([-4,-2, 0])
    c = np.diagonal(m)
    a = np.diagonal(m, offset = -1)
    a = np.insert(a, 0, 0)
    b = np.diagonal(m, offset = 1)
    b = np.insert(b, 2, 0)
    print('\nМетод Прогонки:\n')
    method_Progonky(a, b, c, f)
    print('\nМетод Зейделя:\n')
    method_Zeydelya(m, f)
    print('\nЧисло обусловленности:')
    cond(m)


if __name__ == '__main__':
    main()