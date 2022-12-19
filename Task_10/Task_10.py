import sys
import random
number_array = []
i = 0
while (True):
    number_str = input("Введите количество монет ")
    try:
        number = int(number_str)
        # просто для небольшого ограничения. теоритечески число ограничено лишь памятью
        if (1 <= number <= sys.maxsize):
            while i < number:
                number_array.append(random.randint(0, 1))
                i += 1
            break
    except:
        print("Неккоректный ввод числа")
print(number_array)
Check_summ = (sum((int(number_array[i])
              for i in range(0, int(len(number_array))))))
if (Check_summ > number//2):
    print("необходимо перевернуть " + str(number-Check_summ) + " монет")
else:
    print("необходимо перевернуть " + str(Check_summ) + " монет")
