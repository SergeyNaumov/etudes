# https://habr.com/ru/post/322086/
# Импортируем библиотеку, соответствующую типу нашей базы данных 
# В данном случае импортируем все ее содержимое, чтобы при обращении не писать каждый раз имя библиотеки, как мы делали в первой статье
"""
Проблема: не смог выставить кодировку utf8 для таблицы в default charset
"""
from peewee import *

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы

#conn = SqliteDatabase('Chinook_Sqlite.sqlite')
conn = MySQLDatabase('crm',user='crm',password='',host='localhost',port=3306,charset='utf8')

# Определяем базовую модель о которой будут наследоваться остальные
class BaseModel(Model):
    class Meta:
        database = conn  # соединение с базой, из шаблона выше

# Определяем модель исполнителя
class Test(BaseModel):
    id = AutoField(column_name='id')
    name = TextField(column_name='name', null=True)
    email = TextField(column_name='email', null=True)
    class Meta:
        table_name = 'testorm'
        table_settings = ['ENGINE=InnoDB', 'DEFAULT CHARSET=utf8','comment="тестовая таблица"']
        #default_charset='utf8'

def print_last_five_records():
    #""" Печатаем последние 5 записей в таблице исполнителей"""
    #print('########################################################')
    cur_query = Test.select().limit(5).order_by(Test.id.desc())
    for item in cur_query.dicts().execute():
        print('manager: ', item)

Test.create_table()

print_last_five_records()

#print(Manager.id)
#query = Manager.select().where(Manager.id < 10).limit(5).order_by(Manager.id.desc())
#print(query)
quit()
