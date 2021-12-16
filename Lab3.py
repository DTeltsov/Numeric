import numpy as np
from numpy import linalg



def condition_check(x):
    minor_1 = x[0][0]
    minor_2 = linalg.det(np.array([ [x[0][0], x[0][1]],
                                    [x[1][0], x[1][1]]]))

    minor_3 = linalg.det(np.array([ [x[0][0], x[0][1], x[0][2]],
                                    [x[1][0], x[1][1], x[1][2]],
                                    [x[2][0], x[2][1], x[2][2]]]))
    minor_4 = linalg.det(x)

    if minor_1 < 0 or minor_2 < 0 or minor_3 < 0 or minor_4 < 0:
        return 1
    elif np.allclose(x, x.T) == 1:
        return 1
    else:
        return 0


#Метод скалярных произведений
def max_l(m, y):
    eps = 0.001
    x = np.dot(m,y)
    l =  np.dot(x,y)/np.dot(y,y)
    while True:
        e = x/np.linalg.norm(x)
        x = np.dot(m,e)
        l_n = np.dot(x,e)/np.dot(e,e) 
        if(abs(l_n - l) <= eps):
            result = l_n
            break
        else:
            l = l_n
    return result


def  min_l(m, l, x):
    if condition_check(m) == 0:
        b = l * np.eye(4) - m
        b_l = max_l(b, x)
        result = l - b_l
        return result


def main():
    m = np.array(  [[1,-1,0],
                    [1,-2,-3],
                    [1,0,2]])
    x = np.array([-4,-2, 0])
    l_max = max_l(m, x)
    l_min = min_l(m, l_max, x)
    print('\nМаксимальное собственное значение: {0}\n\nМинимальное собственное значение: {1}'.format(l_max, l_min))


if __name__ == '__main__':
    main()