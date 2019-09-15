import main_func

menu_select = '5' 

#main menu
def main_menu():
    main_func.cls()
    print ("Hopstack Main Menu\n\n1. Inventory\n2. Recipes\n3. Shopping Lists\n4. Ingredients\n5. Log Out\n6. Exit")
    select = input("Select a Menu: ")
    return select

#log in
while menu_select != '6':
    if menu_select == '5':
        main_func.cls()
        connect = main_func.login()
        menu_select = main_menu()

if connect is not None and connect.is_connected():
    connect.close()
 

