"""
Напишите программу которая эмулирует телефонную книгу, то есть хранит 
информацию  о контактах(имя, номер телефона) по запросу можно вывести 
всю книгу разом по умолчанию запрашивает данные и сохраняет в книгу.
"""
phone_book = [
    {'name': 'Иван', 'phone': '+79001101010'},
    {'name': 'Мария', 'phone': '+79001105010'},
    {'name': 'Петр', 'phone': '+79001101310'},
    {'name': 'Анна', 'phone': '+79001101020'},
    {'name': 'Екатерина', 'phone': '+79001101011'}
]

def view_contacts():
    if not phone_book:
        print("Телефонная книга пуста.")
    else:
        print("Телефонная книга:")
        for contact in phone_book:
            print(f"{contact['name']}: {contact['phone']}")

def add_contact():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    new_contact = {'name': name, 'phone': phone}
    phone_book.append(new_contact)
    print(f"Контакт '{name}' успешно добавлен.")

while True:
    choice = input("Выберите действие (1 - просмотреть контакты, 2 - добавить контакт, 3 - выход): ")

    if choice == "1":
        view_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор, попробуйте снова.")