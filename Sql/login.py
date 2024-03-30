import mysql.connector
import hashlib
from termcolor import colored


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="Project1"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS Project1(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")

def register_user(user_name, user_password):
    mycursor.execute("SELECT * FROM Project1 WHERE username=%s", (user_name,))
    if mycursor.fetchone():
        print(colored("Пользователь существует", "red"))
    else:
        user_password = hashlib.sha256(user_password.encode()).hexdigest()
        mycursor.execute("INSERT INTO Project1 (username, password) VALUES (%s, %s)", (user_name, user_password))
        print(colored("вы зарегистрированы", "green"))
        mydb.commit()

def login_user(user_name, user_password):
    user_password = hashlib.sha256(user_password.encode()).hexdigest()
    mycursor.execute("SELECT * FROM Project1 WHERE username=%s AND password=%s", (user_name, user_password))
    user = mycursor.fetchone()
    if user:
        print(colored(f"Добро пожаловать, {user_name}!", "green"))
    else:
        print(colored("Неправильный логин или пароль", "red"))

def print_user():
    mycursor.execute("SELECT username FROM Project1")
    users = mycursor.fetchall()
    for Project1 in users:
        print(f"Имя пользователь: {Project1[0]}")

if __name__ == "__main__":
    while True:
        print("\nМеню:")
        print("1. Регистрация")
        print("2. Вход")
        print("3. Просмотр всех пользователей")
        print("4. Выход")
        a = input("Выберите действие: ")
        if a == "1":
            user_name = input("Введите имя: ")
            user_password = input("Введите пароль: ")
            register_user(user_name, user_password)
        elif a == "2":
            user_name = input("Введите имя пользователь: ")
            user_password = input("Введите пароль: ")
            login_user(user_name, user_password)
        elif a == "3":
            print_user()
        elif a == "4":
            break
        else:
            print("Ошибка")