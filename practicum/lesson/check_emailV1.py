"""
Задача: Проверка корректности в формате электронной почты.
Напишите функцию, которая принимает строку(адрес почты) и проверяет, 
соответствует ли она стандартному формату адреса.

example@email.com # True
invalid.email@domain  #False
another.example@sub.domain.com  #True
"""
import re

emails = [
    "example@email.com", 
    "invalid2.email@domain", 
    "another_2example@sub.domain.com", 
    "invalid_enother?@domain.name", 
    "wdqq@qw.rr"]

def check_email(email):
    pattern =  r'^[\w\.-_]+@[\w\.-]+\.\w+$'
#    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

for email in emails:
    if check_email(email):
        print(f"{email} - True")
    else:
        print(f"{email} - False")