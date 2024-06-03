"""
Напишите функцию для проверки пароля на соответствие следующим условиям:

Длина не должна быть меньше 8
Должна быть как минимум 1 цифра
Как минимум 1 буква
И как минимум 1 знак + в начале или в конце


"""

def valid_pas(pas_):
    if len(pas_) < 8:
        return False
    digit_flag = False
    letter_flag = False
    if pas_[0] == '+' or pas_[-1] == '+':
        for char in pas_:
            if char.isdigit():
                digit_flag = True
            if char.isalpha():
                letter_flag = True
        return digit_flag and letter_flag
    else:
        return False


print(valid_pas('+Qw78111fd')) #True
print(valid_pas('Qw78111fd+')) #False
print(valid_pas('er.!iku')) #False
print(valid_pas('eri3u')) #false

