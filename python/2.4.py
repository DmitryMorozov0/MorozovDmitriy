# -- coding: utf-8 --
a=int(input("Расстояние между рядами: "))
b=int(input("Расстояние между дырочками в ряду: "))
l=int(input("Длина свободного конца шнурка: "))
n=int(input("Количество дырочек в каждом ряду: "))
def s(a,b,l,n):
    return (n-1)*b*2 + (n*2)*a + l*2
print("Искомая длина шнурка: ", s(a,b,l,n))
