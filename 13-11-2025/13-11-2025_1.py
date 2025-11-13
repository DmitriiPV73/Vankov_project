# name=input("Введи имя: ")
# x=len(name)+4
# print("*"*x)
# print("*",name,"*")
# print("*"*x)

# val_list=[1, "int", 3.8, True, [1,2]]

# Создание списка из строки
# a="Hello World!"
# a_list=list(a)
# print(a_list)
# a_str=str(a_list)
# print(a_str)
#
# a_list=list(range(1,10))
# print(a_list)
# print(type(a_list))

# Пустой список
# d=list()
# print(d)

# Замена в списке
# fruits=["Яблоко", "Апельсин", "Банан", "Ананас"]
# print(id(fruits))
# val_list=[1,"int", 3.9, True, [1,2]]
# fruits [2]="Банан"
# print(fruits)
# print(id(fruits))


nambers=[1,2,3,4,5,6,7,8,9]
print(nambers)
nambers.insert(0,256)
print(nambers)
nambers.append(458)
print(nambers)
nambers.pop(0)
nambers.pop(-1)
print(nambers)
x=5
if x in nambers:
    print("В списке")
else:
    print("Не в списке")



