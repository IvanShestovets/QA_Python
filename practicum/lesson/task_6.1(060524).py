"""
Задача 1:
Расчет стоимости покупки в магазине с учетом скидки. Предположим у нас есть 
два списка, в первом список продуктов, во втором стоимость этих самых 
продуктов(произвольно) Вам надо рассчитать общую стоимость покупки с учетом 
скидки, если сумма покупки превышает определенную сумму(произвольно) то 
предоставляется скидка
"""
sum_to_sale = 1000

products = ['яблоки','груши','веники','угли','мясо']
prices = [100,200,300,400,500]

total_price = sum(prices)

# Рассчет общей стоимости с учетом скидки
if total_price > sum_to_sale:
    discount = total_price * 0.1  # 10% скидка
    total_price_with_discount = total_price - discount
else:
    total_price_with_discount = total_price

print(total_price_with_discount)


'''2'''

text = """
There are many variants of Lorem Ipsum, but most of them do not always have 
acceptable modifications, for example, humorous inserts or words that do not 
even remotely resemble Latin. If you need Lorem Ipsum for a serious project, 
you probably don't want some joke hidden in the middle of a paragraph. Also, 
all other well-known Lorem Ipsum generators use the same text, which they 
simply repeat until they reach the desired volume.
"""

#разбиваю текст на слова
words = text.split()

#создаю 2 пустых списка для хранения слов и их частоты
uniq_words = []
words_count = []

#подсчитывает частоту встречаемости каждого слова
for word in words:
    #убирает знаки препинания
    word = word.strip(',.').lower()


    #если слово уже есть в списке, увеличиваю его счетчик
    if word in uniq_words:
        index = uniq_words.index(word)
        words_count[index] += 1
    #если слово встречается впервые, добавляем в список
    else:
        uniq_words.append(word)
        words_count.append(1)
#найти наиболее часто встречающееся слово
max_count = max(words_count)
most_common_word = uniq_words[words_count.index(max_count)]

#вывод
print(f'Наиболее часто встречающеся слово: {most_common_word} встречается {max_count} раз')
