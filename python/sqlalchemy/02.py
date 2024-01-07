from sqlalchemy import text
from lib.database.sync import Engine
from models.md_obj import md_obj
from models.user import table as user_table
from models.manager import table as manager_table

db=Engine(
    echo=True
)
 
def recreate_tables():
    md_obj.drop_all(db.engine)
    md_obj.create_all(db.engine)

#recreate_tables()
r=db.save(
    table=user_table,
    #table='user',
    values={
        'name': 'Вася'
        
    }
)
print('r:',r)



