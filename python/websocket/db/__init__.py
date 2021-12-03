# from peewee import *
 
# user = 'crm'
# password = ''
# db_name = 'crm'
 
# dbhandle = MySQLDatabase(
#     db_name, user=user,
#     password=password,
#     host='localhost'
# )

# class BaseModel(Model):
#     class Meta:
#         database = dbhandle

from .freshdb import FreshDB
from config import config
#def connect():
#  return FreshDB(dbname='crm',user='crm')


connect=config['connect']


print(connect)
db=FreshDB(
  dbname=connect['dbname'],
  user=connect['user'],
  password=connect['password'],
  host=connect['host'],
)

db.query(query="set sql_mode=''")



