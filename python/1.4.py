# -- coding: utf-8 --
seconds=int(input("Введите некотоое кол-во сек: "))
sec=seconds%86400%3600%60
min=seconds%86400//60
h=seconds%86400//24
d=seconds//86400
print(d, ":", h, ":", min, ":", sec)