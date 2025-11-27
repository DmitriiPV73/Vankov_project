# Задание 1

# import re
# action =input("введи выражение типа 23 + 12:  ")
# def function():
#
#     val=re.split(r"[+*/-]",action)
#     sign=re.findall(r"[+*/-]",action)
#     x=int(val[0])
#     y=int(val[1])
#     if sign[0]== "+":
#         result = x + y
#     elif sign[0]== "*":
#         result = x * y
#     elif sign[0]== "/":
#         result = x / y
#     elif sign[0]== "-":
#         result = x - y
#
#     # ВАРИАНТ 2
#     # result=eval(action)
#
#     print(action,"=",result)
#
# val=function()

# Задание 2


import random
list=[random.randint(-10,10)for _ in range(10)]
print(list)
def list_function():
    list_min=min(list)
    list_max=max(list)
    print("Минимальный элемент:  ", list_min)
    print("Максимальный элемент:  ", list_max)

    result_min=0
    for i in list:
        if i<0:
            result_min=result_min+1
        else:
            continue

    result_max=0
    for i in list:
        if i>0:
            result_max=result_max+1
        else:
            continue

    result_0=0
    for i in list:
        if i==0:
            result_0=result_0+1
        else:
            continue

    print("Количество отрицательных элементов:  ", result_min)
    print("Количество положительных элементов:  ", result_max)
    print("Количество нулей:  ", result_0)


val=list_function()









