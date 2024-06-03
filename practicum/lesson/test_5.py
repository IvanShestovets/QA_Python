hero_choice = None
temporarily_choice = None
one_skill = 1

strength_hero = 0
agility_hero = 0
wisdom_hero = 0
health_hero = 0

list_params = [1] * 10
main_list_navikov = list(list_params)
ostalos_navikov = len(main_list_navikov)

def skills_of_hero():
    print("\n\n Осталось очков навыков:", ostalos_navikov)
    print("\nУровень Силы героя/героини:", strength_hero)
    print("Уровень Здоровья героя/героини:", health_hero)
    print("Уровень Мудрости героя/героини:", wisdom_hero)
    print("Уровень Ловкости героя/героини:", agility_hero)

def exit_choice():
    print("\n Получился герой/героиня с такими навыками: ")
    skills_of_hero()
    input("\n\tНажмите Enter для выхода")
    exit()

def make_hero(hero_choice):
    global temporarily_choice
    global strength_hero
    global health_hero
    global wisdom_hero
    global agility_hero

    print("\n Вы выбрали:", hero_choice , "сей выбор приемлем.")

    if hero_choice == 1:
        temporarily_choice = strength_hero
        vivod = "Сила"
    elif hero_choice == 2:
        temporarily_choice = health_hero
        vivod = "Здоровье"
    elif hero_choice == 3:
        temporarily_choice = wisdom_hero
        vivod = "Мудрость"
    elif hero_choice == 4:
        temporarily_choice = agility_hero
        vivod = "Ловкость"

    print("\n Выбор:", hero_choice , "означает:", vivod)
    plus_or_minus_skill = input("Введите знак без кавычек. Вы хотите прибавить '+' или убавить '-' параметр: ")

    if plus_or_minus_skill not in ("+", "-"):
        print("\n Введён не '+' или '-' Выходим.")
        exit_choice()

    if plus_or_minus_skill == '+':
        if one_skill in main_list_navikov:
            temporarily_choice += 1
            main_list_navikov.remove(one_skill)
        else:
            print("\n Похоже, навыки закончились/все распределены.")
    else:
        if temporarily_choice != 0:
            temporarily_choice -= 1
            main_list_navikov.append(one_skill)
        else:
            print("\n Нельзя уменьшить! Навык и так слишком мал!")

    if hero_choice == 1:
        strength_hero = temporarily_choice
        return(strength_hero)

    elif hero_choice == 2:
        health_hero = temporarily_choice
        return(health_hero)

    elif hero_choice == 3:
        wisdom_hero = temporarily_choice
        return(wisdom_hero)

    elif hero_choice == 4:
        agility_hero = temporarily_choice
        return(agility_hero)

print('''
Программа создания персонажа RPG.
У вас есть 10 пунктов навыков, распределите их между параметрами: Здоровье, Сила, Мудрость, Ловкость.
''')

while hero_choice != 0:
    print("\n\n Текущее количество очков навыков: ", ostalos_navikov)

    print('''
    Таблица выбора:
                1 - Добавить/убавить Силу.
                2 - Добавить/убавить Здоровье.
                3 - Добавить/убавить Мудрость.
                4 - Добавить/убавить Ловкость.
                    0 - Выход из меню.
''')

    hero_choice = int(input("Выберете один из вышеозначенных пунктов: "))
    if hero_choice not in range(5):
        print("\n Колдунство не сработало! Попробуйте ещё раз...")
        continue
    exit_choice() if hero_choice == 0 else make_hero(hero_choice)

    ostalos_navikov = len(main_list_navikov)
    skills_of_hero()