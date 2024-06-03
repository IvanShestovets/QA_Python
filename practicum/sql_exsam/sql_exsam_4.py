# WHERE (name LIKE '%А%' OR  name LIKE '%Б%')


import pymysql
import pymysql.cursors
from main_config import host,user,password,db_name

try:
    connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
    )
    print('succsess')
    print('#' * 30)
    try:
        with connection.cursor() as cursor:
            #тут пишем запросы
            select_team = '''
            CREATE VIEW users_qwerty AS
            SELECT * 
            FROM user
            WHERE YEAR(reg_date) = 2018 AND
            name LIKE "А%" OR 
            name LIKE "Б%" OR 
            name LIKE "% А%" OR
            name LIKE "% Б%"
            '''

            cursor.execute(select_team)
            connection.commit()
        
            print("Представление создано успешно.")
                



###################################
    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)