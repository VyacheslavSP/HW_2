# y^2-Sy+P=0; x=P//y
import math
a = 1
while (True):
    try:
        b = (float(input("Сумма чисел = ")))*-1
        c = float(input("Произведение чисел = "))
        if (b > 0 or b > 2000 or c < 0 or c > 1000000):
            raise
        else:
            break
    except:
        print("Неккоректный ввод числа")

discr = b ** 2 - 4 * a * c
try:
    if discr > 0:
        y1 = (-b + math.sqrt(discr)) / (2 * a)
        y2 = (-b - math.sqrt(discr)) / (2 * a)
        if (int(y1) != y1 or int(y2 != y2)):  # проверка на натуральность полученного результата
            raise
        else:
            print("Число 1 = "+str(y1))
            print("Число 2 = "+str(y2))
    elif discr == 0:
        y = -b / (2 * a)
        if (int(y) != y):
            raise
        else:
            print("Число 1 = %.1f" % y)
            print("Число 2= "+str(c//y))
    else:
        print("Неккорекные данные")
except:
    print("числа не натуральные")
