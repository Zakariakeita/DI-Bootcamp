from unicodedata import name
import psycopg2 
import psycopg2.extras

class MenuItem:
    
    def __init__(self,name,price):
        self.name=name
        self.price=price
        

    def save(self):
        connection = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='Menu')
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        sql=f"INSERT INTO menuItem(name,price) VALUES ('{self.name}',{self.price});"
        cursor.execute(sql)
        if( cursor.execute(sql)):
            print("saved sucefullly")  
        connection.commit()
        connection.close()

    def update(self,name,price):
        connection = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='Menu')
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        sql=f"UPDATE menuItem SET name='{name}',price={price} ;"
        cursor.execute(sql)
        if( cursor.execute(sql)):
            print("updated sucefullly")  
        connection.commit()
        connection.close()

    def delete(self):
        connection = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='Menu')
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        sql=f"DELETE FROM menuItem;"
        cursor.execute(sql)
        if( cursor.execute(sql)):
            print("Deleted sucefullly")  
        connection.commit()
        connection.close()

    def all():
        connection = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='Menu')
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        sql=f"SELECT * FROM menuItem;"
        cursor.execute(sql)
        results = cursor.fetchall()
        connection.close()
        return results

    def get_by_name(name):
        connection = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='Menu')
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        sql=f"SELECT * FROM menuItem WHERE name='{name}';"
        cursor.execute(sql)
        results = cursor.fetchall()
        if(len(results)==0):
            connection.close()
            return None

        connection.close()
        return results


item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuItem.get_by_name('Beef Stew')
for i in item2:
    print(i)

items = MenuItem.all()
for i in items:
    print(i)
    