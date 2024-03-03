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
start_date DATETIME,
end_date DATETIME,
price REAL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Clients (
client_id INTEGER PRIMARY KEY,
full_name TEXT NOT NULL,
date_of_birth DATETIME,
address TEXT
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Claims (
claim_id INTEGER PRIMARY KEY,
policy_id INTEGER NOT NULL,
client_id INTEGER NOT NULL,
claim_date DATETIME,
amount REAL,
FOREIGN KEY (policy_id) REFERENCES Policies(policy_id),
FOREIGN KEY (client_id) REFERENCES Clients(client_id)
)""")

# Задание 3. Заполнить таблицы БД информацией с помощью SQL- запросов.

cursor.execute("""INSERT INTO Policies (policy_number, start_date, end_date, price) VALUES
('P001', '2023-01-01', '2024-01-01', 1000),
('P002', '2023-02-01', '2024-02-01', 1200),
('P003', '2023-03-01', '2024-03-01', 1500)""")


cursor.execute("""INSERT INTO Clients (full_name, date_of_birth, address) VALUES
('John Doe', '1980-01-01', '123 Main Street'),
('Jane Doe', '1985-02-01', '456 Elm Street'),
('Peter Jones', '1990-03-01', '789 Oak Street')""")

cursor.execute("""INSERT INTO Claims (policy_id, client_id, claim_date, amount) VALUES
(1, 1, '2023-04-01', 500),
(2, 2, '2023-05-01', 700),
(3, 3, '2023-06-01', 900)""")


cursor.execute("DROP TABLE Claims")
cursor.execute("DROP TABLE Policies")
cursor.execute("DROP TABLE Clients")

insurance_company.close()
