from modules import format_methods as form, misc_methods as misc, draw_methods as draw
import decimal
from decimal import Decimal
import time, mysql.connector

#take separate list components and format into a single string
def format_list(head, body, prompt):
    top_grid = [' ']
    bottom_grid = [' ']

    # generate body with multiple line formatting using format_body
    alt_width = max(len(head), len(prompt))
    body_list = form.format_body(body, alt_width)
    grid_w = max(len(head), len(max(body_list, key = len)), len(prompt))
    body_form = ''.join(body_list)

    head_form = form.head_spacing(grid_w, head)

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
def format_details(head, body, prompt):
    pre_notes = []
    top = []
    bottom = []
    # convert tuple to list to allow editing
    body_list = []
    for i in body:
        body_list.append(i)

    # delete the title and db id from the body
    del body_list[0:2]

    # extract ingredient comment. if none, delete
    if body_list[-1] != None:
        note = body_list.pop()
        pre_notes = form.note_format(note)
    else:
        del body_list[-1]
        pre_notes = []

    # pass the rest of the body with the type to convert add titles and delete none
    pre_body = form.detail_title(body_list)

    # join body with note
    pre_body.extend(pre_notes)

    width = max(len(head), len(max(pre_body, key = len)), len(prompt))

    #get formatted head
    head_det = form.head_spacing(width, head)
    
    # generate grid top and bottom
    top.append(' ')
    bottom.append(' ')
    for _ in range(width):
        top.append('_')
        bottom.append('¯')
    top.append('\n')
    bottom.append('\n')
    top_det = ''.join(top)
    bottom_det = ''.join(bottom)

    #get formatted body
    body_det = form.format_details(pre_body, width)

    det_str = head_det + top_det + body_det + bottom_det + prompt
    return det_str

# draw formatted list to the screen
def draw_list(screen, raw_data, cur_screen, hs_db):
    list_len = len(raw_data)
    next_screen = None
    # ingredient building variable initialization
    create_loop = False

    hop_name = 'NULL'
    hop_origin = 'NULL'
    hop_type = 'NULL'
    htype_display = 'NULL'
    hop_alpha = 'NULL'
    hop_beta = 'NULL'
    hop_price = 0
    hop_qty = 0
    hop_notes = 'NULL'
    hnotes_display = 'NULL'

    # prebuilt headers
    main_head = 'Main Menu'
    ing_head = 'Ingredients'
    hlist_head = 'Hop Select'
    hadd_head = 'Create Hop'
    ylist_head = 'Yeast Select'
    yadd_head = 'Create Yeast'

    # prebuilt bodies
    main_body = [(None, 'Inventory'), (None, 'Recipes'), (None, 'Shopping Lists'), (None, 'Ingredients'), (None, 'Log Out'), (None, 'Exit')]
    ing_body = [(None, 'Hops'), (None, 'Yeast'), (None, 'Fermentables & Adjuncts'), (None, 'Water'), (None, 'Miscellaneous'), (None, 'Main Menu')]
    hadd_body = [(None, 'Hop Name'), (None, 'Hop Origin Country'), (None, 'Hop Type (Bittering, Aroma, or Both)'), (None, 'Alpha Acid Content (%)'), (None, 'Beta Acid Content (%)'), (None, 'Price'), (None, 'Quantity in Inventory'), (None, 'Notes'), (None, 'Save Hop'), (None, 'Exit Without Saving')]

    # prebuilt prompts
    main_prompt = 'Select Menu: '
    ing_prompt = 'Filter Ingredients: '
    add_prompt = 'Select Detail to Edit: '
    hlist_prompt = 'Select Hop: '
    ylist_prompt = 'Select Yeast: '

    # print formatted screen
    while (next_screen == None) or (create_loop == True):
        print(screen, end = '')
        option = input()

        # get the next screen from user input
        next_screen = draw.get_next(cur_screen, option, list_len, raw_data, screen)  

        # logic if the screen is deleting/updating something
        if next_screen == 'hop_del':
            next_screen = 'hop'
            db_curs = hs_db.cursor()
            db_curs.execute('DELETE FROM hops WHERE hop_id = {}'.format(raw_data[0]))
            hs_db.commit()
            db_curs.close()
        elif next_screen == 'hop_update':
            print("test code")
            misc.cls()
            add_val = input("Additional Quantity: ")
            add_val = Decimal(add_val)
            new_val = add_val + raw_data[7]
            next_screen = raw_data
            db_curs = hs_db.cursor()
            db_curs.execute('UPDATE hops SET hop_qty = {} WHERE hop_id = {}'.format(new_val, next_screen[0]))
            hs_db.commit()
            db_curs.close()
        # logic if the screen is creating something
        elif next_screen == 'hop_name':
            create_loop = True
            hop_name = input("Hop Name: ")
            misc.cls()
            hadd_body[0] = (None, ('Hop Name: ' + hop_name))
            screen = format_list(hadd_head, hadd_body, add_prompt)
            hop_name = form.quote_str(hop_name)
        elif next_screen == 'hop_origin':
            create_loop = True
            hop_origin = input("Hop Origin: ")
            misc.cls()
            hadd_body[1] = (None, ('Hop Origin Country: ' + hop_origin))
            screen = format_list(hadd_head, hadd_body, add_prompt)
            hop_origin = form.quote_str(hop_origin)
        elif next_screen == 'hop_type':
            create_loop = True
            hop_type = None
            while hop_type == None:
                hop_temp = input("Hop Type: ")
                if (hop_temp.lower() == 'bittering') or (hop_temp.lower() == 'b'):
                    hop_type = "'B'"
                    htype_display = 'Bittering'
                elif (hop_temp.lower() == 'aroma') or (hop_temp.lower() == 'a'):
                    hop_type = "'A'"
                    htype_display = 'Aroma'
                elif (hop_temp.lower() == 'both') or (hop_temp.lower() == 'o'):
                    hop_type = "'O'"
                    htype_display = 'Aroma and/or Bittering'
                else:
                    print("Please enter 'Bittering, Aroma, or Both'")
            misc.cls()
            hadd_body[2] = (None, ('Hop Type: ' + htype_display))
            screen = format_list(hadd_head, hadd_body, add_prompt)
        elif next_screen == 'hop_alpha':
            create_loop = True
            hop_alpha = None
            while hop_alpha == None:
                hop_temp = input("Alpha %: ")
                try:
                    hop_alpha = Decimal(hop_temp)
                except decimal.InvalidOperation:
                    print("Alpha acid must be a numeric value.")
            hop_alpha = round(hop_alpha, 2)
            hop_temp = str(hop_alpha)
            misc.cls()
            hadd_body[3] = (None, ('Alpha Acid Content: ' + hop_temp + '%'))
            screen = format_list(hadd_head, hadd_body, add_prompt)
        elif next_screen == 'hop_beta':
            create_loop = True
            hop_beta = None
            while hop_beta == None:
                hop_temp = input("Beta %: ")
                try:
                    hop_beta = Decimal(hop_temp)
                except decimal.InvalidOperation:
                    print("Beta acid must be a numeric value.")
            hop_beta = round(hop_beta, 2)
            hop_temp = str(hop_beta)
            misc.cls()
            hadd_body[4] = (None, ('Beta Acid Content: ' + hop_temp + '%'))
            screen = format_list(hadd_head, hadd_body, add_prompt)
        elif next_screen == 'hop_price':
            create_loop = True
            hop_price = None
            while hop_price == None:
                hop_temp = input("Price: ")
                try:
                    hop_price = Decimal(hop_temp)
                except decimal.InvalidOperation:
                    print("Price must be a numeric value.")
            hop_price = round(hop_price, 2)
            hop_temp = str(hop_price)
            misc.cls()
            hadd_body[5] = (None, ('Price: $' + hop_temp))
            screen = format_list(hadd_head, hadd_body, add_prompt)
        elif next_screen == 'hop_qty':
            create_loop = True
            hop_qty = None
            while hop_qty == None:
                hop_temp = input("Inventory Quantity: ")
                try:
                    hop_qty = Decimal(hop_temp)
                except decimal.InvalidOperation:
                    print("Quantity must be a numeric value.")
            hop_qty = round(hop_qty, 2)
            hop_temp = str(hop_qty)
            misc.cls()
            hadd_body[6] = (None, ('Inventory Quantity: ' + hop_temp + ' oz'))
            screen = format_list(hadd_head, hadd_body, add_prompt)
        elif next_screen == 'hop_notes':
            create_loop = True
            hnotes_lst = []
            hnotes_loop = 0
            hop_notes = input("Notes: ")
            for i in hop_notes:
                hnotes_lst.append(i)
                hnotes_loop += 1
                if hnotes_loop == 25:
                    break
            hnotes_display = ''.join(hnotes_lst)
            misc.cls()
            hadd_body[7] = (None, (hnotes_display + '...'))
            screen = format_list(hadd_head, hadd_body, add_prompt)
            hop_notes = form.quote_str(hop_notes)
        elif next_screen == 'hop_save':
            try:
                create_loop = False
                next_screen = 'hop'
                db_curs = hs_db.cursor()
                query_str = 'INSERT INTO hops(hop_name, hop_origin, hop_type, alpha, beta, hop_price, hop_qty, hop_notes) VALUES ({}, {}, {}, {}, {}, {}, {}, {})'.format(hop_name, hop_origin, hop_type, hop_alpha, hop_beta, hop_price, hop_qty, hop_notes)
                db_curs.execute(query_str)
                hs_db.commit()
                db_curs.close()
            except mysql.connector.errors.IntegrityError:
                create_loop = True
                misc.cls()
                screen = format_list('Hop Name Required', hadd_body, add_prompt)
            except mysql.connector.errors.DataError:
                create_loop = True
                misc.cls()
                screen = format_list('Invalid data. Double check alpha, beta, price, and quantity.', hadd_body, add_prompt)
        else:
            create_loop = False

    # return the screen data if next screen doesn't require a db query
    if type(next_screen) == str:
        if next_screen == 'main':
            return [next_screen, main_head, main_body, main_prompt]
        elif next_screen == 'ing':
            return [next_screen, ing_head, ing_body, ing_prompt]
        elif next_screen == 'hop_add':
            return [next_screen, hadd_head, hadd_body, add_prompt]
        elif next_screen == 'exit' or next_screen == 'log':
            return next_screen
        elif next_screen == 'hop':
            # get the list of query responses to format for the next screen
            hop_body = draw.get_body(next_screen, 'all', hs_db)
            return [next_screen, hlist_head, hop_body, hlist_prompt]
        elif next_screen == 'yst':
            yst_body = draw.get_body(next_screen, 'all', hs_db)
            return [next_screen, ylist_head, yst_body, ylist_prompt]
        elif next_screen == 'srch':
            query = input("Search Query: ")
            search_body = draw.get_body(next_screen, query, hs_db, cur_screen)
            return [next_screen, hlist_head, search_body, hlist_prompt]
    else:
        if 'hop' in cur_screen:
            srch_table = 'hop'
        next_det = draw.get_body(cur_screen, next_screen[0], hs_db, srch_table)
        det_head = next_det[1]
        return [next_screen, det_head, next_det, '1. Return\n2. Add Inventory\n3. Delete\n\nSelect Option: ']

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
        if ('_det' in cur_screen) == True:
            screen_now = format_details(cur_head, cur_body, cur_prompt)
        else:
            screen_now = format_list(cur_head, cur_body, cur_prompt)
        screen_next = draw_list(screen_now, cur_body, cur_screen, db_con)
        
        if screen_next == 'log':
            inner_loop = False
        elif screen_next == 'exit':
            inner_loop = False
            outer_loop = False
        else:
            if type(screen_next[0]) != str:
                if cur_screen == 'srch':
                    if cur_head == 'Hop Select':
                        cur_screen = 'hop_det'
                else:
                    if ('_det' in cur_screen) == False:
                        cur_screen = cur_screen + '_det'
            else:
                cur_screen = screen_next[0]
            cur_head = screen_next[1]
            cur_body = screen_next[2]
            cur_prompt = screen_next[3]

    if db_con != None and db_con.is_connected():
        db_con.close()
    misc.cls()