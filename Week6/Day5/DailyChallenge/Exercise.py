
import psycopg2 
import psycopg2.extras
import requests
import random


def get_jokes():
    for i in range(10):
        r=random.randint(0, 250)
        url = 'https://restcountries.com/v3.1/all'
        data = requests.get(url)
        name=data.json()[r]["name"]["common"]
        capital=data.json()[r]["capital"][0]
        flag=data.json()[r]["flag"]
        subregion=data.json()[r]["subregion"]
        pop=data.json()[r]["population"]

        
        connection = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='Menu')
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        sql=f"INSERT INTO country(name,capital,flag,subregion,population) VALUES ('{name}','{capital}','{flag}','{subregion}','{pop}');"
        cursor.execute(sql) 
        connection.commit()
        connection.close()

        

get_jokes()