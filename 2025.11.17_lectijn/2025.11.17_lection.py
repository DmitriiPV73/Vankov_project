# # Списки
# str = "text123/!"
# list = ["text", str, 1234]
# print(id(list)) #Вывод id списка
# list[2]=5678
# print(id(list))
# list2=list[:]
# print(f"копия {id(list2)}")
# list2[0]="new text in list2"
# print(list)
# print(list2)
#
# # Операции со списками
#
# # Объединение списков
# list3=list+list2
# print(f"третий список {list3}")
#
# # Умножение списков
# print(list3*3)
#
# # Проверка вхождения в список
# print("text" in list3)
#
# # Вложенные списки
# included_list=[[1,2,3,4,], ["text1", "text2"]]
# print(included_list[0][1])
# for obj in included_list:
#     for subject in obj:
#         print (subject)

# Методы списков
my_list=[]
my_list.append("Мы учим Python") # Вставить в конец списка
print(my_list)

my_list.extend([1,2,3,4]) # Расширение списка. Добавляем список в список в виде объектов
print(my_list)

my_list.insert(0, 'сегодня') # Вставка по индексу
print(my_list)

my_list.remove(1) # Удаление конкретного элемента "1"
print(my_list)

my_list.pop(0) # Удаление по индексу
print(my_list)

my_list.clear() # Очистка списка

my_list.count(1) # подсчет элементов  в списке. В данном случае считает количество единиц в списке

my_list1 = [1,2,3,4,5,6, 455, 323, 11, 146]
my_list1.sort(reverse=False) # Сортровка. Может быть по убыванию, возрастанию, и т.д.
print(my_list1)

my_list1.reverse() # Перевернуть список
print(my_list1)

counter = 0
while counter < len(my_list1):
    print(my_list1[counter])
    counter += 1

counter = 0
while counter < len(my_list1):
    val = my_list1[counter]
    if val == 323:
        print ("Мы нашли 323")
        break
    counter += 1