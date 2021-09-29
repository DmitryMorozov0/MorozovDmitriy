# -- coding: utf-8 --
a=int(input("Введите 1 число: "))
b=int(input("Введите 2 число: "))
c=int(input("Введите 3 число: "))
def n(a,b,c):
    return(min(a,b,c))
print("Наименьшее из трех чисел: ", n(a,b,c))