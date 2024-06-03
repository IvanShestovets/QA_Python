"""
Закинуть его в файл (на рабочем столе или в папке на выбор) и вывести:

Весь текст
Каждую 2 строчку текста
Найти слово Редрик в тексте
"""



#file = open('Hello.txt','r', encoding="utf-8")
# desktop = open(r'C:\Users\AttekPC\Desktop\qwe.txt', 'r') 


# with open('Hello.txt','r', encoding="utf-8") as file:
#      lines = file.readlines()

# for i in range(1, len(lines), 2):

#     print(lines[i].strip()) 


with open('Hello.txt', 'r', encoding="utf-8") as file:
    word = "Рэдрик"
    words = file.read().split()
    
    if word in words:
        print(f"Слово '{word}' найдено в тексте файла.")



print(file.read())
# print(desktop.read())


"""

"""

numbers = [1, 2, 3, 24, 5, 6]

def max_num(i):
    max_number = max(numbers)
    return max_number

result = max_num(numbers)
print(result)
