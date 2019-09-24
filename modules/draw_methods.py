from modules import misc_methods as misc

def get_next(current, selection, list_lngth, raw):
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
            go_next = 'all'
        elif selection == '7':
            go_next = 'main'
        else:
            misc.cls()
            go_next = None
    elif current == 'hop':
        if int(selection) <= (list_lngth - 3) and int(selection) > 0:
            go_next = [raw[int(selection) - 1][0]]
        elif int(selection) == list_lngth - 2:
            go_next = 'ing'
        elif int(selection) == list_lngth - 1:
            go_next = 'main'
        elif int(selection) == list_lngth:
            go_next = 'srch'
        else:
            misc.cls()
            go_next = None

    return go_next

def get_body(table, param, connection):
    next_body = []
    next_foot = [(None, 'Ingredients'), (None, 'Main Menu'), (None, 'Search')]

    # put params in proper terms for the db query
    if table == 'hop':
        table = 'hops '
        columns = 'hop_id, hop_name '
        order = 'hop_name'
    elif table == 'yst':
        table = 'yeast'
    elif table == 'ferm':
        table = 'fermentables'
    elif table == 'msc':
        table = 'misc'

    # establish db cursor
    curs = connection.cursor(buffered = True)

    if param == 'all':
        curs.execute('SELECT ' + columns + 'FROM ' + table + 'ORDER BY ' + order)

    line = curs.fetchone()
    while line != None:
        next_body.append(line)
        line = curs.fetchone()
    
    next_body.extend(next_foot)
    
    return next_body