
"""
Викторина. Напишите программу с вопросами и ответами, 
с возможностью подсчета очков и отображения результатов.
"""
questions = [
    {
        "question": "Какая планета ближе всего к Солнцу?",
        "options": ["Меркурий", "Венера", "Марс", "Юпитер"],
        "answer": "Меркурий"
    },
    {
        "question": "Какой самый большой океан на Земле?",
        "options": ["Атлантический", "Тихий", "Индийский", "Северный Ледовитый"],
        "answer": "Тихий"
    },
    {
        "question": "Какой язык программирования был создан первым?",
        "options": ["Python", "Fortran", "C++", "Java"],
        "answer": "Fortran"
    },
    {
        "question": "Какое животное является символом России?",
        "options": ["Кенгуру", "Утконос", "Медведь", "Ехидна"],
        "answer": "Медведь"
    },
    {
        "question": "Какая валюта используется в Японии?",
        "options": ["Иена", "Юань", "Вона", "Доллар"],
        "answer": "Иена"
    }
]

score = 0

print("Добро пожаловать в викторину!")
print("Ответьте на следующие вопросы. За каждый правильный ответ вы получите 1 очко.")

for question in questions:
    print("\n" + question["question"])
    options = question["options"]
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_answer = input("Введите номер ответа: ")

    if options[int(user_answer) - 1] == question["answer"]:
        print("Правильно!")
        score += 1
    else:
        print(f"Неверно. Правильный ответ: {question['answer']}")

print(f"\nВикторина завершена. Ваш результат: {score}/{len(questions)} очков.")