# Тангиев Руслан, 37/1

# Лабораторная работа №6.

# Эадание 1. Вариант 12. Создать БД в соответствии с предметной областью: страховая компания.
import sqlite3

insurance_company = sqlite3.connect('insurance-company.db')

insurance_company.close()