import main_func

username = input("Enter Username: ")
password = main_func.getpass.getpass("Enter Password: ")

#establish db connection
con = main_func.hstack_connect(username, password)
#main menu
#main_func.cls()
#print ("Hopstack Main Menu\n1. Inventory\n2. Recipes\n3. Shopping Lists\n4. Ingredients\n5. Log Out")
#menu_select = input("Select a Menu: ")

if con is not None and con.is_connected():
    con.close()