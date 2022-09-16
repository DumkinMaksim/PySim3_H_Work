# # 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# # Пример:

# # [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import numbers
import random
from turtle import onclick 


# def rand_nums(num_min:int,num_max:int, kolvo:int): 
#     '''
#     функция генерирует рандомные целые цисла 
#     принимает целые 
#     num_min-минимальное знацение
#     num_max- максимальное значение диапазона
#     kolvo- количество элементов
#     на выходе список целых чисел из указанных входных данных
#     '''
#     for i in range(kolvo):
#         randa_num=[ random.randint(num_min, num_max) for i in range(kolvo)]
#         return randa_num

# numbers=rand_nums(-30,30,10)
# print(numbers)


# def num_sums(twonumb):
#     sums=0
#     for i in twonumb:
#         sums+=i
#     return sums
# twonumb=numbers[1::2]



# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# one_list=numbers
# print(one_list)

# def find_mult_elements(оne_list):
#     '''
#     Принимает список целых чисел и находит произведение крайних элементов
#     '''
#     if len(one_list)%2==0:
#         minisize=len(one_list)/2
#     else:
#         int((len(one_list)/2)+0.5)
#     rezult_list=[]
#     i=0

#     while i<=minisize-1:
#         rezult_list.append(one_list[i]*one_list[(i+1)*-1])
#         i+=1
#     return rezult_list

# print(find_mult_elements(one_list))


# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

# numbs=[4.07, 5.1, 8.2444, 6.98]
# print('Даны элементы', numbs)
# temp_list=[]
# for i in numbs:
#     temp_list.append(str(str(i).split('.')[1]))

# print('Дробная часть элементов списка',temp_list)

# def find_min_max(numb_list):
#     rez_minmax=0
#     max_numb=max(numb_list)
#     min_numb=min(numb_list)
#     print('Max  '+str(max_numb)+'   Min  '+str(min_numb))
   
#     if int(max_numb)<10:
#         max_numb=int(max_numb)*10
#     rez_minmax=int(max_numb)-int(min_numb)
       
    
#     return 'Разница между максимальным и минимальным значением дробной части элементов-> '+str(rez_minmax)

# print(find_min_max(temp_list))


# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

# binary=[]
# def find_decimal_to_binary(number,m):
#     '''
#     решение с использованием рекурсии
#     '''
#     if number==0:
#         return 1
#     else:
#         binary.insert(m,number%2)    
#     return find_decimal_to_binary(number//2,m-1)
# num=find_decimal_to_binary(int(input('input decial->')),-1)
# print(binary)


# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k=int(input('Inpur k  integer for Fibanachi-> '))
def Fiba_pozitiv(arg,)-> list:
    '''
    Вывод положительного ряда Фибаначи
    '''
    f_pozitiv=[]
    fib_k1=0
    fib_k2=1
    for i in range(arg+1):
        if i==0: f_pozitiv.insert(i,fib_k1)
        elif i==1: f_pozitiv.insert(i,fib_k2)
        else:
            f_pozitiv.insert(i,fib_k1+fib_k2)
            temp=fib_k2
            fib_k2=fib_k2+fib_k1
            fib_k1=temp

    return f_pozitiv
pozitiv_f=Fiba_pozitiv(k)
print('Вывод положительного ряда Фибаначи-> '+str(pozitiv_f))


def Fiba_negativ(arg2)->list:
    '''
    Вывод отрицательного ряда Фибаначи
    '''
    f_negativ=[]
    fib_k1=1
    fib_k2=-1
    for i in range(arg2):
        if i==0: f_negativ.insert(i,fib_k1)
        elif i==1: f_negativ.insert(i,fib_k2)
        else:
            f_negativ.insert(i,fib_k1-fib_k2)
            temp=fib_k2
            fib_k2=fib_k1-fib_k2
            fib_k1=temp

    return f_negativ
negativ_f=Fiba_negativ(k)
print('Вывод отрицательного ряда Фибаначи-> '+str(negativ_f))
    

all_fiba=str(negativ_f[::-1] +negativ_f)
print('Последовательность Фибаначи отриц+полож-> '+all_fiba) 