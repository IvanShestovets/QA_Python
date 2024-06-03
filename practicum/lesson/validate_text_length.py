"""
Напишите функцию, validate_text_length которая принимает на себя текст и 
максимальную длину текста  и возвращает True если длина текста не превышает 
максимальную и false в противном случае.
"""

def validate_text_length():
    text = input('Введие текст: ')
    len_text = int(input('количество символов: '))

    for i in text:
        if len(text) <= len_text:
            return False
        else:
            return True

print(validate_text_length())