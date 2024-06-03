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
            insert_query = "INSERT INTO good (id, category_id, name, count, price) VALUES (null, 12, 't', 757, 500)"
            # record_to_insert = ('value1', 'value2', 'value3')
            cursor.execute(insert_query) # record_to_insert
            connection.commit()
            print('new')


            check_record_query = "SELECT * FROM good WHERE name = 't'"
            cursor.execute(check_record_query)
            result = cursor.fetchone()

        if result:
            print("Запись добавлена в таблицу good'.")
        else:
            print("Ошибка.")



###################################
    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)