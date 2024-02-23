# Тангиев Руслан, 37/1

# Лабораторная работа №4

# Задание 1. Вариант 2.Менеджер по работе с персоналом присваивает рейтинговый балл
# каждому из N кандидатов, резюме которых он изучает. Он хочет нанять двух
# специалистов с суммарным рейтингом не менее К баллов. Требуется по
# имеющимся данным о баллах N кандидатов определить, сколько различных
# пар кандидатов можно выбрать так, чтобы их суммарный рейтинговый балл
# составлял не менее К. Две пары кандидатов считаются различными, если хотя
# бы один из членов пары не присутствует в другой паре. Запишите в ответе
# найденное количество пар.
# Входные данные: Даны два входных файла: файл A (27-169a.txt) и
# файл B (27-169.txt), каждый из которых в первой строке содержит
# натуральное число N (1 < N ≤ 10 000 000) – количество кандидатов, и
# натуральное число К (1 < K ≤ 10 000 000) – ограничение на суммарный рейтинг
# двух кандидатов в баллах. В каждой из следующих N строк находится одно
# число: рейтинговый балл соответствующего кандидата.


def work_with_file():
    with open('C:/Users/shopt/OneDrive/Рабочий стол/универ/питон/материалы/Лабы/ЛР4/27-169b.txt') as file:
        str1=file.readline()
        a=str1.split()
        n=int(a[0])
        k=int(a[1])
        values=[]
        count=0
        for _ in  range(n):
            values.append(int(file.readline()))
        values.sort()
        i=0
        j=n-1
        while i<n:
            while j>1 and values[i]+values[j]>=k:
                j-=1
            count+=n-max(i+1,j+1)
            i+=1
        print("Файл 27-169b.txt:", count)
    with open('C:/Users/shopt/OneDrive/Рабочий стол/универ/питон/материалы/Лабы/ЛР4/27-169bb.txt') as file:
        str1=file.readline()
        a=str1.split()
        n=int(a[0])
        k=int(a[1])
        values=[]
        count=0
        for _ in  range(n):
            values.append(int(file.readline()))
        values.sort()
        i=0
        j=n-1
        while i<n:
            while j>1 and values[i]+values[j]>=k:
                j-=1
            count+=n-max(i+1,j+1)
            i+=1
        print("Файл 27-169bb.txt:",count)

# Эадание 2. Вариант 12. Дан файл, содержащий зашифрованный русский текст.
# Каждая буква заменяется на следующую за ней (буква я заменяется на а).
# Получить в новом файле расшифровку данного текста.
def decoding():
    with open('C:/Users/shopt/OneDrive/Рабочий стол/универ/питон/дз/coded.txt', 'r', encoding='utf-8') as coded:
        decoded=open('C:/Users/shopt/OneDrive/Рабочий стол/универ/питон/дз/decoded.txt','w')
        coded_text=coded.readlines()
        print(coded_text)
        decoded_text=[]
        for line in coded_text:
            str=""
            for symb in line:
                if ord(symb)!=90 and ord(symb)!=122 and ord(symb)!=223 and ord(symb)!=255 and ord(symb)!=10:
                    str+=chr(ord(symb)+1)
                elif ord(symb)==90:
                    str+="A"
                elif ord(symb)==122:
                    str+="a"
                elif ord(symb)==223:
                    str+="А"
                elif ord(symb)==255:
                    str+="а"
            decoded_text.append(str)
        print(decoded_text)
        for decoded_line in decoded_text:
            decoded.write(decoded_line + '\n')
        decoded.close()
