import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Подключение к существующей базе данных
connection = psycopg2.connect(user="postgres",
                              # пароль, который указали при установке PostgreSQL
                              password="1111",
                              host="127.0.0.1",
                              port="5432")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# Курсор для выполнения операций с базой данных
print('Получен курсор из БД')
cursor = connection.cursor()




def select_all_from_bd():
    try:
        sql_select_all = 'SELECT * FROM orders_db'
        cursor.execute(sql_select_all)

    except (Exception, Error) as error:
       print("Ошибка при работе с PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")