from .md_obj import md_obj
from sqlalchemy import Table, Column, Integer, String, MetaData

table=Table(
    "manager",
    md_obj,
    Column("id", Integer, primary_key=True),
    Column("name",String(50)),
    Column("phone",String(50)),
)