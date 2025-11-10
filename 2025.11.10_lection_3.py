# Задание 1

# border1=int(input("Введи границу 1:  "))
# border2=int(input("Введи границу 2:  "))
#
# print("\nЧисла кратные 7: ")
# i=border1
# for i in range (i, border2+1):
#     if i%7==0:
#         print(i,", ",end='')
#     else:
#         continue

# Задание 2

# border1=int(input("Введи границу 1:  "))
# border2=int(input("Введи границу 2:  "))
#
# print("Все числа дипазона: ")
# i=border1
# for i in range (i, border2+1):
#     print(i, ", ", end='')
#
# print("\nВсе числа в убывающем порядке: ")
# i=border2
# while i!=border1-1:
#     print(i, ", ", end='')
#     i=i-1
#
# print("\nЧисла кратные 7: ")
# i=border1
# for i in range (i, border2+1):
#     if i%7==0:
#         print(i,", ",end='')
#     else:
#         continue
#
# print("\nЧисла кратные 5: ")
# i=border1
# for i in range (i, border2+1):
#     if i%5==0:
#         print(i,", ",end='')
#     else:
#         continue

# Задание 3

border1=int(input("Введи границу 1:  "))
border2=int(input("Введи границу 2:  "))

i=border1
for i in range (i, border2+1):
    if i%3==0 and i%5==0:
        print(i,"Fizz Buzz")
    elif i%5==0:
        print(i, "Buzz ")
    elif i%3==0 :
        print(i, "Fizz ")
    else:
        print(i)

