# https://habr.com/ru/post/322086/
# Импортируем библиотеку, соответствующую типу нашей базы данных 
# В данном случае импортируем все ее содержимое, чтобы при обращении не писать каждый раз имя библиотеки, как мы делали в первой статье
from peewee import *

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы

#conn = SqliteDatabase('Chinook_Sqlite.sqlite')
conn = MySQLDatabase('crm',user='crm',password='',host='localhost',port=3306)

# ТУТ БУДЕТ КОД НАШИХ МОДЕЛЕЙ

# Создаем курсор - специальный объект для запросов и получения данных с базы
cursor = conn.cursor()
cursor.execute("select * from manager limit 10")
results = cursor.fetchall()
for m in results:
    print(m['name'])
#print(results)
# ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ

# Не забываем закрыть соединение с базой данных
conn.close()