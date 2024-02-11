
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

# Задание 11. Отсортировать строки В порядке увеличения разницы между частотой наиболее часто
# встречаемого символа в строке и частотой его появления в алфавите.

def sort_diff_freq():
    x=str(input("Введите строку: "))
    a=[]
    b=[0.062,0.014,0.038,0.013,0.025,0.072,0.072,0.007,0.016,0.062,0.010,0.028,0.065,0.026,0.053,0.090,0.023,0.040,0.045,0.053,0.021,0.002,0.009,0.004,0.012,0.006,0.003,0.014,0.016,0.014,0.003,0.006,0.018]
    strs=[]
    diff_freq=[]
    while(x):
        strs.append(x)
        x = str(input("Введите строку: "))
    for i in range(ord('а'), ord('я') + 1):
        a.append(chr(i))
    a.insert(6,"ё")
    for word in strs:
        max_freq=0
        index_max_symb=0
        for symb in word:
            freq_symb=word.count(symb)/len(word)
            if(max_freq<freq_symb):
                max_freq=freq_symb
                index_max_symb=a.index(symb)
        diff_freq.append(max_freq-b[index_max_symb])
    for i in range(len(diff_freq)-1):
        for j in range(i+1,len(diff_freq)):
            if(diff_freq[i]>diff_freq[j]):
                t=strs[i]
                strs[i]=strs[j]
                strs[j]=t
                r=diff_freq[i]
                diff_freq[i]=diff_freq[j]
                diff_freq[j]=r
    print(strs)
    print(diff_freq)

# Задание 12. Отсортировать строки в порядке увеличения медианного значения выборки строк (прошлое
# медианное значение удаляется из выборки и производится поиск нового
# медианного значения).

def find_med_val(a):
    a.sort(key=len)
    n = len(a)
    mid = n // 2
    if n % 2 == 0:
        return (len(a[mid - 1]) + len(a[mid])) / 2
    else:
        return len(a[mid])

def sort_med_val():
    x = str(input("Введите строку: "))
    a = []
    while(x):

        a.append(x)
        x = str(input("Введите строку: "))
    median_value = find_med_val(a)
    print(sorted(a, key=lambda x: abs(len(x) - median_value)))

# Задание 13. Отсортировать строки в порядке увеличения квадратичного отклонения между наибольшим
# ASCII-кодом символа строки и разницы в ASCII-кодах пар зеркально
# расположенных символов строки (относительно ее середины).

def mid_sqr_dev():
    x = str(input("Введите строку: "))
    a = []
    while(x):

        a.append(x)
        x = str(input("Введите строку: "))
    b=[]
    for word in a:
        max_ascii=0
        for i in word:
            if(ord(i)>max_ascii):
                max_ascii=ord(i)
        diff_mirr_couple=0
        first_half = word[:len(word) // 2]
        second_half = word[len(word) // 2:]

        if len(word) % 2 == 1:
            middle = word[len(word) // 2]
            diff_mirr_couple = abs(ord(middle) - ord(middle))
        else:
            for i in range(len(first_half)):
                diff_mirr_couple += abs(ord(first_half[i]) - ord(second_half[len(second_half) - i - 1]))

        b.append(pow(max_ascii-diff_mirr_couple,2))
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if (b[i] > b[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t
                u = b[i]
                b[i] = b[j]
                b[j] = u
    print(a)
    print(b)

# Задание 14. Отсортировать строки в порядке увеличения среднего количества «зеркальных» троек
# (например, «ada») символов в строке.

def sort_count_mirror():
    x = str(input("Введите строку: "))
    a = []
    while(x):

        a.append(x)
        x = str(input("Введите строку: "))
    b=[]
    for word in a:
        c=0
        if (len(word) >= 3):
            for i in range(1,len(word)-1):
                if(word[i-1]==word[i+1]):
                    c+=1
        b.append(c)
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if(b[i]>b[j]):
                t=a[i]
                a[i]=a[j]
                a[j]=t
                u=b[i]
                b[i]=b[j]
                b[j]=u
    print(a)
    print(b)

# Задание 15. Дан целочисленный массив. Необходимо переставить в обратном
# порядке элементы массива, расположенные между его минимальным и
# максимальным элементами.

def repl_el_mass():
    x = input("Введите число: ")
    a = []
    while (x != ""):
        if x.isdigit():
            a.append(int(x))
        else:
            print("Неверный ввод!")
        x = input("Введите число: ")

    index_max = 0
    max_el = a[0]
    index_min = 0
    min_el = a[0]

    for i in range(len(a)):
        if a[i] > max_el:
            max_el = a[i]
            index_max = i
        if a[i] < min_el:
            min_el = a[i]
            index_min = i
    down_index = min(index_min, index_max)
    top_index = max(index_min, index_max)
    print("Исходный массив:", a)
    reversed_section = a[down_index + 1:top_index][::-1]
    a = a[:down_index + 1] + reversed_section + a[top_index:]
    print("Измененный массив:", a)

# Задание 16. Дан целочисленный массив. Необходимо найти два наибольших 
# элемента.

def find_2_max():
    x = input("Введите число: ")
    a = []
    while (x != "" or len(a)<2):
        if x.isdigit():
            a.append(int(x))
        else:
            print("Неверный ввод!")
        x = input("Введите число: ")
    max1=a[0]
    ind=0
    for i in range(len(a)):
        if(a[i]>max1):
            ind=i
            max1=a[i]
    a.pop(ind)
    max2=a[0]
    for i in range(len(a)):
        if(a[i]>max2):
            max2=a[i]
    print(max1)
    print(max2)

