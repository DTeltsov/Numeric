import math

#функция
def F(x):
    return pow(x,3) - 10 * pow(x,2) + 44 * x + 29

#производная функции
def F1(x):
    return 3 * pow(x,2) - 20 * x + 44

#вторая производная функции
def F2(x):
    return 6 * x - 20

#функция для метода простой итерации
def G(x):
    return x - 0.0149 * (pow(x,3) - 10 * pow(x,2) + 44 * x + 29)



#Метод Ньютона
def MethodN(a,b):
    print('Метод Ньютона:\n')
    try:
        l = []
        if F(a)*F2(a) > 0:
            xn = a
        elif F(b)*F2(b) > 0:
            xn = b
        xn1=xn-(F(xn)/F1(xn)) 
        while math.fabs(F(xn)) > math.pow(10,-4) * 44:
            print(xn)
            l.append(math.fabs(xn))
            xn=xn1
            xn1=xn-(F(xn)/F1(xn))
        print(xn)
        l.append(math.fabs(xn))
        print('\nОтвет: {0}\n\nАпостериорная оценка: {1}\n\nАприорная оценка: {2}'.format(round(min(l), 4), len(l), ApriorN(xn)))
    except ValueError:
        print("Value not invalidate")

#Метод простой итерации
def MethodI(a,b):
    print('\nМетод простых итераций:\n')
    try:
        l = []
        xn = a 
        xn1 = G(xn)
        while math.fabs(xn1 - xn) > math.pow(10,-4):
            print(xn)
            l.append(math.fabs(xn))
            xn=xn1
            xn1=G(xn) 
        print(xn)
        l.append(math.fabs(xn))
        print('\nОтвет: {0}\n\nАпостериорная оценка: {1}\n\nАприорная оценка: {2}'.format(round(min(l), 4), len(l), ApriorI()))
    except ValueError:
        print("Value not invalidate")



def ApriorI():
    q = 0.3444
    x0 = -1
    eps = math.pow(10,-4)
    a = math.fabs(G(x0) - (x0))
    b = (1 - q) * eps
    c = math.log(a / b)
    d = math.log(1 / q)
    res = int(c / d) + 1
    return res 



def ApriorN(x):
    q = 0.3444
    x0 = -1
    eps = math.pow(10,-4)
    a = math.fabs(x0 - x)
    b = math.log(a / eps)
    c = math.log(1 / q)
    d = math.log2(b / c + 1)
    res = int(d) + 1
    return res

  

def main():
    MethodN(-1,0)
    MethodI(-1,0)
    
    

if __name__ == "__main__":
    main()