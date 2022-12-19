import sys


def exponent_2(Max):
    print("[", end="")
    res = 0
    for i in range(0, Max):
        res = 2**i
        if (res < Max):
            print(str(res), end=", ")
        else:
            print("]")
            break
    return res


while (True):
    N_str = input("Введите число N ")
    try:
        N = int(N_str)
        if (0 <= N <= sys.maxsize):
            break
        else:
            raise
    except:
        print("Неккоректный ввод числа")
exponent_2(N)
