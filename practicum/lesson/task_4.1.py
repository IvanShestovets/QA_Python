winter = ['декабрь', 'январь', 'февраль']
spring = ['март', 'апрель', 'май']
summer = ['июнь', 'июль', 'август']
authem = ['сентябрь', 'октябрь', 'ноябрь']

mounth = input('Введите название месяца: ')

if mounth in winter:
    print('зима')
elif mounth in spring:
    print('весна')
elif mounth in summer:
    print('лето')
elif mounth in authem:
    print('осень')
else:
    print('ошибка ввода данных')


