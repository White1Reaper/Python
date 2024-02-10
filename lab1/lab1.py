
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




