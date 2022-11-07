def user_choice():
    your_choice = False
    while not your_choice:
        print("Вы являетесь:\n\
                1 - преподавателем;\n\
                2 - студентом;\n\
                3 - абитуриентом\n\
                4 - выход из программы")
        user = input("Выберите цифру, соответствующую вашему статусу: ")
        your_choice = True
    return user


def professor_choice():
    your_choice = False
    while not your_choice:
        print("Вы хотите:\n\
                1 - посмотреть свое расписание;\n\
                2 - просмотреть даты вступительных испытаний;\n\
                3 - просмотреть минимальные проходные баллы;\n\
                4 - просмотреть список документов для поступления;\n\
                5 - выйти из этого меню")
        op = input("Выберите желаемое действие: ")
        your_choice = True
    return op


def entrant_choice():
    your_choice = False
    while not your_choice:
        print("Вы хотите:\n\
                1 - посмотреть список специальностей;\n\
                2 - посмотреть даты вступительных испытаний;\n\
                3 - посмотреть минимальные проходные баллы;\n\
                4 - посмотреть список документов для поступления;\n\
                5 - выйти из этого меню")
        op = input("Выберите желаемое действие: ")
        your_choice = True
    return op


def export_data():
    your_choice = False
    while not your_choice:
        print("Вы хотите сохранить эти данные в файле?\n\
                    1 - да;\n\
                    2 - нет")
        op = input("Выберите желаемое действие: ")
        your_choice = True
    return op
