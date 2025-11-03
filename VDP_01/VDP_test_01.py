#x=input("Введите число: ")
#if x % 2 == 0:
#    print("Even number")
#else:
#    print("Odd number")

#x=input("Введите число: ")
#if x % 7 == 0:
#    print("Number is multiple 7")
#else:
#    print("Number is not multiple 7")




#x=input("Введите число 1: ")
#y=input("Введите число 2: ")
#if x>y:
#    print("Максимальное число: ", x)
#elif x==y:
#    print("Числа равны")
#else:
#    print("Максимальное число: ", y)

#x=input("Введите число 1: ")
#y=input("Введите число 2: ")
#if x>y:
#    print("Минимальное число: ", y)
#elif x==y:
#    print("Числа равны")
#else:
#    print("Минимальное число: ", x)

x=input("Введите число 1: ")
y=input("Введите число 2: ")
action=input(
    "Ведите 1 если нужно сложить.\n"
    "Ведите 2 если нужно вычесть.\n"
    "Ведите 3 если нужно среднеарифметичекое.\n"
    "Ведите 4 если нужно произведение.\n"
    ":   ")
if action == 1:
    print("Сумма чисел:  ", x+y)
elif action == 2:
    print("Разность чисел:  ", x-y)
elif action == 3:
    print("Среднераифметическое чисел:  ", (x+y)/2)
elif action == 4:
    print("Произведение чисел:   ", x*y)
else:
    print("Номер действия введен неверно")