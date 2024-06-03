"""
Подсчет частоты слов в тексте

Написать функцию word_frequency  которая принимает на себя строку и возвращает 
словарь в котором ключ это слово из строки, а значение - количество 
вхождений(повторений). При этом слова не должны учитывать регистр то есть Hello 
и hello должны быть 1 словом а не 2)
"""
def word_frequency(text):
    words = text.lower().split()
    frequency = {}
  
    for word in words:
        word = word.strip('.,!?')
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

text = 'Hello, hello World world, Подсчет частоты слов в тексте'

result = word_frequency(text)
print(result)
