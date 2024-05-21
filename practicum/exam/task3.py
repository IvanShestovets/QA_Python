"""
Напишите калькулятор на простые действия  +-*/
"""

num1 = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))
operator = input('Введите действие +-*/: ')

def calc(operator, num1, num2):
    try:
        if operator =='+':
            return  num1+num2
        elif operator == '-':
            return  num1-num2
        elif operator == '*':
            return  num1*num2
        elif operator == '/':
            if num2 != 0:
                return  num1/num2
            else:
                return "Ошибка: Деление на ноль"
        else:
            return "Неверная операция"
    except ZeroDivisionError:
        return print('на ноль делить нельзя')
    except ValueError:
        return print('неверная операция')

result = calc(operator, num1, num2)

print(result)

