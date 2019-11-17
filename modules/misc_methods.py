import readchar, os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def echo_char(prompt = None, echo_char = '.'):
    cursor_index = 0
    pass_list = []

    if prompt != None:
        # if there's a prompt, print it
        print(prompt, end = '', flush = True)

    key_stroke = readchar.readkey()
    # keep geting input until ENTER
    while key_stroke != readchar.key.ENTER:
        if key_stroke == '\x08':
            if cursor_index > 0:
                del pass_list[-1]
                # move cursor back, overwrite with blank in event of
                print('\b \b', end = '', flush = True)
                cursor_index -= 1
        else:
            pass_list.append(key_stroke)
            # echoes string to the console without newline
            print(echo_char, end = '', flush = True)
            cursor_index += 1
        key_stroke = readchar.readkey()
        
    # convert pass_list to a string to return
    secret = ''.join(pass_list)
    return secret
