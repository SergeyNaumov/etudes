from sqlalchemy import create_engine, insert
from models.blog import blog, metadata
engine = create_engine("mysql+pymysql://crm@localhost/crm")
#engine = create_engine('sqlite:///sqlite3.db')  # используя относительный путь
#engine = create_engine('sqlite:////path/to/sqlite3.db')  # абсолютный пут
engine.connect()
# ins=insert(blog).values(
#     post_title = 'Valeriy',
#     post_slug = 'Golyshkin',
#     content = 'Fortioneaks',
# )
# conn = engine.connect()
# r = conn.execute(ins)
#print(blog.columns)
#print(engine)
#import mysql.connector

metadata.create_all(engine)