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

def add_contact(name, phone_number):
    new_contact = {'name': name, 'phone': phone_number}
    phone_book.append(new_contact)
    print(f"Контакт {name} с номером {phone_number} был успешно добавлен в телефонную книгу.")

def show_phone_book():
    if phone_book:
        print("Телефонная книга:")
        for contact in phone_book:
            print(f"Имя: {contact['name']}, Номер телефона: {contact['phone']}")
    else:
        print("Телефонная книга пуста.")

# По умолчанию запрашиваем данные и выводим имеющиеся контакты
while True:
    choice = input("Введите 1 для добавления контакта, 2 для просмотра телефонной книги, или exit для выхода: ")
    
    if choice == '1':
        name = input("Введите имя контакта: ")
        phone_number = input("Введите номер телефона: ")
        add_contact(name, phone_number)
    elif choice == '2':
        show_phone_book()
    elif choice.lower() == 'exit':
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
