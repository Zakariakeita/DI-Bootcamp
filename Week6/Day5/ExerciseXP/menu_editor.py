from tokenize import Number
import Exercise
import psycopg2
import psycopg2.extras
def load_manager(name,price):
    
    return Exercise.MenuItem(name,price)


def show_user_menu(name,price):
    print("MENU \n")
    print("(a) Add an item")
    print("(d) Delete an item")
    print("(v) View the MENU ")
    print("(x) Exit")
    val=input("Enter a letter")

    if val=='a': 
        return load_manager(name,price).save()
    elif val=='d':
        return load_manager(name,price).delete()
    elif val == 'v':
        return load_manager(name,price).all()
    elif val=='x':
        return True

def add_item_to_menu():
    name=input("Enter your name")
    price=Number(input("Enter a price"))
    resultat=load_manager(name,price).save()
    if resultat:
        print("item was added successfully.")


def remove_item_from_menu(price):
    name=input("Enter your name")
    resultat=Exercise.MenuItem.delete()

    connection = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='Menu')
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    sql=f"DELETE FROM menuItem WHERE name='{name}';"
    cursor.execute(sql)
    connection.commit()
    if( cursor.execute(sql)):
        print("Deleted sucefullly")  
    else:
        print("error")
    connection.close()

def show_restaurant_menu(name,price) :
    show_user_menu(name,price)