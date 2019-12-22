def format_body(messy_body, tb_width):
    temp_list = []
    new_list = []
    form_list = []

    for j in range(len(messy_body)):
        temp_list.append(str(j + 1) + '. ')
        for i in range(len(messy_body[j])):
            if i > 0 and messy_body[j][i] != None:
                temp_list.append(str(messy_body[j][i]))
                if i != (len(messy_body[j]) - 1):
                    temp_list.append(', ')
            elif i > 0 and messy_body[j][i] == None:
                del temp_list[-1]
        str_element = ''.join(temp_list)
        new_list.append(str_element)
        temp_list.clear()

    form_width = max(len(max(new_list, key = len)), tb_width)

    for k in range(len(new_list)):
        temp_list.append('|')
        temp_list.append(new_list[k])
        if len(new_list[k]) < form_width:
            loop_num = form_width - len(new_list[k])
            for _ in range(loop_num):
                temp_list.append(' ')
        temp_list.append('|')
        temp_list.append('\n')
        form_element = ''.join(temp_list)
        form_list.append(form_element)
        temp_list.clear()

    return form_list

def note_format(note):
    is_space = False
    char_count = 0
    char_list = []
    str_list = []

    for i in note:
        char_count += 1
        if char_count == 70:
            is_space = True
        if is_space == True:
            if i == ' ':
                cur_str = ''.join(char_list)
                str_list.append(cur_str)
                is_space = False
                char_count = 0
                char_list = []
            else:
                char_list.append(i)
        else:
            char_list.append(i)
    cur_str = ''.join(char_list)
    str_list.append(cur_str)
    return str_list

def detail_title(details):
    titled_line = []
    line_items = len(details)
    del_index = []
    counter = 0
    if line_items == 6:  # hops
        # format each line
        if details[0] != None:
            titled_line.append('Hop Origin: ' + details[0])
        else:
            titled_line.append(None)

        if details[1] != None:
            if details[1] == 'A':
                titled_line.append('Hop Type: Aroma')
            elif details[1] == 'B':
                titled_line.append('Hop Type: Bittering')
            else:
                titled_line.append('Hop type: Bittering and/or Aroma')
        else:
            titled_line.append(None)
        
        if details[2] != None:
            titled_line.append('Alpha Acid Content: ' + str(details[2]) + '%')
        else:
            titled_line.append(None)

        if details[3] != None:
            titled_line.append('Beta Acid Content: ' + str(details[3]) + '%')
        else:
            titled_line.append(None)

        titled_line.append('Price: $' + str(details[4]) + ' per oz')
        titled_line.append('Inventory Quantity: ' + str(details[5]) + 'oz')
        titled_line.append('')

    elif line_items == 12: # yeast
        # format each line
        if details[0] != None:
            titled_line.append('Monthly Viability Loss: ' + str(details[0]) + '%')
        else:
            titled_line.append(None)

        if details[1] != None:
            titled_line.append('Product ID: ' + details[1])
        else:
            titled_line.append(None)

        if details[2] != None:
            titled_line.append('Lab: ' + details[2])
        else:
            titled_line.append(None)

        if details[3] != None:
            if details[3] == 'Ale':
                titled_line.append('Yeast Type: Ale (Saccharomyces Cerevisiae)')
            elif details[3] == 'Lag':
                titled_line.append('Yeast Type: Lager (Saccharomyces Pastorianus)')
            elif details[3] == 'Brt':
                titled_line.append('Yeast Type: Brett (Brettanomyces)')
            elif details[3] == 'Dia':
                titled_line.append('Yeast Type: Diastatic (Saccharomyces Cerevisiae var. Diastaticus)')
            elif details[3] == 'Ped':
                titled_line.append('Bacteria Type: Pediococcus')
            elif details[3] == 'Lac':
                titled_line.append('Bacteria Type: Lactobacillus')
            elif details[3] == 'Kvk':
                titled_line.append('Yeast Type: Kveik')
            else:
                titled_line.append('Yeast Type: Mixed Culture')
        else:
            titled_line.append(None)
        
        if details[4] != None:
            titled_line.append('Alcohol Tolerance: ' + str(details[4]) + '%')
        else:
            titled_line.append(None)
        
        if details[5] != None:
            if details[5] == 'L':
                titled_line.append('Flocculation: Low')
            elif details[5] == 'M':
                titled_line.append('Flocculation: Medium')
            else:
                titled_line.append('Flocculation: High')
        else:
            titled_line.append(None)
        
        if details[6] != None:
            titled_line.append('Minimum Attenuation: ' + str(details[6]) + '%')
        else:
            titled_line.append(None)

        if details[7] != None:
            titled_line.append('Maximum Attenuation: ' + str(details[7]) + '%')
        else:
            titled_line.append(None)

        if details[8] != None:
            titled_line.append('Minimum Temperature Tolerance: ' + str(details[8]) + '°C')
        else:
            titled_line.append(None)

        if details[9] != None:
            titled_line.append('Maximum Temperature Tolerance: ' + str(details[9]) + '°C')
        else:
            titled_line.append(None)
        
        titled_line.append('Price: $' + str(details[10]) + ' per Unit')
        titled_line.append('Inventory Quantity: ' + str(details[11]) + ' Units')
        titled_line.append('')
    elif line_items == 8: # fermentables
        # format each line
        if details[0] != None:
            titled_line.append('Origin: ' + details[0])
        else:
            titled_line.append(None)

        if details[1] != None:
            if details[1] == 'B':
                titled_line.append('Type: Base Malt')
            elif details[1] == 'S':
                titled_line.append('Type: Specialty Malt')
            elif details[1] == 'L':
                titled_line.append('Type: Liquid Extract')
            elif details[1] == 'D':
                titled_line.append('Type: Dry Extract')
            elif details[1] == 'U':
                titled_line.append('Type: Sugar')
            elif details[1] == 'Y':
                titled_line.append('Type: Syrup')
            elif details[1] == 'J':
                titled_line.append('Type: Juice')
            elif details[1] == 'F':
                titled_line.append('Type: Fruit')
            elif details[1] == 'A':
                titled_line.append('Type: Adjunct')
            elif details[1] == 'O':
                titled_line.append('Type: Other')
        else:
            titled_line.append(None)

        if details[2] != None:
            if details[1] == 'B' or details[1] == 'S' or details[1] == 'A':
                line_title = 'Base Gravity Potential: '
            elif details[1] == 'L' or details[1] == 'D' or details[1] == 'U' or details[1] == 'Y' or details[1] == 'J' or details[1] == 'F' or details[1] == 'O':
                line_title = 'Specific Gravity: '
            else:
                line_title = 'Base Gravity Potential/Specific Gravity: '
            titled_line.append(line_title + str(details[2]))
        else:
            titled_line.append(None)

        if details[3] != None:
            titled_line.append('Colour: ' + str(details[3]) + ' Lovibond')
        else:
            titled_line.append(None)

        if details[4] != None:
            if details[1] == 'B' or details[1] == 'S' or details[1] == 'A':
                titled_line.append('Diastatic Power: ' + str(details[4]) + ' Litner')
            else:
                titled_line.append(None)
        else:
            titled_line.append(None)
            
        if details[5] != None:
            if details[1] == 'B' or details[1] == 'S' or details[1] == 'A':
                titled_line.append('Protein Content: ' + str(details[5]) + '%')
            else:
                titled_line.append(None)
        else:
            titled_line.append(None)
        
        titled_line.append('Price: $' + str(details[6]) + ' per lb')
        titled_line.append('Inventory Quantity: ' + str(details[7]) + ' lbs')
        titled_line.append('')
    elif line_items == 9: # water
        # format each line
        if details[0] != None:
            titled_line.append('PH: ' + str(details[0]))
        else:
            titled_line.append(None)
            
        if details[1] != None:
            titled_line.append('Calcium: ' + str(details[1]) + ' ppm')
        else:
            titled_line.append(None)
        
        if details[2] != None:
            titled_line.append('Magnesium: ' + str(details[2]) + ' ppm')
        else:
            titled_line.append(None)

        if details[3] != None:
            titled_line.append('Sodium: ' + str(details[3]) + ' ppm')
        else:
            titled_line.append(None)

        if details[4] != None:
            titled_line.append('Sulfate: ' + str(details[4]) + ' ppm')
        else:
            titled_line.append(None)

        if details[5] != None:
            titled_line.append('Chloride: ' + str(details[5]) + ' ppm')
        else:
            titled_line.append(None)

        if details[6] != None:
            titled_line.append('Bicarbonate: ' + str(details[6]) + ' ppm')
        else:
            titled_line.append(None)

        titled_line.append('Price: $' + str(details[7]) + ' per gal')
        titled_line.append('Inventory Quantity: ' + str(details[8]) + ' gal')
        titled_line.append('')

    # get items to delete
    for i in titled_line:
        if i == None:
            del_index.append(counter)
        counter += 1

    # delete items
    for j in reversed(del_index):
        del titled_line[j]

    return titled_line

def head_spacing(width, head):
    head_space = []
    head_w = len(head)
    
    if (width % 2) != 0:
        temp_gwidth = width + 1
    else:
        temp_gwidth = width

    if (head_w % 2) != 0:
        head_w += 1

    # find the relative position of the header based on the grid width and the header width
    h_pos = int((temp_gwidth / 2) - (head_w / 2))

    # generate header with formatted spacing
    for _ in range(h_pos):
        head_space.append(' ')
    empty = ''.join(head_space)
    spaced_head = (empty + head + '\n')

    return spaced_head

def format_details(body, width):
    line_format = []
    body_form = []

    for i in body:
        line_format.append('|' + str(i))
        if len(str(i)) < width:
            for _ in range(width - len(str(i))):
                line_format.append(' ')
        line_format.append('|\n')
        line = ''.join(line_format)
        line_format = []
        body_form.append(line)
    
    body_str = ''.join(body_form)

    return body_str

def quote_str(string):
    str_elem = ["'"]
    
    for i in string:
        str_elem.append(i)

    str_elem.append("'")
    str_quoted = ''.join(str_elem)

    return str_quoted

def sql_sanitize(query):
    query_elem = []

    for i in query:
        query_elem.append(i)

        if i == '\\':
            query_elem.append('\\')
        elif i == "'":
            query_elem.append("'")
    
    sanit_str = ''.join(query_elem)

    return sanit_str