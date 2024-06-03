"""
Написать программу генератор случайных шуток на основе шаблонов. 
У вас будет список шаблонов для шуток, где вы можете использовать 
различные элементы для подстановки.через f строку например:

Почему {} перешел дорогу.
"""
import random

joke_template = [
    'Почему {} катится вниз?',
    'Потому что {} смеятся над ним!',
    'Кто {} в книгах?',
    'Кто {}?',
    'Что сказал {} ему {} когда они встретились ?'
]
joke_elements = [
    'слон','заяц','бетмен','крокодил','чебурашка','студент','препод',
    'водитель','улитка']

def generate_random_joke():
    template = random.choice(joke_template)

    num_elements = template.count('{}')
    elements = random.sample(joke_elements, num_elements)
    joke = template.format(*elements)

    return joke

random_joke = generate_random_joke()
print(random_joke)

generate_random_joke()