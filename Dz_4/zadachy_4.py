# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = int(input("Введите степень многочлена: "))

my_list = []
for i in range(k+1):
    if i ==0:
       my_list.append(random.randint(1, 100)) 
    else:
        my_list.append(random.randint(0, 100))
print(my_list)

new_list = my_list[:]
wr = ''
for i in range(len(new_list)):
            if i != len(new_list) - 1 and new_list[i] != 0 and i != len(new_list) - 2:
                wr += f'{new_list[i]}x^{len(new_list)-i-1}'
                if new_list[i+1] != 0:
                    wr += ' + '
            elif i == len(new_list) - 2 and new_list[i] != 0:
                wr += f'{new_list[i]}x'
                if new_list[i+1] != 0:
                    wr += ' + '
            elif i == len(new_list) - 1 and new_list[i] != 0:
                wr += f'{new_list[i]} = 0'
            elif i == len(new_list) - 1 and new_list[i] == 0:
                wr += ' = 0'
print(wr)

with open('file.txt','w') as data:
    data.write(wr)


    
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
