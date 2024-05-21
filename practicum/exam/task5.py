"""
Викторина напишите программу с вопросами и ответами, 
с возможностью подсчета очков и отображения результатов.
"""
questions = {
    "Столица России?": "Москва",
    "Сколько месяцев в году?": "12",
    "Как зовут главного героя книги 'Мастер и Маргарита'?": "Воланд"
}

score = 0

print("Добро пожаловать в викторину!")
print("Ответьте на следующие вопросы:")

for question, correct_answer in questions.items():
    user_answer = input(f"{question} ")
    if user_answer.lower() == correct_answer.lower():
        print("Правильно!")
        score += 1
    else:
        print("Неправильно.")

print(f"Вы ответили правильно на {score} вопросов из {len(questions)}.")