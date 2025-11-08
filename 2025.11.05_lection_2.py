# ЧАСТЬ1

# Задание 1

# x=int(input("Введи число 1:  "))
# y=int(input("Введи число 2:  "))
#
# for i in range(x, y+1, 1):
#     print(i, end=', ')

#  Задание 2

# x=int(input("Введи число 1:  "))
# y=int(input("Введи число 2:  "))
#
# for i in range(x, y+1, 1):
#     if i%2 == 0:
#         continue
#     print(i, end=', ')

#  Задание 3

# x=int(input("Введи число 1:  "))
# y=int(input("Введи число 2:  "))
#
# for i in range(x, y+1, 1):
#     if i%2 != 0:
#         continue
#     print(i, end=', ')

#  Задание 4

# x=int(input("Введи число 1:  "))
# y=int(input("Введи число 2:  "))
# if x>y:
#     max=x
#     min=y
# else:
#     max=y
#     min=x
#
#
# while max != min-1:
#     print (max, end=', ')
#     max=max-1

#  Задание 5

# x=int(input("Введи число 1:  "))
# y=int(input("Введи число 2:  "))
#
# if x>y:
#     max=x
#     min=y
# else:
#     max=y
#     min=x
#
# for i in range(min, max+1):
#     if i%2 == 0:
#         continue
#     print(i, end=', ')


# ЧАСТЬ 2
# Задание 1

# x=int(input("Введи число 1:  "))
# y=int(input("Введи число 2:  "))
#
# if x>y:
#     max=x
#     min=y
# else:
#     max=y
#     min=x
#
# summa=0
# delit=0
# for i in range(min, max+1):
#     print (i, end=', ')
#     summa = summa + i
#     delit = delit + 1
# print("cумма =", summa)
# print("Среднее арифметическое: ", summa/delit)

# Задание 2

# x=int(input("Введи число 1:  "))
# n=1
# for i in range (1, x+1):
#     n=n*i
# print("Факториал = ", n)

# Задание 3

# x=int(input("Введи длинну линии:  "))
# n=1
# for i in range (1, x+1):
#     print("*",end='')

# Задание 4

#x=int(input("Введи длинну линии:  "))
#y=input("Введи символ :  ")
#n=1
#for i in range (1, x+1):
#    print(y,end='')

# ЧАСТЬ 3
# Задание 1

# x=int(input("Введи число:  "))
# for i in range (1, 10+1):
#     print(x,"*",i,"=", x*i )

# Задание 2

# x=int(input("Введи сумму для конвертирования :  "))
# currency1=input("Введи\n S если доллар\n E если евро\n C если юань\n R если рубль\n :  ")
# currency2=input("Введи в какую валюту конвертировать\n S если доллар\n E если евро\n C если юань\n R если рубль\n :  ")
# 
# if currency2 in ['S', 's'] and currency1 in ['S', 's']:
#      print(x, currency1,"=", x*1, currency2)
# elif currency2 in ['S', 's'] and currency1 in ['E', 'e']:
#     print(x, currency1,"=", x*0.8664, currency2)
# elif currency2 in ['S', 's'] and currency1 in ['C', 'c']:
#     print(x, currency1,"=", x*7.12, currency2)
# elif currency2 in ['S', 's'] and currency1 in ['R', 'r']:
#     print(x, currency1,"=", x * 81.38, currency2)
# elif currency2 in ['E', 'e'] and currency1 in ['E', 'e']:
#     print(x, currency1,"=", x * 1, currency2)
# elif currency2 in ['E', 'e'] and currency1 in ['S', 's']:
#     print(x, currency1, x * 1.15, currency2)
# elif currency2 in ['E', 'e'] and currency1 in ['C', 'c']:
#     print(x, currency1,"=", x * 8.21, currency2)
# elif currency2 in ['E', 'e'] and currency1 in ['R', 'r']:
#     print(x, currency1,"=", x * 93.76, currency2)
# elif currency2 in ['C', 'c'] and currency1 in ['C', 'c']:
#     print(x, currency1,"=", x * 1, currency2)
# elif currency2 in ['C', 'c'] and currency1 in ['S', 's']:
#     print(x, currency1,"=", x * 0.1405, currency2)
# elif currency2 in ['C', 'c'] and currency1 in ['E', 'e']:
#     print(x, currency1,"=", x * 0.1218, currency2)
# elif currency2 in ['C', 'c'] and currency1 in ['R', 'r']:
#     print(x, currency1,"=", x * 11.37, currency2)
# elif currency2 in ['R', 'r'] and currency1 in ['R', 'r']:
#     print(x, currency1,"=", x * 1, currency2)
# elif currency2 in ['R', 'r'] and currency1 in ['S', 's']:
#     print(x, currency1,"=", x * 0.012289, currency2)
# elif currency2 in ['R', 'r'] and currency1 in ['E', 'e']:
#     print(x, currency1,"=", x * 0.010665, currency2)
# elif currency2 in ['R', 'r'] and currency1 in ['C', 'c']:
#     print(x, currency1,"=", x * 0.087971, currency2)
# else:
#      print("Ввод неверный")


# Задание 3

# border1=int(input("Введи границу 1:  "))
# border2=int(input("Введи границу 2:  "))
#
# while True:
#     x = int(input("Введите число: "))
#     if border1 <= x <= border2:
#         for i in range(border1, border2 + 1):
#             if i==x:
#                 print('!',i,'! ', end='')
#             else:
#                 print(i," ", end='')
#         break
#     else:
#         print("Введите корректное значение.")


# Задание 4

from random import *

number = randint(1, 500)
print("Угадай число от 1 до 500 (",number,")\nНадоест - нажми 0")

counter=0
while True:
    counter=counter+1
    value = int(input("Введи число: "))
    if value == 0:
        print("Надоело...")
        break
    else:
        if value > number:
            print("Число меньше")
        elif value < number:
            print("Число больше")
        else:
            print("Угадал! ", value)
            print("Количество попыток - ", counter)
            break
