# Тангиев Руслан, 37/1

# Лабораторная работа №6.

# Эадание 1. Вариант 12. Создать БД в соответствии с предметной областью: страховая компания.
import sqlite3

insurance_company = sqlite3.connect('insurance-company.db')
# Эадание 2. БД должна содержать не менее трех связанных таблиц.
cursor = insurance_company.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Policies (
policy_id INTEGER PRIMARY KEY,
policy_number TEXT NOT NULL,
start_date TEXT,
end_date TEXT,
price REAL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Clients (
client_id INTEGER PRIMARY KEY,
full_name TEXT NOT NULL,
date_of_birth TEXT,
address TEXT
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Claims (
claim_id INTEGER PRIMARY KEY,
policy_id INTEGER NOT NULL,
client_id INTEGER NOT NULL,
claim_date TEXT,
amount REAL,
FOREIGN KEY (policy_id) REFERENCES Policies(policy_id),
FOREIGN KEY (client_id) REFERENCES Clients(client_id)
)""")
insurance_company.close()
