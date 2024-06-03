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
            SELECT * FROM team WHERE members_count > 5
            '''

            cursor.execute(select_team)
            result = cursor.fetchall()

            if len(result) > 0:
                for row in result:
                    print(row)
            else:
                print("Нет строк с количеством участников выше 5.")
                



###################################
    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)