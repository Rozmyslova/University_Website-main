from user_interface import user_choice
from uni_professor import operation_for_professor
from uni_entrant import operation_for_entrant


def users():
    users_st = True
    while users_st:
        status = user_choice()
        if status == '1':
            operation_for_professor()
        elif status == '2':
            print("2")
        elif status == '3':
            operation_for_entrant()
        else:
            break
