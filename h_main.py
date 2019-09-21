from modules import format_methods as form
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#take separate view components and format into a single string
def format_list(head, body, prompt):
    head_w = len(head)
    head_space = []
    top_grid = [' ']
    bottom_grid = ['|']

    #generate body with multiple line formatting using format_body
    alt_width = max(len(head), len(prompt))
    body_list = form.format_body(body, alt_width)
    grid_w = max(len(head), len(max(body_list, key = len)), len(prompt))
    body_form = ''.join(body_list)

    if (grid_w % 2) != 0:
        temp_gwidth = grid_w + 1
    else:
        temp_gwidth = grid_w

    if (head_w % 2) != 0:
        head_w += 1

    #find the relative position of the header based on the grid width and the header width
    h_pos = int((temp_gwidth / 2) - (head_w / 2))

    #generate header with formatted spacing
    for _ in range(h_pos):
        head_space.append(' ')
    empty = ''.join(head_space)
    head_form = (empty + head + '\n')

    #generate grid top
    temp_gwidth = grid_w - 3
    for _ in range(temp_gwidth):
        top_grid.append('_')
        bottom_grid.append('_')
    top_grid.append('\n')
    bottom_grid.append('|')
    bottom_grid.append('\n')
    top_form = ''.join(top_grid)
    bottom_form = ''.join(bottom_grid)

    #stitch all the formatted pieces together into a single string
    screen_form = head_form + top_form + body_form + bottom_form + prompt

    return screen_form

loop = True

while loop == True:
    #call format list with initial params
    #call draw list with initial params