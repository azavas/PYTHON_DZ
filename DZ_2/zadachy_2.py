#Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


number = float(input('Введите число: '))
s = str(number)
sum =0
for i in range(0,len(s)):
    if s[i] != '.':
        sum=sum+int(s[i])
    else :
        i+1
print(f'Сумма цифр = {sum}')


# Задача 2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.

# N = int(input("Введите число: "))
# result = []
# for i in range(1, N+1):
#     result.append(round((1+1/i)**i, 2))

# print(f' Для N = {N}->', end=" ")
# print(result, sep=', ')
# print(f'Сумма {sum(result)}')

#Задача 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int
# import random

# my_list = []
# for i in range(10):
#     my_list.append(random.randint(0,100)) 
# mix_list = my_list[:]    
# for i in range(len(my_list)):
#     mix = random.randint(0, len(my_list) - 1)
#     temp = my_list[i]
#     my_list[i] = my_list[mix]
#     my_list[mix] = temp

# print(f'Изначальный список: {my_list}')
# print(f'Перемешанный список: {mix_list}')