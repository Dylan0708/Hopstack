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
        try:
            if int(selection) <= (list_lngth - 4) and int(selection) > 0:
                go_next = [raw[int(selection) - 1][0]]
            elif int(selection) == list_lngth - 3:
                go_next = 'ing'
            elif int(selection) == list_lngth - 2:
                go_next = 'main'
            elif int(selection) == list_lngth - 1:
                go_next = 'hop_add'
            elif int(selection) == list_lngth:
                go_next = 'hop_srch'
            else:
                misc.cls()
                go_next = None
        except ValueError:
            misc.cls()
            go_next = None
    elif current == 'hop_srch':
        if int(selection) <= (list_lngth - 3) and int(selection) > 0:
            go_next = [raw[int(selection) - 1][0]]
        elif int(selection) == list_lngth - 2:
            go_next = 'ing'
        elif int(selection) == list_lngth - 1:
            go_next = 'main'
        elif int(selection) == list_lngth:
            go_next = 'hop'
        else:
            misc.cls()
            go_next = None
    elif current == 'hop_det':
        if selection == '1':
            go_next = 'hop'
        elif selection == '2':
            go_next = 'hop_update'
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
    elif current == 'yst':
        try:
            if int(selection) <= (list_lngth - 4) and int(selection) > 0:
                go_next = [raw[int(selection) - 1][0]]
            elif int(selection) == list_lngth - 3:
                go_next = 'ing'
            elif int(selection) == list_lngth - 2:
                go_next = 'main'
            elif int(selection) == list_lngth - 1:
                go_next = 'yst_add'
            elif int(selection) == list_lngth:
                go_next = 'yst_srch'
            else:
                misc.cls()
                go_next = None
        except ValueError:
            misc.cls()
            go_next = None
    elif current == 'yst_srch':
        if int(selection) <= (list_lngth - 3) and int(selection) > 0:
            go_next = [raw[int(selection) - 1][0]]
        elif int(selection) == list_lngth - 2:
            go_next = 'ing'
        elif int(selection) == list_lngth - 1:
            go_next = 'main'
        elif int(selection) == list_lngth:
            go_next = 'yst'
        else:
            misc.cls()
            go_next = None
    elif current == 'yst_det':
        if selection == '1':
            go_next = 'yst'
        elif selection == '2':
            go_next = 'yst_update'
        elif selection == '3':
            misc.cls()
            loop = True
            while loop == True:
                misc.cls()
                print("Delete " + raw[1] + "? Y/N")
                verify = input()
                if verify.lower() == 'y':
                    go_next = 'yst_del'
                    loop = False
                elif verify.lower() == 'n':
                    go_next = [raw[0]]
                    loop = False
                else:
                    loop = True
        else:
            misc.cls()
            go_next = None
    elif current == 'yst_add':
        if selection == '1':
            go_next = 'yst_name'
        elif selection == '2':
            go_next = 'yst_ar'
        elif selection == '3':
            go_next = 'yst_prid'
        elif selection == '4':
            go_next = 'yst_lab'
        elif selection == '5':
            go_next = 'yst_type'
        elif selection == '6':
            go_next = 'yst_alc'
        elif selection == '7':
            go_next = 'yst_floc'
        elif selection == '8':
            go_next = 'yst_minatt'
        elif selection == '9':
            go_next = 'yst_maxatt'
        elif selection == '10':
            go_next = 'yst_mintmp'
        elif selection == '11':
            go_next = 'yst_maxtmp'
        elif selection == '12':
            go_next = 'yst_price'
        elif selection == '13':
            go_next = 'yst_qty'
        elif selection == '14':
            go_next = 'yst_notes'
        elif selection == '15':
            go_next = 'yst_save'
        elif selection == '16':
            go_next = 'yst'
        else:
            misc.cls()
            go_next = None
    elif current == 'ferm':
        try:
            if int(selection) <= (list_lngth - 4) and int(selection) > 0:
                go_next = [raw[int(selection) - 1][0]]
            elif int(selection) == list_lngth - 3:
                go_next = 'ing'
            elif int(selection) == list_lngth - 2:
                go_next = 'main'
            elif int(selection) == list_lngth - 1:
                go_next = 'ferm_add'
            elif int(selection) == list_lngth:
                go_next = 'ferm_srch'
            else:
                misc.cls()
                go_next = None
        except ValueError:
            misc.cls()
            go_next = None
    elif current == 'ferm_srch':
        if int(selection) <= (list_lngth - 3) and int(selection) > 0:
            go_next = [raw[int(selection) - 1][0]]
        elif int(selection) == list_lngth - 2:
            go_next = 'ing'
        elif int(selection) == list_lngth - 1:
            go_next = 'main'
        elif int(selection) == list_lngth:
            go_next = 'ferm'
        else:
            misc.cls()
            go_next = None
    elif current == 'ferm_det':
        if selection == '1':
            go_next = 'ferm'
        elif selection == '2':
            go_next = 'ferm_update'
        elif selection == '3':
            misc.cls()
            loop = True
            while loop == True:
                misc.cls()
                print("Delete " + raw[1] + "? Y/N")
                verify = input()
                if verify.lower() == 'y':
                    go_next = 'ferm_del'
                    loop = False
                elif verify.lower() == 'n':
                    go_next = [raw[0]]
                    loop = False
                else:
                    loop = True
        else:
            misc.cls()
            go_next = None
    elif current == 'ferm_add':
        if selection == '1':
            go_next = 'ferm_name'
        elif selection == '2':
            go_next = 'ferm_origin'
        elif selection == '3':
            go_next = 'ferm_type'
        elif selection == '4':
            go_next = 'ferm_pg'
        elif selection == '5':
            go_next = 'ferm_col'
        elif selection == '6':
            go_next = 'ferm_dp'
        elif selection == '7':
            go_next = 'ferm_pc'
        elif selection == '8':
            go_next = 'ferm_price'
        elif selection == '9':
            go_next = 'ferm_qty'
        elif selection == '10':
            go_next = 'ferm_notes'
        elif selection == '11':
            go_next = 'ferm_save'
        elif selection == '12':
            go_next = 'ferm'
        else:
            misc.cls()
            go_next = None
    elif current == 'wat':
        try:
            if int(selection) <= (list_lngth - 4) and int(selection) > 0:
                go_next = [raw[int(selection) - 1][0]]
            elif int(selection) == list_lngth - 3:
                go_next = 'ing'
            elif int(selection) == list_lngth - 2:
                go_next = 'main'
            elif int(selection) == list_lngth - 1:
                go_next = 'wat_add'
            elif int(selection) == list_lngth:
                go_next = 'wat_srch'
            else:
                misc.cls()
                go_next = None
        except ValueError:
            misc.cls()
            go_next = None 
    elif current == 'wat_srch':
        if int(selection) <= (list_lngth - 3) and int(selection) > 0:
            go_next = [raw[int(selection) - 1][0]]
        elif int(selection) == list_lngth - 2:
            go_next = 'ing'
        elif int(selection) == list_lngth - 1:
            go_next = 'main'
        elif int(selection) == list_lngth:
            go_next = 'wat'
        else:
            misc.cls()
            go_next = None
    elif current == 'wat_det':
        if selection == '1':
            go_next = 'wat'
        elif selection == '2':
            go_next = 'wat_update'
        elif selection == '3':
            misc.cls()
            loop = True
            while loop == True:
                misc.cls()
                print("Delete " + raw[1] + "? Y/N")
                verify = input()
                if verify.lower() == 'y':
                    go_next = 'wat_del'
                    loop = False
                elif verify.lower() == 'n':
                    go_next = [raw[0]]
                    loop = False
                else:
                    loop = True
        else:
            misc.cls()
            go_next = None
    elif current == 'wat_add':
        if selection == '1':
            go_next = 'wat_name'
        elif selection == '2':
            go_next = 'wat_ph'
        elif selection == '3':
            go_next = 'wat_ca'
        elif selection == '4':
            go_next = 'wat_mg'
        elif selection == '5':
            go_next = 'wat_na'
        elif selection == '6':
            go_next = 'wat_so4'
        elif selection == '7':
            go_next = 'wat_cl'
        elif selection == '8':
            go_next = 'wat_hco3'
        elif selection == '9':
            go_next = 'wat_price'
        elif selection == '10':
            go_next = 'wat_qty'
        elif selection == '11':
            go_next = 'wat_notes'
        elif selection == '12':
            go_next = 'wat_save'
        elif selection == '13':
            go_next = 'wat'
        else:
            misc.cls()
            go_next = None
    elif current == 'msc':
        try:
            if int(selection) <= (list_lngth - 4) and int(selection) > 0:
                go_next = [raw[int(selection) - 1][0]]
            elif int(selection) == list_lngth - 3:
                go_next = 'ing'
            elif int(selection) == list_lngth - 2:
                go_next = 'main'
            elif int(selection) == list_lngth - 1:
                go_next = 'msc_add'
            elif int(selection) == list_lngth:
                go_next = 'msc_srch'
            else:
                misc.cls()
                go_next = None
        except ValueError:
            misc.cls()
            go_next = None 
    elif current == 'msc_srch':
        if int(selection) <= (list_lngth - 3) and int(selection) > 0:
            go_next = [raw[int(selection) - 1][0]]
        elif int(selection) == list_lngth - 2:
            go_next = 'ing'
        elif int(selection) == list_lngth - 1:
            go_next = 'main'
        elif int(selection) == list_lngth:
            go_next = 'msc'
        else:
            misc.cls()
            go_next = None
    elif current == 'msc_det':
        if selection == '1':
            go_next = 'msc'
        elif selection == '2':
            go_next = 'msc_update'
        elif selection == '3':
            misc.cls()
            loop = True
            while loop == True:
                misc.cls()
                print("Delete " + raw[1] + "? Y/N")
                verify = input()
                if verify.lower() == 'y':
                    go_next = 'msc_del'
                    loop = False
                elif verify.lower() == 'n':
                    go_next = [raw[0]]
                    loop = False
                else:
                    loop = True
        else:
            misc.cls()
            go_next = None
    elif current == 'msc_add':
        if selection == '1':
            go_next = 'msc_name'
        elif selection == '2':
            go_next = 'msc_unit'
        elif selection == '3':
            go_next = 'msc_type'
        elif selection == '4':
            go_next = 'msc_price'
        elif selection == '5':
            go_next = 'msc_qty'
        elif selection == '6':
            go_next = 'msc_notes'
        elif selection == '7':
            go_next = 'msc_save'
        elif selection == '8':
            go_next = 'msc'
        else:
            misc.cls()
            go_next = None

    return go_next

def get_body(table, param, connection, current = None):
    next_body = []

    # put params in proper terms for the db query
    if table == 'hop' or table == 'hop_det' or table == 'hop_srch':
        table = 'hops '
        columns = 'hop_id, hop_name, hop_origin '
        order = 'hop_name'
        db_id = 'hop_id '
        foot_add = 'Add Hop'
        srch_params = ' hop_notes LIKE "%{}%" OR hop_name LIKE "%{}%" OR hop_origin LIKE "%{}%"'.format(param, param, param)
    elif table == 'yst' or table == 'yst_det' or table == 'yst_srch':
        table = 'yeast '
        columns = 'yeast_id, yeast_name, lab '
        order = 'yeast_name'
        db_id = 'yeast_id '
        foot_add = 'Add Yeast'
        srch_params = ' yeast_notes LIKE "%{}%" OR yeast_name LIKE "%{}%" OR lab LIKE "%{}%"'.format(param, param, param)
    elif table == 'ferm' or table == 'ferm_det' or table == 'ferm_srch':
        table = 'fermentables '
        columns = 'ferm_id, ferm_name, ferm_origin '
        order = 'ferm_name'
        db_id = 'ferm_id '
        foot_add = 'Add Fermentable'
        srch_params = ' ferm_notes LIKE "%{}%" OR ferm_name LIKE "%{}%" OR ferm_origin LIKE "%{}%"'.format(param, param, param)
    elif table == 'wat' or table == 'wat_det' or table == 'wat_srch':
        table = 'water '
        columns = 'water_id, water_name '
        order = 'water_name'
        db_id = 'water_id '
        foot_add = 'Add Water'
        srch_params = ' water_notes LIKE "%{}%" OR water_name LIKE "%{}%"'.format(param, param)
    elif table == 'msc' or table == 'msc_det' or table == 'msc_srch':
        table = 'misc '
        columns = 'misc_id, misc_name '
        order = 'misc_name'
        db_id = 'misc_id '
        foot_add = 'Add Misc'
        srch_params = ' misc_notes LIKE "%{}%" OR misc_name LIKE "%{}%"'.format(param, param)

    # establish db cursor
    curs = connection.cursor(buffered = True)

    if type(param) == str:
        if param == 'all':
            curs.execute('SELECT ' + columns + 'FROM ' + table + 'ORDER BY ' + order)
            next_foot = [(None, 'Ingredients'), (None, 'Main Menu'), (None, foot_add), (None, 'Search')]
        else:
            curs.execute('SELECT ' + columns + 'FROM ' + table + 'WHERE (' + srch_params + ') ORDER BY ' + order)
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