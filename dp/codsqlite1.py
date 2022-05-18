import sqlite3

banco = sqlite3.connect('banco_cadastro.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, email text, senha text)")

#cursor.execute("INSERT INTO pessoas VALUES ('Mario', 'mei@gmail.com', 'ttt')")

#banco.commit()

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())