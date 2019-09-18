import main_func
from hstack_classes import MiniHop

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
    search_cursor.execute("SELECT hop_id, hop_name FROM hops WHERE (hop_notes LIKE '%" + query + "%' OR hop_name LIKE '%" + query + "%');")

    h_details = search_cursor.fetchone()
    while h_details != None:
        h_list.append(MiniHop(h_details[0], h_details[1]))
        print(str(x + 1) + '. ' + h_list[x].name)
        h_details = search_cursor.fetchone()
        x += 1
    print('')
    print(str(x + 1) + ". Hop List")
    hop_select = input("Select Hop: ")

    if hop_select <= x:
        db_num = h_list[(x-1)].db_id
    elif hop_select == str(x + 1):
        main_func.cls()
        hop_list(search_cursor)