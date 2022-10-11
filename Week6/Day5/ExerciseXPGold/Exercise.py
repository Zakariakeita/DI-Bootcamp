
import psycopg2 
import psycopg2.extras
import hashlib

users={'SANOU':'sanou12','TRAORE':'tr@45','BOLY':'bhjkd'}

connection = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='Menu')
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
sql="CREATE TABLE users(id SERIAL PRIMARY KEY,name Varchar(50),password Varchar(200));"
cursor.execute(sql) 
connection.commit()

for i, j in users.items():
    pwd=hashlib.md5(j.encode('utf-8')).hexdigest()
    sql1=f"INSERT INTO users(name,password) VALUES ('{i}','{pwd}');"
    cursor.execute(sql1) 
    connection.commit()
connection.close()

