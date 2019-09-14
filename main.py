import main_func

#log in
connect = main_func.login()

#main menu
main_func.cls()
print ("Hopstack Main Menu\n1. Inventory\n2. Recipes\n3. Shopping Lists\n4. Ingredients\n5. Log Out")
menu_select = input("Select a Menu: ")

if connect is not None and connect.is_connected():
    connect.close()