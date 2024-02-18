# Тангиев Руслан, 37/1

# Лабораторная работа №2. Вариант 2

# задание 1
def find_ident_el():
    x = input("Введите число в список a: ")
    a = []
    while (x != ""):
        if x.isdigit():
            a.append(int(x))
        else:
            print("Неверный ввод!")
        x = input("Введите число в список а: ")

    b=[]
    x = input("Введите число в список b: ")
    while (x != ""):
        if x.isdigit():
            b.append(int(x))
        else:
            print("Неверный ввод!")
        x = input("Введите число в список b: ")
    for i in a:
        for j in b:
            if(i==j):
                print(i)
                break
find_ident_el()
