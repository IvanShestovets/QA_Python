"""
Написать функцию validate_email которая принимает строку с email и 
проверяет его на корректность по следующим правилам:
Должен быть символ @ 
должен быть символ .
символ @ должен быть перед символом .

"""
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

# Пример использования функции
email1 = 'example@example.com'
email2 = 'invalid_email.com'
email3 = 'invalid@emaildotcom'

print(validate_email(email1))  # Должно вернуть True
print(validate_email(email2))  # Должно вернуть False
print(validate_email(email3))  # Должно вернуть False