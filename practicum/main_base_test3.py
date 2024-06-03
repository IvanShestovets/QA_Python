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
            insert_into_q = 'UPDATE `good` SET `count` = 35 WHERE `name` ="new_good";'
            cursor.execute(insert_into_q)
            connection.commit()
            print('record update')


            check_query = 'SELECT * FROM `good` WHERE name = "new_good" AND `count` = 35;'
            cursor.execute(check_query)
            result = cursor.fetchone()
            if result:
               print('good')
            else:
               print('not good')




###################################
    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)