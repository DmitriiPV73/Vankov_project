# Задание 1

# line_1=input("Веди строку:  ")
# line_1=line_1[::-1]
# print(line_1)

# Задание 2

# text=input("Веди строку:  ")
# letter=0
# figure=0
# for char in text:
#     if char.isalpha():
#         letter+=1
#     else:
#         figure+=1
# print(letter)
# print(figure)

# Задание 3

# text=input("Веди строку:  ")
# symbol=input("Введи символ:  ")
# counter = 0
# for char in text:
#     if char==symbol:
#         counter+=1
#     continue
# print(counter)

# Задание 4

# text=input("Веди строку:  ")
# word=input("Введи слово:  ")
#
# val = text.count(word)
# print(val)

# Задание 5

text=input("Веди строку:  ")
word1= input("Введи слово 1:  ")
word2= input("Введи слово 2:  ")

val = text.replace(word1, word2)
print(val)