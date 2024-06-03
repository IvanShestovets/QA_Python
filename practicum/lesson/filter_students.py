"""
Обработать списки словарей.
Напишите функцию filter_stundents которая будет принимать на себя список студентов в виде словарей и возвращает список имен студентов у которых средний балл выше 4

Условие:
каждый студент представлен в виде словаря с ключами name и grades
grades - список оценок(целые числа)
Если у студента нет оценок его средний балл равен 0
"""
stundents_list = [
    {'name': 'Иван', 'grades': [5, 4, 3, 5, 4]},
    {'name': 'Мария', 'grades': [3, 4, 5, 3]},
    {'name': 'Петр', 'grades': [5, 5, 5, 5, 5]},
    {'name': 'Анна', 'grades': [4, 4, 4, 5, 4]},
    {'name': 'Екатерина', 'grades': []}
]

def filter_students(stundents_list):
    filtered_students = []

    for student in stundents_list:
        name = student['name']
        grades = student.get('grades', [])
        if grades:
           avg_grade = sum(grades) / len(grades)
        else:
           avg_grade = 0

        if avg_grade > 4:
            filtered_students.append(name)
    return filtered_students
 
top_students = filter_students(stundents_list)
print(top_students)