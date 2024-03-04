# Тангиев Руслан, 37/1

# Лабораторная работа №6.

# Эадание 1. Вариант 12. Создать БД в соответствии с предметной областью: страховая компания.
import sqlite3
import http.server
import socketserver
insurance_company = sqlite3.connect('./cgi-bin/insurance-company.db')
# Эадание 2. БД должна содержать не менее трех связанных таблиц.
cursor = insurance_company.cursor()
# cursor.execute("DROP TABLE Clients")
# cursor.execute("DROP TABLE Claims")
# cursor.execute("DROP TABLE Policies")
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

# Задание 4. Написать не менее трех статистических запросов (SELECT).

cl=cursor.execute('SELECT * FROM Clients')
for cl1 in cl:
    print(cl1)

print()
pl=cursor.execute('SELECT * FROM Policies')
for pl1 in pl:
    print(pl1)
print()
clim=cursor.execute('SELECT * FROM Claims WHERE claim_id="2"')
for cl1 in clim:
    print(cl1)
# Задание 7. Осуществить вывод содержимого таблиц.
class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
          <title>insurance company</title>
        </head>
        <body>
          <h1>clients</h1>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>fio</th>
                <th>birth date</th>
                <th>address</th>
              </tr>
            </thead>
            <tbody>
        """

        for row in cursor.execute('SELECT * FROM Clients'):
            html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(*row)

        html += """
            </tbody>
          </table>

          <h1>policies</h1>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>policy number</th>
                <th>start datчe</th>
                <th>end date</th>
                <th>amount</th>
              </tr>
            </thead>
            <tbody>
        """
        for row in cursor.execute('SELECT * FROM Policies'):
            html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(*row)

        html += """
            </tbody>
          </table>

          <h1>claims</h1>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>policy</th>
                <th>client</th>
                <th>claim date</th>
                <th>amount</th>
              </tr>
            </thead>
            <tbody>
        """
        for row in cursor.execute('SELECT * FROM Claims'):
            html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(*row)

        html += """
            </tbody>
          </table>
        </body>
        </html>
        """

        self.wfile.write(html.encode('utf-8'))

# Задание 5. Создать CGI-сервер.
PORT = 8000
httpd = socketserver.TCPServer(("", PORT), MyHandler)
httpd.serve_forever()

insurance_company.commit()
cursor.close()


insurance_company.close()
