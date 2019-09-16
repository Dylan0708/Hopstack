import main_func
from hstack_classes import Hop, Yeast, Ferm, Water, Misc

def ingredient_list(connection):
    db_cursor = connection.cursor()
    filter_select = None

    main_func.cls()
    print("Ingredients\n\n1. Hops\n2. Yeast\n3. Fermentables & Adjuncts\n4. Water\n5. Miscellaneous\n6. All\n7. Search\n8. Main Menu")
    filter_select = input("Select Filter: ")

    if filter_select == '8':
        return




"""conn = main_func.hstack_connect('root', 'StupidSexyFlanders')
cursor = conn.cursor(buffered = True)
cursor.execute("SELECT * FROM yeast")

row = cursor.fetchone()

print(row)

cursor.close()
conn.close()"""
