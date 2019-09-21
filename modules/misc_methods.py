import readchar, os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def echo_char(prompt = None, echo_char = '.'):
    cursor_index = 0
    pass_list = []
    if prompt != None:
        print(prompt, end = '', flush = True)  # if there's a prompt, print it
    key_stroke = readchar.readkey()
    while key_stroke != readchar.key.ENTER:  # keep geting input until ENTER
        if key_stroke == '\x08':
            if cursor_index > 0:
                del pass_list[-1]
                print('\b \b', end = '', flush = True)  # move cursor back, overwrite with blank in event of
                cursor_index -= 1
        else:
            pass_list.append(key_stroke)
            print(echo_char, end = '', flush = True)  # echoes string to the console without newline
            cursor_index += 1
        key_stroke = readchar.readkey()
    secret = ''.join(pass_list)  # convert pass_list to a string to return
    return secret