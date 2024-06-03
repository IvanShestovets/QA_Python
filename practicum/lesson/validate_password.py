"""
Напишите функцию для проверки пароля на соответствие следующим условиям:

Длина не должна быть меньше 8
Должна быть как минимум 1 цифра
Как минимум 1 буква
И как минимум 1 знак + в начале или в конце

"""

import re

def validate_password(password):
    pattern = r'^(\+?[\w\.-]+)$'
    
    if len(password) < 8:
        return False
    
    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'[a-zA-Z]', password):
        return False
    
    if not re.match(pattern, password):
        return False
    
    return True

print(validate_password('+Qw78111fd')) #True
print(validate_password('Qw78111fd+')) #False
print(validate_password('er.!iku')) #False
print(validate_password('eri3u')) #false

