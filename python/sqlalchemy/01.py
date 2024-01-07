#from lib.freshdb import query
#from pprint import pprint
#v=query(query="select count(*) from user")
#pprint(v)
import asyncio
from lib.database import get_engine

from sqlalchemy import text




async def db_query(engine, query):
    async with engine.connect() as conn:
        res = await conn.execute(text(query))
        print(f'{res.all()=}')
        await conn.commit()
        #quit()
        #return res.all()   
    #return res.fetchall()  

engine=get_engine(True)
if (__name__ == '__main__'):
    asyncio.run(
        db_query(engine, "select count(*) from user")
    )