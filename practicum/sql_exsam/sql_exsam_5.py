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
            create_view_query = ''' 
            CREATE VIEW tea_without_icetea AS
            SELECT * 
            FROM good
            WHERE name NOT LIKE '%Айс Ти%'
            '''
            cursor.execute(create_view_query)
            connection.commit()
            
            print("Представление 'tea_without_icetea' создано успешно.")
            
            # Выбор и изменение названий, стоимости и количества для выборочных 20 позиций
            update_query = ''' 
            UPDATE tea_without_icetea
            SET name = 'Новое', count = 100, price = 50
            LIMIT 20
            '''
            cursor.execute(update_query)
            connection.commit()
            
            print("Выборочные 20 позиций в представлении изменены успешно.")
            
            # Запрос для выборки измененных данных после обновления
            select_query = ''' 
            SELECT * FROM tea_without_icetea
            LIMIT 20
            '''
            cursor.execute(select_query)
            result = cursor.fetchall()
            
            if len(result) > 0:
                for row in result:
                    print(row)
            else:
                print("Нет данных для отображения.")

###################################
    except Exception as e:
        print('An error ')
        print(e)        
        
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)