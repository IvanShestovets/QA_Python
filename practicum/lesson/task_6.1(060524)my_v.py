
'''
Задача 2:
Поиск наиболее часто встречающегося слова в тексте.
У нас есть текст:

Знаки препинания можно убрать как я показывал ранее с текстом через import re
Или использовать команду метод strip()
внутри цикла for 
word = word.strip(“,.”).lower()
'''
import re

text = """
There are many variants of Lorem Ipsum, but most of them do not always have 
acceptable modifications, for example, humorous inserts or words that do not 
even remotely resemble Latin. If you need Lorem Ipsum for a serious project, 
you probably don't want some joke hidden in the middle of a paragraph. Also, 
all other well-known Lorem Ipsum generators use the same text, which they 
simply repeat until they reach the desired volume.
"""

text_without_punctuation = re.sub(r'[^\w\s]', '', text)
print(text_without_punctuation)

words = text_without_punctuation.lower().split()

word_count = {}
for word in words:
    if word in word_count:
       word_count[word] += 1
    else:
        word_count[word] = 1

most_common_word = max(word_count)

print("Наиболее часто встречающееся слово: ", most_common_word)
