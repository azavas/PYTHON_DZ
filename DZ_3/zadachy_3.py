# Задача 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
import random

# my_list = []
# for i in range(10):
#     my_list.append(random.randint(1,10))
# print(my_list)
# sum = 0
# new_list = []
# for i in range(len(my_list)):
#     div = i%2
#     if div!=0:
#         sum=sum+my_list[i]
#         new_list.append(my_list[i])
# print(f'На нечетных позициях элементы {new_list} Сумма этих элементов = {sum}')

# Задача2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# my_list = []
# for i in range(10):
#     my_list.append(random.randint(1, 10))
# print(my_list)
# pr = 0
# s = 1

# new_list = []
# for i in range(int(len(my_list)/2)):
#     pr = my_list[i]*my_list[(len(my_list)-s)]
#     s = s+1
#     new_list.append(pr)

# print(new_list)

#Задача 3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# my_list = []
# for i in range(5):
#     my_list.append(round(random.random(),2))
# print(my_list)
# new_list = []
# for i in my_list:
#     if i%1!=0:
#      new_list.append(round(i%1,2))
# print(f'Разница между максимальным и минимальным значением дробной части = {max(new_list) - min(new_list)}')


# Задача 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# N = int(input("Введите число: "))
# dv=''
# while N != 0:
#     dv = str(N%2) + dv
#     N = N//2
# print(dv)