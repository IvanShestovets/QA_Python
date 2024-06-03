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
            insert_team = '''
            INSERT INTO `team` (id,team_name,members_count) VALUES
            ('1','epic',3),
            ('2','Lord',5),
            ('3','Holy',7),
            ('4','Moli',9),
            ('5','SPb',8),
            ('6','Python',8),
            ('7','Wolf',8),
            ('8','Buls',8),
            ('9','Stupid',8),
            ('10','com',8);
            '''
            cursor.execute(insert_team)
            connection.commit()
            print('data inserted')



###################################
    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)