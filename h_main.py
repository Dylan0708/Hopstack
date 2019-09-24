from modules import format_methods as form, misc_methods as misc, draw_methods as draw
import time, mysql.connector

#take separate list components and format into a single string
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

# take separate details components and format into a single string
def format_details(body, prompt):
    det_head = body[1]

# draw formatted list to the screen
def draw_list(screen, raw_data, cur_screen, hs_db):
    list_len = len(raw_data)
    next_screen = None

    # prebuilt headers
    main_head = 'Main Menu'
    ing_head = 'Ingredients'
    hlist_head = 'Hop Select'

    # prebuilt bodies
    main_body = [(None, 'Inventory'), (None, 'Recipes'), (None, 'Shopping Lists'), (None, 'Ingredients'), (None, 'Log Out'), (None, 'Exit')]
    ing_body = [(None, 'Hops'), (None, 'Yeast'), (None, 'Fermentables & Adjuncts'), (None, 'Water'), (None, 'Miscellaneous'), (None, 'All'), (None, 'Main Menu')]

    # prebuilt prompts
    main_prompt = 'Select Menu: '
    ing_prompt = 'Filter Ingredients: '
    hlist_prompt = 'Select Hop: '

    # print formatted screen
    while next_screen == None:
        print(screen, end = '')
        option = input()
        next_screen = draw.get_next(cur_screen, option, list_len, raw_data)  # get the next screen from user input

    # return the screen data if next screen doesn't require a db query
    if next_screen == 'main':
        return [next_screen, main_head, main_body, main_prompt]
    elif next_screen == 'ing':
        return [next_screen, ing_head, ing_body, ing_prompt]
    elif next_screen == 'exit' or next_screen == 'log':
        return next_screen
    else:
    # get the list of query responses to format for the next screen
        hop_body = draw.get_body(next_screen, 'all', hs_db)
        return [next_screen, hlist_head, hop_body, hlist_prompt]


# main program
db_con = None
outer_loop = True
cur_screen = 'main'
cur_head = 'Main Menu'
cur_body = [(None, 'Inventory'), (None, 'Recipes'), (None, 'Shopping Lists'), (None, 'Ingredients'), (None, 'Log Out'), (None, 'Exit')]
cur_prompt = 'Select Menu: '

while outer_loop == True:
    misc.cls()
    username = 'root' #input("Enter Username: ")
    password = 'StupidSexyFlanders' #misc.echo_char("Enter Password: ")
    
    try:
        db_con = mysql.connector.connect(host = 'localhost', database = 'hopstack', user = username, password = password) #attempt db connection
    except mysql.connector.Error as e:
        misc.cls()
        print("Unable to Connect: {}".format(e))
        for i in range(3):
            time.sleep(1)
            print(".")
    
    if db_con != None and db_con.is_connected():
        inner_loop = True
    
    while inner_loop == True:
        misc.cls()
        screen_now = format_list(cur_head, cur_body, cur_prompt)
        screen_next = draw_list(screen_now, cur_body, cur_screen, db_con)
        
        if screen_next == 'log':
            inner_loop = False
        elif screen_next == 'exit':
            inner_loop = False
            outer_loop = False
        else:
            cur_screen = screen_next[0]
            cur_head = screen_next[1]
            cur_body = screen_next[2]
            cur_prompt = screen_next[3]

    if db_con != None and db_con.is_connected():
        db_con.close()
    misc.cls()
    
    
    
    
    #call format list with initial params
    #call draw list with initial params

