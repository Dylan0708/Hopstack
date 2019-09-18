import main_func
from hstack_classes import MiniHop, Hop

def note_format(note):
    note_list = []
    space_listen = False
    char_count = 0

    for i in note:
        char_count += 1
        if char_count == 70:
            space_listen = True
        if space_listen == True:
            if i == ' ':
                note_list.append('\n')
                space_listen = False
                char_count = 0
            else:
                note_list.append(i)
        else:
            note_list.append(i)

    note_formatted = ''.join(note_list)
    return note_formatted

def hop_list(h_cursor):
    h_cursor.execute("SELECT hop_id, hop_name FROM hops ORDER BY hop_name")
    x = 0
    h_list = []

    h_details = h_cursor.fetchone()
    while h_details != None:
        h_list.append(MiniHop(h_details[0], h_details[1]))
        print(str(x + 1) + '. ' + h_list[x].name)
        h_details = h_cursor.fetchone()
        x += 1
    print('')
    print(str(x + 1) + ". Ingredients Menu")
    print(str(x + 2) + ". Search")
    hop_select = input("Select Hop: ")

    if hop_select == str(x + 1):
        main_func.cls()
        return
    elif hop_select == str(x + 2):
        hop_search(h_cursor)


def hop_search(search_cursor):
    x = 0
    h_list = []

    query = input("Search Query: ")
    main_func.cls()
    search_cursor.execute("SELECT hop_id, hop_name FROM hops WHERE (hop_notes LIKE '%" + query + "%' OR hop_name LIKE '%" + query + "%')")

    h_details = search_cursor.fetchone()
    while h_details != None:
        h_list.append(MiniHop(h_details[0], h_details[1]))
        print(str(x + 1) + '. ' + h_list[x].name)
        h_details = search_cursor.fetchone()
        x += 1
    print('')
    print(str(x + 1) + ". Hop List")
    hop_select = input("Select Hop: ")

    if (int(hop_select) <= x) and (int(hop_select) > 0):
        main_func.cls()
        db_num = h_list[int(hop_select)-1].db_id
        hop_details(search_cursor, db_num)
    elif hop_select == str(x + 1):
        main_func.cls()
        hop_list(search_cursor)

def hop_details(det_cursor, id):
    det_cursor.execute("SELECT * FROM hops WHERE hop_id = " + str(id))
    sel_hop = det_cursor.fetchone()
    current_hop = Hop(sel_hop[0], sel_hop[1], sel_hop[2], sel_hop[3], sel_hop[4], sel_hop[5], sel_hop[6], sel_hop[7], sel_hop[8])

    if current_hop.origin != None:
        print(current_hop.name + ", " + current_hop.origin)
    else:
        print(current_hop.name)
    print("Price: $" + str(current_hop.price))
    print("Current Qty: " + str(current_hop.qty))
    print('')
    if current_hop.h_type == 'A':
        print("Hop Type: Aroma")
    elif current_hop.h_type == 'B':
        print("Hop Type: Bittering")
    elif current_hop.h_type == 'O':
        print("Hop Type: Both")
    else:
        print("Hop Type: Unknown")
    print("Alpha Acid: " + str(current_hop.alpha) + "%")
    print("Beta Acid: " + str(current_hop.beta) + "%")
    print('')
    if current_hop.notes != None:
        note = note_format(current_hop.notes)
        print(note)

    input("Enter to Return to Hop List: ")
    hop_list(det_cursor)