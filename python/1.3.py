# -- coding: utf-8 --
name="ivan"
name2=input("Введите имя: ")
age=int(input("Введите ваш возраст: "))
i=16-age
if name!=name2:
    if 0<age<75:
        if age>=16:
            print("Поздравляем вы поступили в ВГУИТ!")
        else:
            print("Сначала нужно окончить школу!")
            print("Осталось учится", i, "лет")
    else:
        print("Сначала родись!!!")
else:
    print("Иванам нельзя!!!")