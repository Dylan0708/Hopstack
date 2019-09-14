import os
import sys
import mysql.connector
import getpass
import readchar
from mysql.connector import Error

#Connect to db
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

#Function takes in user input, and returns a string, while echoing a single char to the console
#Char to echo defaults to . but can be passed as an argument
def echo_char(echo_char = '.'):
    pass_list = []
    key_stroke = readchar.readkey()
    while key_stroke != readchar.key.ENTER:
        pass_list.append(key_stroke)
        print(echo_char, end = '', flush = True)#echoes a single character to the console without newline
        key_stroke = readchar.readkey()
    secret = ''.join(pass_list)#convert pass_list to a string to return
    return secret

