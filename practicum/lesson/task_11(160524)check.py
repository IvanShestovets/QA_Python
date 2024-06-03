"""
Задача:


Написать функцию, которая будет имитировать процесс регистрации пользователя(нового) Имя, email , пароль.
Проверить на корректность если все ок сообщения аля тип зарегистрировался и добавить нового пользователя 
в базу и вывести в конце базу по запросу , если какой-то из пунктов не корректный то выдать сообщение 
о том что не так. Все в цикле.

1. Правильность почты
2. Проверка уникальности email
3. Проверка пароля (пароль должен быть не менее 8 символов, содержать в себе как минимум 1 заглавную букву, 1 цифру, 1 знак.
4. Проверка имени, имя не должно содержать в себе символы, цифры (кроме -) и длина не менее 2 символов.

user_database = {
    "user1@example.com": {'name':'User', 'password': 'Qwe12343r'},
    "user2@example.com": {'name':'Vasya', 'password': 'Qwe12343r'},
    "user3@example.com": {'name':'Petya', 'password': 'Qwe12343r'},
    "user4@example.com": {'name':'Sereja', 'password': 'Qwe12343r'}}
"""

import re

user_database = {
    "user1@example.com": {'name':'User', 'password': 'Qwe12343r'},
    "user2@example.com": {'name':'Vasya', 'password': 'Qwe12343r'},
    "user3@example.com": {'name':'Petya', 'password': 'Qwe12343r'},
    "user4@example.com": {'name':'Sereja', 'password': 'Qwe12343r'},
}

def register_user():
    while True:
# Проверка имени
        name = input("Введите ваше имя: ")
        if not re.match(r'^[a-zA-Zа-яА-Я\-]{2,}$', name):
            print("Ийймя не должно содержать в себе символы, цифры (кроме -) и длина не менее 2 символов.")
            continue
# Правильность почты        
        email = input("Введите ваш email: ")
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            print("Некорректный email.")
            continue
# Проверка уникальности email
        if email in user_database:
            print("Такой email уже существует.")
            continue
# Проверка пароля
        password = input("Введите пароль: ")
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', password):
            print("Пароль должен быть не менее 8 символов, содержать в себе как минимум 1 заглавную букву, 1 цифру, 1 знак.")
            continue
# Добавление пользователя в словарь                    
        user_database[email] = {'name': name, 'password': password}
        print(f"Регистрация ок!")
# Запрос на повтор цикла
        repit = input("Хотите продолжить? Введите '+' если да, или другой символ для окончания цикла:")
        if repit != "+":
            break
# Вывод словаря    
    for email, user_data in user_database.items():
        print(f"Email: {email}, Имя: {user_data['name']}")

register_user()



