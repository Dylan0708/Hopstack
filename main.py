import main_func, ingredients

def login():
    main_func.cls()
    username = 'root' #input("Enter Username: ")
    password = 'StupidSexyFlanders' #main_func.echo_char("Enter Password: ")
    con = main_func.hstack_connect(username, password)
    main_menu(con)

#main menu
def main_menu(connection):
    loop = True
    
    while loop == True:
        main_func.cls()
        print ("Hopstack Main Menu\n\n1. Inventory\n2. Recipes\n3. Shopping Lists\n4. Ingredients\n5. Log Out\n6. Exit")
        select = input("Select Menu: ")

        if select == '4':
            ingredients.ingredient_list(connection)
        elif select == '5':
            if connection != None and connection.is_connected():
                connection.close()
            main_func.cls()
            login()
        elif select == '6':
            if connection != None and connection.is_connected():
                connection.close()
            main_func.cls()
            raise SystemExit
        else:
            print("Invalid Input - ", end = '')

login()