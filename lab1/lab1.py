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










