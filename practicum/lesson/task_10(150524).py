"""
Напишите программу которая будет запрашивать у пользователя 2 числа(внести в 
переменные через ввод с клавиатуры) и выводит результат деления первого числа 
на второе. Обработайте ошибку деления на 0 с помощью try-except
"""

try:
    num_1 = int(input('Ведите первое число: '))
    num_2 = int(input('Ведите второе число: '))

    result = num_1 / num_2
    print(result)
except ValueError:
    print('Введено неверное значение. Введите число.')
except ZeroDivisionError:
    print('На ноль делить нельзя.')


"""
Напишите программу, которая открывает файл и выводит его содержимое. 
Обработайте исключение открытия файла с помощью try-except
"""

try:

    with open('Hello.txt','r',encoding='utf-8') as file:
        print(file.read())

except FileNotFoundError:
    print('Фаил не найден.')


"""
Написать 2 функции: 
Одна функция находит сумму всех чисел в списке и возвращает значение. 
Другая функция должна принять на себя результат первой функции и выполнить 
деление на введенное число пользователем. Дополнительно необходимо выполнить 
обработку исключения при делении на 0
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]
divisor = int(input("Введите число: "))

def find_sum(numbers):
    sum_numbers = sum(numbers)
    return sum_numbers

def div_sum(sum_numbers, divisor):
    try:
        result = sum_numbers / divisor
        return result
    except ZeroDivisionError:
        return "На ноль делить нельзя."

sum_numbers = find_sum(numbers)
result = div_sum(sum_numbers, divisor)
print(f"Результат деления: {result}")


"""
Написать функцию count_letters() которая принимает на вход строку и 
подсчитывает количество букв в этой строке. Функция должна вернуть 
словарь  где ключами будут буквы, а значениями - их количество в строке. 
Пробелы и знаки препинания не учитываются.
"""
text = input('Ввод: ')

def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

result = count_letters(text)
print(result)


"""
Написать функцию, которая будет принимать на себя список оценок. 
и затем будет проводить расчет, по возврату средней оценки
[6,7,9,6,10]
"""

list = [6, 7, 9, 6, 10]

def average(q):
    average = sum(q) / len(q)
    print(average)

average(list)