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
        if char_count == 20:
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