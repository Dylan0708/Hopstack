import main_func
import ingredients_func

def ingredient_list(connection):
    db_cursor = connection.cursor(buffered = True)
    loop = True

    while loop == True:
        main_func.cls()
        print("Ingredients\n\n1. Hops\n2. Yeast\n3. Fermentables & Adjuncts\n4. Water\n5. Miscellaneous\n6. All\n7. Search\n8. Main Menu")
        filter_select = input("Select Filter: ")

        if filter_select == '1':
            main_func.cls()
            ingredients_func.hop_list(db_cursor)
        elif filter_select == '8':
            db_cursor.close()
            main_func.cls()
            return
        else:
            print("Invalid Input - ", end = '')




"""conn = main_func.hstack_connect('root', 'StupidSexyFlanders')
cursor = conn.cursor(buffered = True)
cursor.execute("SELECT * FROM yeast")

row = cursor.fetchone()

print(row)

cursor.close()
conn.close()"""
