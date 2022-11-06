from user_interface import user_choice


def users():
    users_st = True
    while users_st:
        status = user_choice()
        if status == '1':
            print("1")
        elif status == '2':
            print("2")
        elif status == '3':
            
        else:
            break
