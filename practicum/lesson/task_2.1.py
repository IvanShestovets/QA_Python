"""
Задача сложная: Напишите функцию которая будет принимать 
две строки и возвращать True если они будут является 
анаграммами друг друга и False в противном случае
"""

str1 = input("Введите фразу 1:")
str2 = input("Введите фразу 2:")

def anagrams(str1, str2):

    return sorted(str1) == sorted(str2)

if anagrams(str1, str2):
    result = True
else:
    result = False

print(result)
 

