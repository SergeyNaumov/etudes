# https://pythonbasics.org/flask-sqlalchemy/
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask (__name__)
#app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://crm:@localhost/crm?charset=utf8'
# engine = create_engine("mysql+pymysql://crm:pass@some_mariadb/dbname?charset=utf8mb4")
#engine = create_engine("mysql+pymysql://crm:@localhost/crm?charset=utf8")
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)
print(db)

class Managers(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))



@app.route('/')
def main_page():
    return 'hello!'

if __name__ == '__main__':
   #db.create_all()
   app.run(debug = False)