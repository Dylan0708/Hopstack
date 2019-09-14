import os
import sys
import mysql.connector
import getpass
import readchar
from mysql.connector import Error

#Connect to db, and set cursor
def hstack_connect(u_name, p_word):
    try:
        db_con = mysql.connector.connect(host = 'localhost', database = 'hopstack', user = u_name, password = p_word) #attempt db connection
    except Error as e:
        print(e) #if connection fails, print error
    if db_con.is_connected():
        return db_con #if connected, return connection
    else:
        sys.exit("Couldn't Connect") #exit

#Clear screen function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def dot_echo():
    pass_list = []
    key_stroke = readchar.readkey()
    while key_stroke != readchar.key.ENTER:
        pass_list.append(key_stroke)
        sys.stdout.write('.')
        key_stroke = readchar.readkey()
    secret = ''.join(pass_list)
    return secret

stuff = dot_echo()
print(stuff)
