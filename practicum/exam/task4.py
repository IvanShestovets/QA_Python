"""
Напишите программу которая будет находить слово в строке.
"""

with open('Hello.txt', 'r', encoding="utf-8") as file:
    word = input('Введите искомое слово: ')
    # word = "Рэдрик"
    words = file.read().split()
    
    if word in words:
        print(f"Слово '{word}' найдено в тексте файла.")