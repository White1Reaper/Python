# Тангиев Руслан, 37/1

# Лабораторная работа №6.

# Эадание 1. Вариант 12. Создать БД в соответствии с предметной областью: страховая компания.
import json
import sqlite3
import http.server
import socketserver
import cgi

def database_and_server():
    insurance_company = sqlite3.connect('./cgi-bin/insurance-company.db')
    # Эадание 2. БД должна содержать не менее трех связанных таблиц.
    cursor = insurance_company.cursor()
    cursor.execute("DROP TABLE Clients")
    cursor.execute("DROP TABLE Claims")
    cursor.execute("DROP TABLE Policies")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Policies (
    policy_id INTEGER PRIMARY KEY,
    policy_number INTEGER NOT NULL,
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
    (001, '2023-01-01', '2024-01-01', 1000),
    (002, '2023-02-01', '2024-02-01', 1200),
    (003, '2023-03-01', '2024-03-01', 1500)""")


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

    class MyHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            # Получение данных из формы
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST','CONTENT_TYPE': self.headers['Content-Type'],
                         }
            )
            if 'addclient' in form:
                full_name = form.getvalue('full_name')
                date_of_birth = form.getvalue('date_of_birth')
                address = form.getvalue('address')
                cursor.execute("INSERT INTO Clients (full_name, date_of_birth, address) VALUES (?, ?, ?)",(full_name, date_of_birth, address))
            elif 'addpolicy' in form:
                pol_num = form.getvalue('num')
                start = form.getvalue('date1')
                end = form.getvalue('date2')
                price=form.getvalue('amount')
                cursor.execute("INSERT INTO Policies (policy_number, start_date, end_date, price) VALUES (?, ?, ?, ?)",(pol_num, start, end,price))
            elif 'addclaim' in form:
                policy_id = form.getvalue('policy_id')
                client_id = form.getvalue('client_id')
                claim_date = form.getvalue('claim_date')
                amount = form.getvalue('amount')
                cursor.execute("INSERT INTO Claims (policy_id, client_id, claim_date, amount) VALUES (?, ?, ?, ?)",(policy_id, client_id, claim_date, amount))
            insurance_company.commit()
            # Задание 8. Экспорт/импорт таблицы в JSON
            if 'addclient' in form:
                cursor.execute('SELECT * FROM Clients')
                table_out = json.dumps(cursor.fetchall())

                with open('Clients.json', 'w') as f:
                    f.write(table_out)
                with open('Clients.json', 'r') as f:
                    json_data = f.read()

                table_in= json.loads(json_data)

                for st in table_in:
                    print(st)
            elif 'addclaim' in form:
                cursor.execute('SELECT * FROM Claims')
                table_out = json.dumps(cursor.fetchall())

                with open('Claims.json', 'w') as f:
                    f.write(table_out)
                with open('Claims.json', 'r') as f:
                    json_data = f.read()

                table_in= json.loads(json_data)

                for st in table_in:
                    print(st)
            elif 'addpolicy' in form:
                cursor.execute('SELECT * FROM Policies')
                table_out = json.dumps(cursor.fetchall())

                with open('Policies.json', 'w') as f:
                    f.write(table_out)
                with open('Policies.json', 'r') as f:
                    json_data = f.read()

                table_in= json.loads(json_data)

                for st in table_in:
                    print(st)
            self.send_response(303)
            self.send_header('location','/')
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Задание 6. Создать форму (формы) для заполнения полей таблиц.
            # Задание 7. Осуществить вывод содержимого таблиц.
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
            html += """
            <form method="POST" action="">
              <label for="full_name">name:</label>
              <input type="text" name="full_name">
              <br>
              <label for="date_of_birth">birth date:</label>
              <input type="date" name="date_of_birth">
              <br>
              <label for="address">address:</label>
              <input type="text" name="address">
              <br>
              <label for "addclient"</label>
              <input type="submit" name="addclient" value="add_client">
            </form>
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
                    <th>start date</th>
                    <th>end date</th>
                    <th>amount</th>
                  </tr>
                </thead>
                <tbody>
                
                <form method="POST" action="">
      <label for="<form method="POST" action="">
      <label for="num">policy number:</label>
      <input type="text" name="num">
      <br>
      <label for="date1">start date:</label>
      <input type="date" name="date1">
      <br>
      <label for="date2">end date:</label>
      <input type="date" name="date2">
      <br>
        <label for="amount">amount:</label>
      <input type="text" name="amount">
      <br>
      <label for "addpolicy"</label>
      <input type="submit" name="addpolicy" value="add_policy">
    </form>
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
                <form method="POST" action="">
      <label for="policy_id">policy id:</label>
      <input type="text" name="policy_id">
      <br>
      <label for="client_id">client id:</label>
      <input type="text" name="client_id">
      <br>
      <label for="claim_date">claim date:</label>
      <input type="date" name="claim_date">
      <br>
      <label for="amount">amount:</label>
      <input type="text" name="amount">
      <br>
      <label for "addclaim"</label>
      <input type="submit" name="addclaim" value="add_claim">
    </form>
            """
            for row in cursor.execute('SELECT * FROM Claims'):
                html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(*row)

            html += """
                </tbody>
              </table>
     
            """

            html+="""
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
database_and_server()
