# -- coding: utf-8 --
stroka=int(input("Номер первой строки (от 1 до 8): "))
stolb=int(input("Номер первого солбца (от 1 до 8): "))
stroka2=int(input("Номер второй строки (от 1 до 8): "))
stolb2=int(input("Номер второго солбца (от 1 до 8): "))
if ((stroka and stolb)>= 1 and (stroka and stolb)<= 8) and ((stroka2 and stolb2)>= 1 and (stroka2 and stolb2)<= 8):
    if (stroka%2 == 1 and stolb%2 == 1) and (stroka%2 == 0 and stolb%2 == 0):
        color= "белый"
    else:
        color= "черный"
    if (stroka2%2 == 1 and stolb2%2 == 1) and (stroka2%2 == 0 and stolb2%2 == 0):
        color2= "белый"
    else:
        color2= "черный"
    if color==color2:
        print("Цвета совпадают")
    else:
        print("Цвета не совпадают")
else:
    print("Введите число от 1 до 8 !!!")
