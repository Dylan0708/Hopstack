def format_body(messy_body):
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
            elif messy_body[j][i] == None:
                del temp_list[-1]
        str_element = ''.join(temp_list)
        new_list.append(str_element)
        temp_list.clear()

    form_width = len(max(new_list, key = len))

    for k in range(len(new_list)):
        temp_list.append('|')
        temp_list.append(new_list[k])
        if len(new_list[k]) < form_width:
            loop_num = form_width - len(new_list[k])
            for l in range(loop_num):
                temp_list.append(' ')
        temp_list.append('|')
        temp_list.append('\n')
        form_element = ''.join(temp_list)
        form_list.append(form_element)
        temp_list.clear()

    str_form = ''.join(form_list)

    print(str_form)
    print(form_width)