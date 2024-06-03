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
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS `students`(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age INT NOT NULL
            );
            '''
            cursor.execute(create_table_query)
            print('table students created')


            #заполняю таблицу
            insert_query = '''
            INSERT INTO `students` (name,email,age) VALUES
            ('Иванов Иван', 'ivanov@example.com', 25),
            ('Петров Петр', 'petrov@example.com', 22),
            ('Сидорова Мария', 'sidorova@example.com', 20),
            ('Козлов Алексей', 'kozlov@example.com', 23),
            ('Смирнова Екатерина', 'smirnova@example.com', 24),
            ('Никитин Никита', 'nikitin@example.com', 21),
            ('Ковалева Ольга', 'kovaleva@example.com', 26),
            ('Иванова Анна', 'ivanova@example.com', 22),
            ('Соколов Павел', 'sokolov@example.com', 27),
            ('Морозова Дарья', 'morozova@example.com', 23);
            '''
            cursor.execute(insert_query)
            connection.commit() # инсерб гбдейбю делит
            print('data inserted')

    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)