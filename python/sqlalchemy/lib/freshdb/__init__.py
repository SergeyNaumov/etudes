from ..database import engine
from sqlalchemy import text

def query(**arg):
    print('arg: ',arg)
    if 'query' in arg:
        query = arg['query']
        print('query: ',query)
        async with engine.connect() as conn:
            res = conn.execute(text(query))
            return res.all()   
            #return res.fetchall()   

    #with engine.connect() as conn:
    #    result = conn.execute(text("SELECT * FROM user limit 1"))
    #    pprint(result.all())