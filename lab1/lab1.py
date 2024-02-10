
# Тангиев Руслан, 37/1

# Лабораторная работа №1. Вариант 12

# задание 1

# функция 1. Найти сумму непростых делителей числа.

def sum_nepr_del(x):
    sum=0
    for i in range(2,x+1):
        if(x%i==0):
            for j in range(2,i):
                if(i%j==0):
                    sum+=i
                    break
    return sum

# функция 2. Найти количество цифр числа, меньших 3.

def kol_sifr(x):
    x1=x
    c=0
    while(x1):
        if(x1%10<3):
            c+=1
        x1//=10
    return c

# функция 3. Найти количество чисел, не являющихся делителями исходного числа, не взамно простых с ним и взаимно простых с суммой простых цифр этого числа.
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_mut_prime(x, y):
    for i in range(2, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            return False
    return True

def sum_prime_sifr(x):
    digit_sum = 0
    for digit in str(x):
        if is_prime(int(digit)):
            digit_sum += int(digit)
    return digit_sum

def num_count(x):
    count = 0
    for i in range(2, x):
        if i % x != 0 and not is_mut_prime(i, x) and is_mut_prime(i, sum_prime_sifr(x)):
            count += 1
    return count


# задание 2.  Дана строка в которой записаны слова через пробел. Необходимо
# перемешать в каждом слове все символы в случайном порядке кроме первого
# и последнего.

import random
def shake_symbs():
    text=str(input("Введите строку: "))
    words = text.split()
    for word in words:
        if (len(word) <= 3):
            print(word)
        else:
            w = ""
            w1 = ""
            w1 += word[0]
            for i in range(1, len(word) - 1):
                w += word[i]
            w = list(w)
            random.shuffle(w)
            w = ''.join(w)
            w1 += w
            w1 += word[len(word) - 1]
            print(w1)

# задание 3. Дана строка в которой содержатся цифры и буквы. Необходимо
# расположить все цифры в начале строки, а буквы – в конце.

def div():
    a = ""
    b = ""
    text = str(input("Введите строку: "))
    for symb in text:

        if (symb.isdigit()):
            a += symb
        else:
            b += symb
    print(a + b)

# Задание 4. Дана строка в которой записаны слова через пробел. Необходимо
# перемешать все слова в случайном порядке (спонсор задачи Мастер Йода).

import random
def shake_words():
    text = str(input("Введите строку: "))
    words = text.split()
    random.shuffle(words)
    s = ""
    for h in words:
        s += h + " "
        print(s)

# Задание 5. Дана строка. Необходимо найти все даты, которые описаны в
# виде "31 февраля 2007".

import re

def find_dates():
    text = str(input("Введите строку: "))
    pattern = r"\b(\d{1,2} (?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря) \d{4})\b"
    dates = re.findall(pattern, text)
    print(dates)

# Задание 6. Дана строка. Необходимо подсчитать количество чисел в этой строке,
# значение которых больше 5.

def count_nums():
    s=str(input("Введите строку: "))
    num = ""
    c=0
    for symb in s:
        if(symb.isdigit()):
            num+=symb
        else:
            if(num!="" and int(num)>5):
                c+=1
                num=""
            else:
                m=""
    print(c)

# Задание 7. Дана строка. Необходимо найти те символы кириллицы, которые не
# задействованы в данной строке.
def find_symb():
    s=str(input("Введите строку: "))
    for i in range(ord('а'), ord('я') + 1):
        c=1
        for symb in s:
            if(i==ord(symb)):
                c=0
        if(c):
            print(chr(i))

# Задание 8. Дана строка. Необходимо найти максимальное из имеющихся в ней
# натуральных чисел.
def find_max():
    s=str(input("Введите строку: "))
    max_num=0
    num = ""
    for symb in s:
        if(symb.isdigit()):
            num+=symb
        else:
            if(num!="" and int(num)>max_num):
                max_num=int(num)
                num=""
            else:
                num=""
    print(max_num)

# Задание 9. Прочитать список строк с клавиатуры. Упорядочить по длине
# строки.
def sort_str_list():
    x=str(input("Введите строку: "))
    a=[]
    while(x):
        a.append(x)
        x = str(input("Введите строку: "))
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if(len(a[i])>len(a[j])):
                t=a[i]
                a[i]=a[j]
                a[j]=t
    print(a)

# Задание 10. Дан список строк с клавиатуры. Упорядочить по количеству
# слов в строке

def sort_str_count_list():
    x=str(input("Введите строку: "))
    a=[]
    while(x):
        a.append(x)
        x = str(input("Введите строку: "))
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            c1=a[i].count(" ")
            c2=a[j].count(" ")
            if(c1>c2):
                t=a[i]
                a[i]=a[j]
                a[j]=t
    print(a)
