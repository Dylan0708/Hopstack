from modules import misc_methods as misc

def get_next(current, selection, list_lngth, raw, cur_data):
    if current == 'main':
        if selection == '1':
            go_next = 'inv'
        elif selection == '2':
            go_next = 'rec'
        elif selection == '3':
            go_next = 'shop'
        elif selection == '4':
            go_next = 'ing'
        elif selection == '5':
            go_next = 'log'
        elif selection == '6':
            go_next = 'exit'
        else:
            misc.cls()
            go_next = None
    elif current == 'ing':
        if selection == '1':
            go_next = 'hop'
        elif selection == '2':
            go_next = 'yst'
        elif selection == '3':
            go_next = 'ferm'
        elif selection == '4':
            go_next = 'wat'
        elif selection == '5':
            go_next = 'msc'
        elif selection == '6':
            go_next = 'main'
        else:
            misc.cls()
            go_next = None
    elif current == 'hop':
        if int(selection) <= (list_lngth - 4) and int(selection) > 0:
            go_next = [raw[int(selection) - 1][0]]
        elif int(selection) == list_lngth - 3:
            go_next = 'ing'
        elif int(selection) == list_lngth - 2:
            go_next = 'main'
        elif int(selection) == list_lngth - 1:
            go_next = 'hop_add'
        elif int(selection) == list_lngth:
            go_next = 'srch'
        else:
            misc.cls()
            go_next = None
    elif current == 'srch':
        if int(selection) <= (list_lngth - 3) and int(selection) > 0:
            go_next = [raw[int(selection) - 1][0]]
        elif int(selection) == list_lngth - 2:
            go_next = 'ing'
        elif int(selection) == list_lngth - 1:
            go_next = 'main'
        elif int(selection) == list_lngth:
            if ('Hop Select' in cur_data) == True:
                go_next = 'hop'
        else:
            misc.cls()
            go_next = None
    elif current == 'hop_det':
        if selection == '1':
            go_next = 'hop'
        elif selection == '3':
            misc.cls()
            loop = True
            while loop == True:
                misc.cls()
                print("Delete " + raw[1] + "? Y/N")
                verify = input()
                if verify.lower() == 'y':
                    go_next = 'hop_del'
                    loop = False
                elif verify.lower() == 'n':
                    go_next = [raw[0]]
                    loop = False
                else:
                    loop = True
        else:
            misc.cls()
            go_next = None
    elif current == 'hop_add':
        if selection == '1':
            go_next = 'hop_name'
        elif selection == '2':
            go_next = 'hop_origin'
        elif selection == '3':
            go_next = 'hop_type'
        elif selection == '4':
            go_next = 'hop_alpha'
        elif selection == '5':
            go_next = 'hop_beta'
        elif selection == '6':
            go_next = 'hop_price'
        elif selection == '7':
            go_next = 'hop_qty'
        elif selection == '8':
            go_next = 'hop_notes'
        elif selection == '9':
            go_next = 'hop_save'
        elif selection == '10':
            go_next = 'hop'
        else:
            misc.cls()
            go_next = None

    return go_next

def get_body(table, param, connection, current = None):
    next_body = []

    # put params in proper terms for the db query
    if table == 'hop' or table == 'hop_det':
        table = 'hops '
        columns = 'hop_id, hop_name '
        order = 'hop_name'
        db_id = 'hop_id '
    elif table == 'yst':
        table = 'yeast'
    elif table == 'ferm':
        table = 'fermentables'
    elif table == 'msc':
        table = 'misc'
    elif table == 'srch':
        if current == 'hop':
            table = 'hops '
            columns = 'hop_id, hop_name '
            order = 'hop_name'
            db_id = 'hop_id'

    # establish db cursor
    curs = connection.cursor(buffered = True)

    if type(param) == str:
        if param == 'all':
            curs.execute('SELECT ' + columns + 'FROM ' + table + 'ORDER BY ' + order)
            if table == 'hops ':
                next_foot = [(None, 'Ingredients'), (None, 'Main Menu'), (None, 'Add Hop'), (None, 'Search')]
        else:
            curs.execute('SELECT ' + columns + 'FROM ' + table + 'WHERE (hop_notes LIKE "%' + param + '%" OR hop_name LIKE "%' + param + '%") ORDER BY ' + order)
            next_foot = [(None, 'Ingredients'), (None, 'Main Menu'), (None, 'Back')]
    else:
        curs.execute('SELECT * FROM ' + table + 'WHERE ' + db_id + '= ' + str(param))

    line = curs.fetchone()
    while line != None:
        next_body.append(line)
        line = curs.fetchone()
    
    curs.close()
    if type(param) == str:
        next_body.extend(next_foot)
        return next_body
    else:
        list_body = next_body[0]
        return list_body