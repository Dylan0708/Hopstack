import mysql.connector
import getpass
from mysql.connector import Error

#Log In Variables
#username
#password

username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")

#connect to db, set cursor
try:
    db_con = mysql.connector.connect(host = 'localhost', database = 'hopstack', user = username, password = password)
    if db_con.is_connected():
        print('Connected to hopstack') 
except Error as e:
    print(e)

if db_con is not None and db_con.is_connected():
    db_con.close()