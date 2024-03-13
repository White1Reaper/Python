# Тангиев Руслан, 37/1

# Лабораторная работа №9.

# Эадание 1. Вариант. 12. Дан файл в формате csv. (Фамилия, Имя, Учреждение
# (организация), Отдел, Адрес электронной почты, Состояние, Тест начат,
# Завершено, Затраченное время, Оценка/100,00, В.1 /10,00, В.2 /10,00, В.3
# /10,00, В.4 /10,00, В.5 /10,00, В.6 /10,00, В.7 /10,00, В.8 /10,00, В.9 /10,00, В.10
# /10,00).
# Примечание: Тест считается пройденным, если набрано 6/10 (60/100)
# баллов.
# Примечание: Поля «Тест начат», «Завершено» заданы в формате «12
# Май 2017 10:09», поле «Затраченное время» в формате «31 мин. 22 сек.».
# Вывести в алфавитном порядке слушателей, набравших заданное
# количество баллов и выполнивших тест за наименьшее время.
import csv
import re
def balls(ball):
    match = re.match(r"(\d+),(\d+)", ball)
    if match:
        return int(match.group(1))
def extract_seconds(dur):
    match1 = re.match(r"(\d+) мин\. (\d+) сек\.", dur)
    match2 = re.match(r"(\d+) ч\. (\d+) мин\.", dur)
    match2_2 = re.match(r"(\d+) час\. (\d+) мин\.", dur)
    match3 = re.match(r"(\d+) дн\. (\d+) час\.", dur)
    if match1:
        minutes = int(match1.group(1))
        seconds = int(match1.group(2))
        return minutes * 60 + seconds
    else:
        if match2:
            hours = int(match2.group(1))
            seconds = int(match2.group(2))
            return hours*3600 + seconds
        else:
            if match2_2:
                minutes = int(match2_2.group(2))
                hours = int(match2_2.group(1))
                return hours * 3600 + minutes*60
            else:
                if match3:
                    days = int(match3.group(1))
                    hours = int(match3.group(2))
                    return hours*3600 + days*86400
                else:
                    raise ValueError("Неверный формат строки времени")



def csv_files():
    with open("12-1.csv", encoding='utf-8') as r_file:
        inp = int(input("Введите заданное ко-лво баллов для файла 1: "))
        file_reader = csv.reader(r_file, delimiter=",")
        file_reader2 = csv.reader(r_file, delimiter=",")
        count = 0
        min_time = 1000000
        c = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                q = 0
            else:
                if row[0] == "Среднее по группе":
                    break
                if inp == balls(row[9]) and min_time > int(extract_seconds(row[8])) and balls(row[9]) >=6:
                    min_time = int(extract_seconds(row[8]))
                    c = 1
            count += 1
        counter = 0
        if not c:
            print("Такого результата ни у кого нет!")
        chosen_persons = []
        r_file.seek(0)
        for row in file_reader:
            if counter == 0:
                q = 0
            else:
                if row[0] == "Среднее по группе":
                    break
                if inp == balls(row[9]) and min_time == int(extract_seconds(row[8])):
                    chosen_persons.append(row)
            counter += 1
        sorted(chosen_persons, key=lambda x: chosen_persons[0])
        print("Результат для файла 1:")
        print(chosen_persons)
        print()
        print()
    with open("12-2.csv", encoding='utf-8') as r_file:
        inp = int(input("Введите заданное ко-лво баллов для файла 2: "))
        file_reader = csv.reader(r_file, delimiter=",")
        file_reader2 = csv.reader(r_file, delimiter=",")
        count = 0
        min_time = 1000000
        c = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                q = 0
            else:
                if row[0] == "Среднее по группе":
                    break
                if inp == balls(row[9]) and min_time > int(extract_seconds(row[8])):
                    min_time = int(extract_seconds(row[8]))
                    c = 1
            count += 1
        counter = 0
        if not c:
            print("Такого результата ни у кого нет!")
        chosen_persons = []
        r_file.seek(0)
        for row in file_reader:
            if counter == 0:
                q = 0
            else:
                if row[0] == "Среднее по группе":
                    break
                if inp == balls(row[9]) and min_time == int(extract_seconds(row[8])) and balls(row[9]) >=60:
                    chosen_persons.append(row)
            counter += 1
        sorted(chosen_persons, key=lambda x: chosen_persons[0])
        print("Результат для файла 2:")
        print(chosen_persons)
        print()
        print()
csv_files()