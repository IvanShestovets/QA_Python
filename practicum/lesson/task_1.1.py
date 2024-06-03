"""
Напишите функцию для проверки корректности номера телефона в веб-форме. 
Допустим у нас номер телефона должен соответствовать определенному формату 
+XXXXXXXXXXX - где X цифра от 0-9

В номере не должно быть ничего кроме набора цифр от 0 до 9 для каждого X и 
первый знак (символ) всегда будет +

"""

def phone_num(phone_number):
    if len(phone_number) != 12:
        return False
    if phone_number[0] != '+':
        return False
    
    for char in phone_number[1:]:
        if not char.isdigit():
            return False
    return True

print(phone_num('+79211007238'))

