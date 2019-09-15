import main_func

conn = main_func.hstack_connect('root', 'StupidSexyFlanders')
cursor = conn.cursor()
cursor.execute("SELECT * FROM yeast")

row = cursor.fetchone()

while row != None:
    print(row)
    row = cursor.fetchone()

cursor.close()
conn.close()
