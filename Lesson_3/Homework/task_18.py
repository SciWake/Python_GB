"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
к заданному числу X. Пользователь в первой строке вводит натуральное число N – 
количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*

5
1 2 3 4 5
6
-> 5"""
    
n = int(input("Введите количество элементов в массиве: "))
list_1 = list()
for i in range(n):
    x = int(input("Введите элемент массива: "))
    list_1.append(x)


x = int(input("Введите число, чтобы найти ближайшее число в массиве: "))
dist = abs(x - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, n):
    if dist > abs(list_1[i] - x):
        dist = abs(list_1[i] - x)
        number = list_1[i]
print(number)

print("Ближайшим элементом массива к числу", x, "является", number)
