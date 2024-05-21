"""
Напишите функцию которая принимает список чисел  и возвращает новый список, 
содержащий только те числа которые делятся на 3.
"""

def dig_tree(numbers):
 
    list = []
    for num in numbers:
        if num % 3 == 0:
            list.append(num)
    return list

print(dig_tree([3, 5, 9, 10, 12, 21, 15]))
