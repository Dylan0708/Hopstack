from modules import format_methods as form, misc_methods as misc
import time, mysql.connector

#take separate view components and format into a single string
def format_list(head, body, prompt):
    head_w = len(head)
    head_space = []
    top_grid = [' ']
    bottom_grid = [' ']

    # generate body with multiple line formatting using format_body
    alt_width = max(len(head), len(prompt))
    body_list = form.format_body(body, alt_width)
    grid_w = max(len(head), len(max(body_list, key = len)), len(prompt))
    body_form = ''.join(body_list)

    if (grid_w % 2) != 0:
        temp_gwidth = grid_w + 1
    else:
        temp_gwidth = grid_w

    if (head_w % 2) != 0:
        head_w += 1

    # find the relative position of the header based on the grid width and the header width
    h_pos = int((temp_gwidth / 2) - (head_w / 2))

    # generate header with formatted spacing
    for _ in range(h_pos):
        head_space.append(' ')
    empty = ''.join(head_space)
    head_form = (empty + head + '\n')

    # generate grid top
    temp_gwidth = grid_w - 3
    for _ in range(temp_gwidth):
        top_grid.append('_')
        bottom_grid.append('¯')
    top_grid.append('\n')
    bottom_grid.append('\n')
    top_form = ''.join(top_grid)
    bottom_form = ''.join(bottom_grid)

    # stitch all the formatted pieces together into a single string
    screen_form = head_form + top_form + body_form + bottom_form + prompt

    return screen_form

def draw_list(screen, type):
    # prebuilt headers
    main_head = 'Main Menu'
    ing_head = 'Ingredients'
    hlist_head = 'Hop Select'

    # prebuilt bodies
    main_body = [()]

"""test = format_list('test list', [(None, 'test1', None), (6, 'test2', 'bleh', None), (2, 'test3', 'babaa')], 'prompt: ')
misc.cls()
print(test, end = '')"""

db_con = None
outer_loop = True
inner_loop = True
cur_screen = 'main'


while outer_loop == True:
    misc.cls()
    username = 'root' #input("Enter Username: ")
    password = 'StupidSexyFlanders' #main_func.echo_char("Enter Password: ")
    
    try:
        db_con = mysql.connector.connect(host = 'localhost', database = 'hopstack', user = username, password = password) #attempt db connection
    except mysql.connector.Error as e:
        misc.cls()
        print("Unable to Connect: {}".format(e))
        for i in range(3):
            time.sleep(1)
            print(".")

    if db_con != None and db_con.is_connected():
        db_con.close()
    
    
    
    
    #call format list with initial params
    #call draw list with initial params

