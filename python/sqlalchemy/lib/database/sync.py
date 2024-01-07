from sqlalchemy import create_engine, text, insert, Table
from sqlalchemy.orm import Session, sessionmaker

from config import settings
from .save import save
#from sqlalchemy import URL, create_engine, text

def get_engine(**arg):  
    echo = arg.get('echo', False)
    engine = create_engine(
        url=settings.DATABASE_URL_syncmysql,
        echo=echo,
        pool_size=5,
        max_overflow=10
    )
    return engine





class Engine:
    def __init__(self, **arg):
        self.engine = get_engine(**arg)

    

    def save(self, **arg):
        return save(self, **arg)


