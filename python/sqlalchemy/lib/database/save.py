from .error import print_error
from sqlalchemy import text, insert, update, Table

def save(self, **arg):
        table=arg.get('table','')
        values=arg.get('values','')
        #print(f"{table=}",isinstance(table,Table))
        #quit()

        if not(values):
            print_error(self, "save: не указан параметр values")
            return 

        if table=='':
            print_error(self, "save: не указан параметр table")
            return 



        #query = arg.get('query')
        #if not(query):
        #    print('Error: параметр qyery не указан',)
        if isinstance(table,Table):
            with self.engine.connect() as conn:
                #stmt = insert(table).values(values)
                r=conn.execute(insert(table).values(values))
                conn.commit()
                return r

        elif isinstance(table,str):
            with self.engine.connect() as conn:
                #stmt = insert(table).values(values)
                values_str=''
                for name in values:
                    if values_str:
                        values_str+=', '
                    values_str+=f"{name} = '{values[name]}'"

               
                stmt = f"INSERT INTO {table} {values_str}"

                try:
                    conn.execute(text(stmt))
                    conn.commit()
                except Exception as e:
                    print_error(self,f"save: произошла ошибка при выполнении запроса: {e}")

        else:
            print_error("save: параметр table должен быть Объектом sqlalchemy.Table или строкой")
            return 