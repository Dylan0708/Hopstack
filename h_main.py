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
    yst_name = 'NULL'
    yst_ar = 21
    yst_prid = 'NULL'
    yst_lab = 'NULL'
    yst_type = 'NULL'
    yst_alc = 'NULL'
    yst_floc = 'NULL'
    yst_minatt = 'NULL'
    yst_maxatt = 'NULL'
    yst_mintmp = 'NULL'
    yst_maxtmp = 'NULL'
    yst_price = 0
    yst_qty = 0
    yst_notes = 'NULL'
    ynotes_display = 'NULL'

    ferm_name = 'NULL'
    ferm_origin = 'NULL'
    ferm_type = 'NULL'
    ftype_display = 'NULL'
    ferm_pg = 'NULL'
    ferm_col = 'NULL'
    ferm_dp = 'NULL'
    ferm_pc = 'NULL'
    ferm_price = 0
    ferm_qty = 0
    ferm_notes = 'NULL'
    fnotes_display = 'NULL'

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
    yadd_body = [(None, 'Name'), (None, 'Monthly Viability Loss (%)'), (None, 'Product ID'), (None, 'Lab'), (None, 'Type (Ale, Lager, Brett, Diastaticus, Kveik, Pediococcus, Lactobacillus, or Mixed Culture)'), (None, 'Alcohol Tolerance (%)'), (None, 'Flocculation (Low, Medium, or High)'), (None, 'Minimum Attenuation (%)'), (None, 'Maximum Attenuation (%)'), (None, 'Minimum Temperature (°C)'), (None, 'Maximum Temperature (°C)'), (None, 'Price'), (None, 'Quantity in Inventory'), (None, 'Notes'), (None, 'Save'), (None, 'Exit Without Saving')]
    fadd_body = [(None, 'Name'), (None, 'Origin'), (None, 'Type (Base Malt, Specialty Malt, Liquid Extract, Dry Extract, Sugar, Syrup, Juice, Fruit, Adjunct, or Other)'), (None, 'Potential/Specific Gravity'), (None, 'Colour Contribution (Lovibond)'), (None, 'Diastatic Power (Litner)'), (None, 'Protein Content (%)'), (None, 'Price'), (None, 'Quantity in Inventory'), (None, 'Notes'), (None, 'Save Yeast'), (None, 'Exit Without Saving')]

    # prebuilt prompts
    main_prompt = 'Select Menu: '
    ing_prompt = 'Filter Ingredients: '
    add_prompt = 'Select Detail to Edit: '
    hlist_prompt = 'Select Hop: '
    ylist_prompt = 'Select Yeast: '
    flist_prompt = 'Select Fermentable/Adjunct: '

    # loop until a valid next screen is selected or through a create screen
    while (next_screen == None) or (create_loop == True):
        # print formatted screen and get user input for next screen
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

        # logic if the screen is creating something
        elif next_screen == 'hop_name':
            create_loop = True
            hop_cr.get_name()
            misc.cls()
            screen = format_list(hadd_head, hop_cr.body, add_prompt)
        elif next_screen == 'hop_origin':
            create_loop = True
            hop_cr.get_origin()
            misc.cls()
            screen = format_list(hadd_head, hop_cr.body, add_prompt)
        elif next_screen == 'hop_type':
            create_loop = True
            hop_cr.get_type()
            misc.cls()
            screen = format_list(hadd_head, hop_cr.body, add_prompt)
        elif next_screen == 'hop_alpha':
            create_loop = True
            hop_cr.get_alpha()
            misc.cls()
            screen = format_list(hadd_head, hop_cr.body, add_prompt)
        elif next_screen == 'hop_beta':
            create_loop = True
            hop_cr.get_beta()
            misc.cls()
            screen = format_list(hadd_head, hop_cr.body, add_prompt)
        elif next_screen == 'hop_price':
            create_loop = True
            hop_cr.get_price()
            misc.cls()
            screen = format_list(hadd_head, hop_cr.body, add_prompt)
        elif next_screen == 'hop_qty':
            create_loop = True
            hop_cr.get_qty()
            misc.cls()
            screen = format_list(hadd_head, hop_cr.body, add_prompt)
        elif next_screen == 'hop_notes':
            create_loop = True
            hop_cr.get_notes()
            misc.cls()
            screen = format_list(hadd_head, hop_cr.body, add_prompt)
        elif next_screen == 'hop_save':
            success = hop_cr.save(hs_db)
            if success[0]:
                create_loop = False
                next_screen = 'hop'
            else:
                create_loop = True
                if success[1] == "1048 (23000): Column 'hop_name' cannot be null":
                    temp_head = 'Hop Name Required'
                else:
                    temp_head = 'Invalid data. Double check alpha, beta, price, and quantity.'
                misc.cls()
                screen = format_list(temp_head, hop_cr.body, add_prompt)

        elif next_screen == 'yst_name':
            create_loop = True
            yst_cr.get_name()
            misc.cls()
            screen = format_list(yadd_head, yst_cr.body, add_prompt)
        elif next_screen == 'yst_ar':
            create_loop = True
            yst_cr.get_ar()
            misc.cls()
            screen = format_list(yadd_head, yst_cr.body, add_prompt)
        elif next_screen == 'yst_prid':
            create_loop = True
            yst_cr.get_pid()
            misc.cls()
            screen = format_list(yadd_head, yst_cr.body, add_prompt)
        elif next_screen == 'yst_lab':
            create_loop = True
            yst_cr.get_lab()
            misc.cls()
            screen = format_list(yadd_head, yst_cr.body, add_prompt)
        elif next_screen == 'yst_type':
            create_loop = True
            yst_cr.get_type()
            misc.cls()
            screen = format_list(yadd_head, yst_cr.body, add_prompt)
        elif next_screen == 'yst_alc':
            create_loop = True
            yst_cr.get_alc()
            misc.cls()
            screen = format_list(yadd_head, yst_cr.body, add_prompt)
        elif next_screen == 'yst_floc':
            create_loop = True
            yst_cr.get_floc()
            misc.cls()
            screen = format_list(yadd_head, yst_cr.body, add_prompt)
        elif next_screen == 'yst_minatt':
            create_loop = True
            yst_cr.get_minat()
            misc.cls()
            screen = format_list(yadd_head, yst_cr.body, add_prompt)
        elif next_screen == 'yst_maxatt':
            create_loop = True
            yst_cr.get_maxat()
            misc.cls()
            screen = format_list(yadd_head, yst_cr.body, add_prompt)
        elif next_screen == 'yst_mintmp':
            create_loop = True
            yst_cr.get_mintmp()
            misc.cls()
            screen = format_list(yadd_head, yst_cr.body, add_prompt)
        elif next_screen == 'yst_maxtmp':
            create_loop = True
            yst_cr.get_maxtmp()
            misc.cls()
            screen = format_list(yadd_head, yst_cr.body, add_prompt)
        elif next_screen == 'yst_price':
            create_loop = True
            yst_cr.get_price()
            misc.cls()
            screen = format_list(yadd_head, yst_cr.body, add_prompt)
        elif next_screen == 'yst_qty':
            create_loop = True
            yst_qty = None
            while yst_qty == None:
                yst_temp = input("Inventory Quantity: ")
                try:
                    yst_qty = Decimal(yst_temp)
                except decimal.InvalidOperation:
                    print("Quantity must be a numeric value.")
            yst_qty = round(yst_qty, 2)
            yst_temp = str(yst_qty)
            misc.cls()
            yadd_body[12] = (None, ('Inventory Quantity: ' + yst_temp + ' Units'))
            screen = format_list(yadd_head, yadd_body, add_prompt)
        elif next_screen == 'yst_notes':
            create_loop = True
            ynotes_lst = []
            ynotes_loop = 0
            yst_notes = input("Notes: ")
            for i in yst_notes:
                ynotes_lst.append(i)
                ynotes_loop += 1
                if ynotes_loop == 25:
                    break
            ynotes_display = ''.join(ynotes_lst)
            misc.cls()
            yadd_body[13] = (None, (ynotes_display + '...'))
            screen = format_list(yadd_head, yadd_body, add_prompt)
            yst_notes = form.sql_sanitize(yst_notes)
            yst_notes = form.quote_str(yst_notes)
        elif next_screen == 'yst_save':
            try:
                create_loop = False
                next_screen = 'yst'
                db_curs = hs_db.cursor()
                query_str = 'INSERT INTO yeast(yeast_name, age_rate, product_id, lab, yeast_type, alcohol_tolerance, flocculation, min_attenuation, max_attenuation, min_temperature, max_temperature, yeast_price, yeast_qty, yeast_notes) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(yst_name, yst_ar, yst_prid, yst_lab, yst_type, yst_alc, yst_floc, yst_minatt, yst_maxatt, yst_mintmp, yst_maxtmp, yst_price, yst_qty, yst_notes)
                db_curs.execute(query_str)
                hs_db.commit()
                db_curs.close()
            except mysql.connector.errors.IntegrityError:
                create_loop = True
                misc.cls()
                screen = format_list('Yeast Name Required', yadd_body, add_prompt)
            except mysql.connector.errors.DataError:
                create_loop = True
                misc.cls()
                screen = format_list('Invalid data. Double check price, and quantity.', yadd_body, add_prompt)

        elif next_screen == 'ferm_name':
            create_loop = True
            ferm_name = input("Name: ")
            misc.cls()
            fadd_body[0] = (None, ('Name: ' + ferm_name))
            screen = format_list(fadd_head, fadd_body, add_prompt)
            ferm_name = form.quote_str(ferm_name)
        elif next_screen == 'ferm_origin':
            create_loop = True
            ferm_origin = input("Origin: ")
            misc.cls()
            fadd_body[1] = (None, ('Origin: ' + ferm_origin))
            screen = format_list(fadd_head, fadd_body, add_prompt)
            ferm_origin = form.quote_str(ferm_origin)
        elif next_screen == 'ferm_type':
            create_loop = True
            ferm_type = None
            while ferm_type == None:
                ferm_temp = input("Type: ")
                if ('b' in ferm_temp.lower()) == True:
                    ferm_type = "'B'"
                    ftype_display = 'Base Malt'
                elif ('sp' in ferm_temp.lower()) == True:
                    ferm_type = "'S'"
                    ftype_display = 'Specialty Malt'
                elif ('l' in ferm_temp.lower()) == True:
                    ferm_type = "'L'"
                    ftype_display = 'Liquid Extract'
                elif ('a' in ferm_temp.lower()) == True:
                    ferm_type = "'A'"
                    ftype_display = 'Adjunct'
                elif ('d' in ferm_temp.lower()) == True:
                    ferm_type = "'D'"
                    ftype_display = 'Dry Extract'
                elif ('su' in ferm_temp.lower()) == True:
                    ferm_type = "'U'"
                    ftype_display = 'Sugar'
                elif ('sy' in ferm_temp.lower()) == True:
                    ferm_type = "'Y'"
                    ftype_display = 'Syrup'
                elif ('j' in ferm_temp.lower()) == True:
                    ferm_type = "'J'"
                    ftype_display = 'Juice'
                elif ('f' in ferm_temp.lower()) == True:
                    ferm_type = "'F'"
                    ftype_display = 'Fruit'
                else:
                    ferm_type = "'O'"
                    ftype_display = 'Other'
            misc.cls()
            if ferm_pg != 'NULL':
                ferm_temp = str(ferm_pg)
                if ferm_type == "'B'" or ferm_type == "'S'" or ferm_type == "'A'":
                    fadd_body[3] = (None, ('Potential Gravity: ' + ferm_temp))
                else:
                    fadd_body[3] = (None, ('Specific Gravity: ' + ferm_temp))
            if ferm_dp != 'NULL':
                ferm_temp = str(ferm_dp)
                if ferm_type != "'B'" and ferm_type != "'S'" and ferm_type != "'A'":
                    ferm_dp = 'NULL'
                    fadd_body[5] = (None, 'Diastatic Power (Litner)')
            if ferm_pc != 'NULL':
                ferm_temp = str(ferm_pc)
                if ferm_type != "'B'" and ferm_type != "'S'" and ferm_type != "'A'":
                    ferm_pc = 'NULL'
                    fadd_body[6] = (None, 'Protein Content (%)')
            fadd_body[2] = (None, ('Type: ' + ftype_display))
            screen = format_list(fadd_head, fadd_body, add_prompt)
        elif next_screen == 'ferm_pg':
            create_loop = True
            if ferm_type == "'B'" or ferm_type == "'S'" or ferm_type == "'A'":
                ferm_pg = None
                while ferm_pg == None:
                    ferm_temp = input("Potential Gravity: ")
                    try:
                        ferm_pg = Decimal(ferm_temp)
                    except decimal.InvalidOperation:
                        print("Potential gravity must be a numeric value.")
                ferm_pg = round(ferm_pg, 3)
                ferm_temp = str(ferm_pg)
                misc.cls()
                fadd_body[3] = (None, ('Potential Gravity: ' + ferm_temp))
                screen = format_list(fadd_head, fadd_body, add_prompt)
            elif ferm_type == "'L'" or ferm_type == "'D'" or ferm_type == "'U'" or ferm_type == "'Y'" or ferm_type == "'J'" or ferm_type == "'F'" or ferm_type == "'O'":
                ferm_pg = None
                while ferm_pg == None:
                    ferm_temp = input("Specific Gravity: ")
                    try:
                        ferm_pg = Decimal(ferm_temp)
                    except decimal.InvalidOperation:
                        print("Specific gravity must be a numeric value.")
                ferm_pg = round(ferm_pg, 3)
                ferm_temp = str(ferm_pg)
                misc.cls()
                fadd_body[3] = (None, ('Specific Gravity: ' + ferm_temp))
                screen = format_list(fadd_head, fadd_body, add_prompt)
            else:
                misc.cls()
                screen = format_list('Potential/Specific Gravity Requires a Type', fadd_body, add_prompt)
        elif next_screen == 'ferm_col':
            create_loop = True
            ferm_col = None
            while ferm_col == None:
                ferm_temp = input("Colour Contribution: ")
                try:
                    ferm_col = Decimal(ferm_temp)
                except decimal.InvalidOperation:
                    print("Colour contribution must be a numeric value.")
            ferm_col = round(ferm_col, 2)
            ferm_temp = str(ferm_col)
            misc.cls()
            fadd_body[4] = (None, ('Colour Contribution: ' + ferm_temp + ' Lovibond'))
            screen = format_list(fadd_head, fadd_body, add_prompt)
        elif next_screen == 'ferm_dp':
            create_loop = True
            if ferm_type == "'B'" or ferm_type == "'S'" or ferm_type == "'A'":
                ferm_dp = None
                while ferm_dp == None:
                    ferm_temp = input("Diastatic Power: ")
                    try:
                        ferm_dp = Decimal(ferm_temp)
                    except decimal.InvalidOperation:
                        print("Diastatic power must be a numeric value.")
                ferm_dp = round(ferm_dp, 1)
                ferm_temp = str(ferm_dp)
                misc.cls()
                fadd_body[5] = (None, ('Diastatic Power: ' + ferm_temp + ' Litner'))
                screen = format_list(fadd_head, fadd_body, add_prompt)
            else:
                misc.cls()
                screen = format_list('Diastatic Power Requires Type "Base Malt", "Specialty Malt", or "Adjunct"', fadd_body, add_prompt)
        elif next_screen == 'ferm_pc':
            create_loop = True
            if ferm_type == "'B'" or ferm_type == "'S'" or ferm_type == "'A'":
                ferm_pc = None
                while ferm_pc == None:
                    ferm_temp = input("Protein Content %: ")
                    try:
                        ferm_pc = Decimal(ferm_temp)
                    except decimal.InvalidOperation:
                        print("Protein content must be a numeric value.")
                ferm_pc = round(ferm_pc, 1)
                ferm_temp = str(ferm_pc)
                misc.cls()
                fadd_body[6] = (None, ('Protein Content: ' + ferm_temp + '%'))
                screen = format_list(fadd_head, fadd_body, add_prompt)
            else:
                misc.cls()
                screen = format_list('Protein Content Requires Type "Base Malt", "Specialty Malt", or "Adjunct"', fadd_body, add_prompt)
        elif next_screen == 'ferm_price':
            create_loop = True
            ferm_price = None
            while ferm_price == None:
                ferm_temp = input("Price: ")
                try:
                    ferm_price = Decimal(ferm_temp)
                except decimal.InvalidOperation:
                    print("Price must be a numeric value.")
            ferm_price = round(ferm_price, 2)
            ferm_temp = str(ferm_price)
            misc.cls()
            fadd_body[7] = (None, ('Price: $' + ferm_temp))
            screen = format_list(fadd_head, fadd_body, add_prompt)
        elif next_screen == 'ferm_qty':
            create_loop = True
            ferm_qty = None
            while ferm_qty == None:
                ferm_temp = input("Inventory Quantity: ")
                try:
                    ferm_qty = Decimal(ferm_temp)
                except decimal.InvalidOperation:
                    print("Quantity must be a numeric value.")
            ferm_qty = round(ferm_qty, 2)
            ferm_temp = str(ferm_qty)
            misc.cls()
            fadd_body[8] = (None, ('Inventory Quantity: ' + ferm_temp + ' lbs'))
            screen = format_list(fadd_head, fadd_body, add_prompt)
        elif next_screen == 'ferm_notes':
            create_loop = True
            fnotes_lst = []
            fnotes_loop = 0
            ferm_notes = input("Notes: ")
            for i in ferm_notes:
                fnotes_lst.append(i)
                fnotes_loop += 1
                if fnotes_loop == 25:
                    break
            fnotes_display = ''.join(fnotes_lst)
            misc.cls()
            fadd_body[9] = (None, (fnotes_display + '...'))
            screen = format_list(fadd_head, fadd_body, add_prompt)
            ferm_notes = form.sql_sanitize(ferm_notes)
            ferm_notes = form.quote_str(ferm_notes)
        elif next_screen == 'ferm_save':
            try:
                create_loop = False
                next_screen = 'ferm'
                db_curs = hs_db.cursor()
                query_str = 'INSERT INTO fermentables(ferm_name, ferm_origin, ferm_type, potential_gravity, colour, diastatic_power, protein_content, ferm_price, ferm_qty, ferm_notes) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(ferm_name, ferm_origin, ferm_type, ferm_pg, ferm_col, ferm_dp, ferm_pc, ferm_price, ferm_qty, ferm_notes)
                db_curs.execute(query_str)
                hs_db.commit()
                db_curs.close()
            except mysql.connector.errors.IntegrityError:
                create_loop = True
                misc.cls()
                screen = format_list('Fermentable Name Required', fadd_body, add_prompt)
            except mysql.connector.errors.DataError:
                create_loop = True
                misc.cls()
                screen = format_list('Invalid data. Double check potential gravity, colour, diastatic power, protein content, price, and quantity.', fadd_body, add_prompt)

        else: 
            create_loop = False

    # return the screen data if next screen doesn't require a db query
    if type(next_screen) == str:
        if next_screen == 'main':
            return [next_screen, main_head, main_body, main_prompt]
        elif next_screen == 'ing':
            return [next_screen, ing_head, ing_body, ing_prompt]
        elif next_screen == 'hop_add':
            return [next_screen, hadd_head, hop_cr.body, add_prompt]
        elif next_screen == 'yst_add':
            return [next_screen, yadd_head, yadd_body, add_prompt]
        elif next_screen == 'ferm_add':
            return [next_screen, fadd_head, fadd_body, add_prompt]
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