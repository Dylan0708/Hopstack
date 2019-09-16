from hstack_classes import MiniHop

def hop_list(h_cursor):
    h_cursor.execute("SELECT hop_id, hop_name FROM hops ORDER BY hop_name")
    x = 0
    hop_display = []

    h_details = h_cursor.fetchone()

    while h_details != None:
        hop_display.append(MiniHop(h_details[0], h_details[1], x + 1))
        print(hop_display[x].list_id, hop_display[x].name)
        h_details = h_cursor.fetchone()
        x += 1
    temp = input("temp")