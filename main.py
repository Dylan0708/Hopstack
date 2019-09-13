import main_func
import mysql.connector
import getpass
from mysql.connector import Error

username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")

#connect to db, set cursor
try:
    db_con = mysql.connector.connect(host = 'localhost', database = 'hopstack', user = username, password = password)
except Error as e:
    print(e)

#main menu
main_func.cls()
print ('Hopstack Main Menu\n1. Inventory\n2. Recipes\n3. Shopping Lists\n4. Ingredients')
menu_select = input("Select a Menu: ")

if db_con is not None and db_con.is_connected():
    db_con.close()