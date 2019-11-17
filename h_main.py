from modules import format_methods as form, misc_methods as misc, draw_methods as draw
import decimal
from decimal import Decimal
import time, mysql.connector, hstack_classes as hscls

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

    hop_cr = hscls.Hop()
    yst_cr = hscls.Yeast()
    ferm_cr = hscls.Ferm()

    # prebuilt headers
    main_head = 'Main Menu'
    ing_head = 'Ingredients'
    hlist_head = 'Hop Select'
    hadd_head = 'Create Hop'
    ylist_head = 'Yeast Select'
    yadd_head = 'Create Yeast'
    flist_head = 'Fermentable/Adjunct Select'
    fadd_head = 'Create Fermentable/Adjunct'

    # prebuilt bodies
    main_body = [(None, 'Inventory'), (None, 'Recipes'), (None, 'Shopping Lists'), (None, 'Ingredients'), (None, 'Log Out'), (None, 'Exit')]
    ing_body = [(None, 'Hops'), (None, 'Yeast'), (None, 'Fermentables & Adjuncts'), (None, 'Water'), (None, 'Miscellaneous'), (None, 'Main Menu')]

    # prebuilt prompts
    main_prompt = 'Select Menu: '
    ing_prompt = 'Filter Ingredients: '
    add_prompt = 'Select Detail to Edit: '
    hlist_prompt = 'Select Hop: '
    ylist_prompt = 'Select Yeast: '
    flist_prompt = 'Select Fermentable/Adjunct: '

    # Create ingredient switch functions
    def h_name():
        nonlocal create_loop, hop_cr, screen, add_prompt, hadd_head
        create_loop = True
        hop_cr.get_name()
        misc.cls()
        screen = format_list(hadd_head, hop_cr.body, add_prompt)

    def h_origin():
        nonlocal create_loop, hop_cr, screen, add_prompt, hadd_head
        create_loop = True
        hop_cr.get_origin()
        misc.cls()
        screen = format_list(hadd_head, hop_cr.body, add_prompt)

    def h_type():
        nonlocal create_loop, hop_cr, screen, add_prompt, hadd_head
        create_loop = True
        hop_cr.get_type()
        misc.cls()
        screen = format_list(hadd_head, hop_cr.body, add_prompt)

    def h_alpha():
        nonlocal create_loop, hop_cr, screen, add_prompt, hadd_head
        create_loop = True
        hop_cr.get_alpha()
        misc.cls()
        screen = format_list(hadd_head, hop_cr.body, add_prompt)

    def h_beta():
        nonlocal create_loop, hop_cr, screen, add_prompt, hadd_head
        create_loop = True
        hop_cr.get_beta()
        misc.cls()
        screen = format_list(hadd_head, hop_cr.body, add_prompt)

    def h_price():
        nonlocal create_loop, hop_cr, screen, add_prompt, hadd_head
        create_loop = True
        hop_cr.get_price()
        misc.cls()
        screen = format_list(hadd_head, hop_cr.body, add_prompt)

    def h_qty():
        nonlocal create_loop, hop_cr, screen, add_prompt, hadd_head
        create_loop = True
        hop_cr.get_qty()
        misc.cls()
        screen = format_list(hadd_head, hop_cr.body, add_prompt)

    def h_notes():
        nonlocal create_loop, hop_cr, screen, add_prompt, hadd_head
        create_loop = True
        hop_cr.get_notes()
        misc.cls()
        screen = format_list(hadd_head, hop_cr.body, add_prompt)

    def h_save():
        nonlocal create_loop, hop_cr, screen, hs_db, next_screen, add_prompt
        success = hop_cr.save(hs_db)
        if success[0]:
            create_loop = False
            next_screen = 'hop'
        else:
            create_loop = True
            if success[1] == 'name':
                temp_head = 'Name Required'
            else:
                temp_head = 'Invalid data. Double check alpha, beta, price, and quantity.'
            misc.cls()
            screen = format_list(temp_head, hop_cr.body, add_prompt)

    def y_name():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_name()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_ar():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_ar()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_prid():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_pid()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_lab():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_lab()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_type():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_type()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_alc():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_alc()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_floc():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_floc()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_minatt():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_minat()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_maxatt():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_maxat()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_mintmp():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_mintmp()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_maxtmp():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_maxtmp()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_price():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_price()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_qty():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_qty()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_notes():
        nonlocal create_loop, yst_cr, screen, add_prompt, yadd_head
        create_loop = True
        yst_cr.get_notes()
        misc.cls()
        screen = format_list(yadd_head, yst_cr.body, add_prompt)

    def y_save():
        nonlocal create_loop, yst_cr, screen, hs_db, next_screen, add_prompt
        success = yst_cr.save(hs_db)
        if success[0]:
            create_loop = False
            next_screen = 'yst'
        else:
            create_loop = True
            if success[1] == 'name':
                temp_head = 'Name Required'
            else:
                temp_head = 'Invalid data. Double check price, and quantity.'
            misc.cls()
            screen = format_list(temp_head, yst_cr.body, add_prompt)

    def f_name():
        nonlocal create_loop, ferm_cr, screen, add_prompt, fadd_head
        create_loop = True
        ferm_cr.get_name()
        misc.cls()
        screen = format_list(fadd_head, ferm_cr.body, add_prompt)

    def f_origin():
        nonlocal create_loop, ferm_cr, screen, add_prompt, fadd_head
        create_loop = True
        ferm_cr.get_origin()
        misc.cls()
        screen = format_list(fadd_head, ferm_cr.body, add_prompt)

    def f_type():
        nonlocal create_loop, ferm_cr, screen, add_prompt, fadd_head
        create_loop = True
        ferm_cr.get_type()
        misc.cls()
        screen = format_list(fadd_head, ferm_cr.body, add_prompt)

    def f_pg():
        nonlocal create_loop, ferm_cr, screen, add_prompt, fadd_head
        create_loop = True
        can_write = ferm_cr.get_grav()
        misc.cls()
        if can_write:
            screen = format_list(fadd_head, ferm_cr.body, add_prompt)
        else:
            screen = format_list('Potential/Specific Gravity Requires a Type', ferm_cr.body, add_prompt)

    def f_col():
        nonlocal create_loop, ferm_cr, screen, add_prompt, fadd_head
        create_loop = True
        ferm_cr.get_col()
        misc.cls()
        screen = format_list(fadd_head, ferm_cr.body, add_prompt)

    def f_dp():
        nonlocal create_loop, ferm_cr, screen, add_prompt, fadd_head
        create_loop = True
        can_write = ferm_cr.get_dp()
        misc.cls()
        if can_write:
            screen = format_list(fadd_head, ferm_cr.body, add_prompt)
        else:
            screen = format_list('Diastatic Power Requires Type "Base Malt", "Specialty Malt", or "Adjunct"', ferm_cr.body, add_prompt)

    def f_pc():
        nonlocal create_loop, ferm_cr, screen, add_prompt, fadd_head
        create_loop = True
        can_write = ferm_cr.get_pc()
        misc.cls()
        if can_write:
            screen = format_list(fadd_head, ferm_cr.body, add_prompt)
        else:
            screen = format_list('Protein Content Requires Type "Base Malt", "Specialty Malt", or "Adjunct"', ferm_cr.body, add_prompt)

    def f_price():
        nonlocal create_loop, ferm_cr, screen, add_prompt, fadd_head
        create_loop = True
        ferm_cr.get_price()
        misc.cls()
        screen = format_list(fadd_head, ferm_cr.body, add_prompt)

    def f_qty():
        nonlocal create_loop, ferm_cr, screen, add_prompt, fadd_head
        create_loop = True
        ferm_cr.get_qty()
        misc.cls()
        screen = format_list(fadd_head, ferm_cr.body, add_prompt)

    def f_notes():
        nonlocal create_loop, ferm_cr, screen, add_prompt, fadd_head
        create_loop = True
        ferm_cr.get_notes()
        misc.cls()
        screen = format_list(fadd_head, ferm_cr.body, add_prompt)

    def f_save():
        nonlocal create_loop, ferm_cr, screen, hs_db, next_screen, add_prompt
        success = ferm_cr.save(hs_db)
        if success[0]:
            create_loop = False
            next_screen = 'ferm'
        else:
            create_loop = True
            if success[1] == 'name':
                temp_head = 'Name Required'
            else:
                temp_head = 'Invalid data. Double check potential/specific gravity, colour, diastatic power, protein content, price, and quantity.'
            misc.cls()
            screen = format_list(temp_head, ferm_cr.body, add_prompt)

    def default():
        nonlocal create_loop
        create_loop = False

    # ingredient create switcher. Provide next_screen variable
    create_case = {
        'hop_name': h_name,
        'hop_origin': h_origin,
        'hop_type': h_type,
        'hop_alpha': h_alpha,
        'hop_beta': h_beta,
        'hop_price': h_price,
        'hop_qty': h_qty,
        'hop_notes': h_notes,
        'hop_save': h_save,
        'yst_name': y_name,
        'yst_ar': y_ar,
        'yst_prid': y_prid,
        'yst_lab': y_lab,
        'yst_type': y_type,
        'yst_alc': y_alc,
        'yst_floc': y_floc,
        'yst_minatt': y_minatt,
        'yst_maxatt': y_maxatt,
        'yst_mintmp': y_mintmp,
        'yst_maxtmp': y_maxtmp,
        'yst_price': y_price,
        'yst_qty': y_qty,
        'yst_notes': y_notes,
        'yst_save': y_save,
        'ferm_name': f_name,
        'ferm_origin': f_origin,
        'ferm_type': f_type,
        'ferm_pg': f_pg,
        'ferm_col': f_col,
        'ferm_dp': f_dp,
        'ferm_pc': f_pc,
        'ferm_price': f_price,
        'ferm_qty': f_qty,
        'ferm_notes': f_notes,
        'ferm_save': f_save
    }

    # loop until a valid next screen is selected or through a create screen
    while (next_screen == None) or (create_loop == True):
        # print formatted screen and get user input for next screen
        print(screen, end = '')
        option = input()

        # get the next screen from user input
        next_screen = draw.get_next(cur_screen, option, list_len, raw_data, screen)   

        if type(next_screen) == str:
            create_case.get(next_screen, default)()
        else:
            default()

    # logic if the screen is deleting/updating something
    if next_screen == 'hop_del':
        next_screen = 'hop'
        db_curs = hs_db.cursor()
        db_curs.execute('DELETE FROM hops WHERE hop_id = {}'.format(raw_data[0]))
        hs_db.commit()
        db_curs.close()
    elif next_screen == 'hop_update':
        misc.cls()
        add_val = input("Additional Quantity: ")
        add_val = Decimal(add_val)
        new_val = add_val + raw_data[7]
        next_screen = raw_data
        db_curs = hs_db.cursor()
        db_curs.execute('UPDATE hops SET hop_qty = {} WHERE hop_id = {}'.format(new_val, next_screen[0]))
        hs_db.commit()
        db_curs.close()
    elif next_screen == 'yst_del':
        next_screen = 'yst'
        db_curs = hs_db.cursor()
        db_curs.execute('DELETE FROM yeast WHERE yeast_id = {}'.format(raw_data[0]))
        hs_db.commit()
        db_curs.close()
    elif next_screen == 'yst_update':
        misc.cls()
        add_val = input("Additional Quantity: ")
        add_val = Decimal(add_val)
        new_val = add_val + raw_data[13]
        next_screen = raw_data
        db_curs = hs_db.cursor()
        db_curs.execute('UPDATE yeast SET yeast_qty = {} WHERE yeast_id = {}'.format(new_val, next_screen[0]))
        hs_db.commit()
        db_curs.close()
    elif next_screen == 'ferm_del':
        next_screen = 'ferm'
        db_curs = hs_db.cursor()
        db_curs.execute('DELETE FROM fermentables WHERE ferm_id = {}'.format(raw_data[0]))
        hs_db.commit()
        db_curs.close()
    elif next_screen == 'ferm_update':
        misc.cls()
        add_val = input("Additional Quantity: ")
        add_val = Decimal(add_val)
        new_val = add_val + raw_data[9]
        next_screen = raw_data
        db_curs = hs_db.cursor()
        db_curs.execute('UPDATE fermentables SET ferm_qty = {} WHERE ferm_id = {}'.format(new_val, next_screen[0]))
        hs_db.commit()
        db_curs.close()

    # return the screen data if next screen doesn't require a db query
    if type(next_screen) == str:
        if next_screen == 'main':
            return [next_screen, main_head, main_body, main_prompt]
        elif next_screen == 'ing':
            return [next_screen, ing_head, ing_body, ing_prompt]
        elif next_screen == 'hop_add':
            return [next_screen, hadd_head, hop_cr.body, add_prompt]
        elif next_screen == 'yst_add':
            return [next_screen, yadd_head, yst_cr.body, add_prompt]
        elif next_screen == 'ferm_add':
            return [next_screen, fadd_head, ferm_cr.body, add_prompt]
        elif next_screen == 'exit' or next_screen == 'log':
            return next_screen
        # get the list of query responses to format for the next screen
        elif next_screen == 'hop':
            hop_body = draw.get_body(next_screen, 'all', hs_db)
            return [next_screen, hlist_head, hop_body, hlist_prompt]
        elif next_screen == 'yst':
            yst_body = draw.get_body(next_screen, 'all', hs_db)
            return [next_screen, ylist_head, yst_body, ylist_prompt]
        elif next_screen == 'ferm':
            ferm_body = draw.get_body(next_screen, 'all', hs_db)
            return [next_screen, flist_head, ferm_body, flist_prompt]
        elif next_screen == 'hop_srch':
            query = input("Search Query: ")
            search_body = draw.get_body(next_screen, query, hs_db, cur_screen)
            return [next_screen, hlist_head, search_body, hlist_prompt]
        elif next_screen == 'yst_srch':
            query = input("Search Query: ")
            search_body = draw.get_body(next_screen, query, hs_db, cur_screen)
            return [next_screen, ylist_head, search_body, ylist_prompt]
        elif next_screen == 'ferm_srch':
            query = input("Search Query: ")
            search_body = draw.get_body(next_screen, query, hs_db, cur_screen)
            return [next_screen, flist_head, search_body, flist_prompt]
    else:
        if cur_screen == 'hop' or cur_screen == 'hop_det' or cur_screen == 'hop_srch':
            srch_table = 'hop'
        elif cur_screen == 'yst' or cur_screen == 'yst_det' or cur_screen == 'yst_srch':
            srch_table = 'yst'
        elif cur_screen == 'ferm' or cur_screen == 'ferm_det' or cur_screen == 'ferm_srch':
            srch_table = 'ferm'
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
                if cur_screen == 'hop_srch':
                    cur_screen = 'hop_det'
                elif cur_screen == 'yst_srch':
                    cur_screen = 'yst_det'
                elif cur_screen == 'ferm_srch':
                    cur_screen = 'ferm_det'
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