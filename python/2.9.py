# -- coding: utf-8 --
n=int(input("Введите первое число: "))
m=int(input("Введите первое число: "))
k=int(input("Введите число долек : "))
if n!=m:
    if k< n*m and (k%n == 0 or k%m == 0):
        print("Да")
    else:
        print("Нет")
else:
    print("Смотри условие!")