
# https://digitalstudium.com/ru/python-programming/how-to-create-a-simple-asynchronous-api-in-python-using-aiohttp-and-tortoise-orm/
from aiohttp import web
#from tortoise import Model, fields
from tortoise.contrib.aiohttp import register_tortoise
app = web.Application()

register_tortoise(
    #app, db_url=f"mysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:3306/{DATABASE_NAME}",
    app, db_url=f"mysql://crm:@localhost:3306/crm",
    modules={"models": ["models"]},
    generate_schemas=True
)