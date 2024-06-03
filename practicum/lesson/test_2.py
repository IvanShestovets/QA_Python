"""
Генератор случайной фразы из файла.
Напишите функцию, которая будет генерировать случайные фразы 
взятые из файла 
"""
import random

def random_generet():
    with open('Hello.txt','r', encoding="utf-8") as file:
        lines = file.readlines()

        random_line = random.choice(lines).strip()

    print(random_line)

random_generet()