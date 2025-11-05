x=int(input("Введи число:  "))


summa=0
for i in range (1, x+1, 10):
    print (i, end=', ')
    summa = summa + i


print("Сумма =", summa)
