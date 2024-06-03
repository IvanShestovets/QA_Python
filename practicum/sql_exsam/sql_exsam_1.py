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
            new_table_team = '''
            CREATE TABLE team (
            id INT PRIMARY KEY,
            team_name VARCHAR(255),
            members_count INT CHECK (members_count <= 10)
        )'''
            cursor.execute(new_table_team)
            connection.commit()
        
            print("Таблица 'team' успешно создана.")


    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)