def user_choice():
    your_choice = False
    while not your_choice:
        print("Вы являетесь:\n\
                1 - преподавателем;\n\
                2 - студентом;\n\
                3 - абитуриентом\n\
                4 - выход из программы")
        us = input("Выберите цифру, соответствующую вашему статусу: ")
        your_choice = True
    return us