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
        sys.exit("Couldn't Connect") #exit
    
    return db_con #if connected, return connection

#Clear screen function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Function takes in user input, and returns a string, while echoing a single char to the console
#Char to echo defaults to . but can be passed as an argument
def echo_char(prompt = None, echo_char = '.'):
    cursor_index = 0
    pass_list = []
    if prompt != None:
        print(prompt, end = '', flush = True)#if there's a prompt, print it
    key_stroke = readchar.readkey()
    while key_stroke != readchar.key.ENTER:#keep geting input until ENTER
        if key_stroke == '\x08':
            if cursor_index > 0:
                del pass_list[-1]
                print('\b \b', end = '', flush = True)#move cursor back, overwrite with blank in event of
                cursor_index -= 1
        else:
            pass_list.append(key_stroke)
            print(echo_char, end = '', flush = True)#echoes string to the console without newline
            cursor_index += 1
        key_stroke = readchar.readkey()
    secret = ''.join(pass_list)#convert pass_list to a string to return
    return secret

def login():
    username = input("Enter Username: ")
    password = echo_char("Enter Password: ")
    con = hstack_connect(username, password)
    return con
