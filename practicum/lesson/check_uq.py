"""
Написать функцию проверять списки на уникальность. 
Функция принимает на себя список и проверяет, 
все ли элементы в нем уникальны.
"""

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 1]

def check(list):
    unique_len = len(set(list))
    
    if unique_len == len(list):
        return True
    else:
        return False

# result1 = check(list1)
# result2 = check(list2)

print("list1:", check(list1))
print("list2:", check(list2))

