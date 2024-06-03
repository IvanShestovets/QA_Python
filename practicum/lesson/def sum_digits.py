"""
Напишите функцию, которая принимает на себя целое число 
и возвращает сумму его цифр.
"""
#num = int(input('Введите число:'))
    
def sum_digits(num):
    num_str = str(num)    
    digit_sum = 0
    
    for digit in num_str:
        digit_sum += int(digit)

    return digit_sum

print(sum_digits(123))
