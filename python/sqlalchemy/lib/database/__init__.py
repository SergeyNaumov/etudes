# pip install async-sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from config import settings

from pprint import pprint
pprint(settings)

# sync_engine = create_engine(
#     url=settings.DATABASE_URL_syncmysql,
#     echo=False,
#     pool_size=5,
#     max_overflow=10
# )
def get_engine(**arg):
    async_connection = arg.get('async_connection', False)
    echo = arg.get('echo', False)
    if async_connection:

        engine = create_async_engine(
            url=settings.DATABASE_URL_asyncmysql,
            echo=echo,
            # pool_size=5,
            # max_overflow=10
        )
    else:

        engine = create_engine(
            url=settings.DATABASE_URL_syncmysql,
            echo=echo,
            pool_size=5,
            max_overflow=10
        )
    return engine


# На этом этапе подключения ещё нет



