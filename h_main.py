#take separate view components and format into a single string
def format_list(head, body, foot, prompt, type):
    grid_w = max(len(head), len(max(body, key = len)), len(max(foot, key = len)), len(prompt))
    head_w = len(head)
    head_space = []
    top_list = [' ']

    if (grid_w % 2) != 0:
        temp_gwidth = grid_w + 1
    else:
        temp_gwidth = grid_w

    if (head_w % 2) != 0:
        head_w += 1

    #find the relative position of the header based on the grid width and the header width
    h_pos = (temp_gwidth / 2) - (head_w / 2)

    #generate header with formatted spacing
    for _ in range(h_pos):
        head_space.append(' ')
    empty = ''.join(head_space)
    head_form = (empty + head + '\n').upper

    #generate grid top
    temp_gwidth = grid_w - 2
    for _ in range(temp_gwidth):
        top_list.append('_')
    top_list.append('\n')
    top_form = ''.join(top_list)





#loop = True

#while loop == True:
    #call format list with initial params
    #call draw list with initial params