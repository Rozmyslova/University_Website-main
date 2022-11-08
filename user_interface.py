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
                2 - работа с группами;\n\
                3 - выйти из этого меню")
        op = input("Выберите желаемое действие: ")
        your_choice = True
    return op


def choice_func(func):
    your_choice = False
    while not your_choice:
        op = input(f"Выберите {func} для работы - введите цифру: ")
        your_choice = True
    return int(op)


def choice_gr_list_hw():
    your_choice = False
    while not your_choice:
        print("Вы хотите:\n\
                1 - поработать с ведомостями;\n\
                2 - работа с домашним заданием")
        op = input("Выберите желаемое действие: ")
        your_choice = True
    return op


def choice_gr():
    your_choice = False
    while not your_choice:
        print("Вы хотите:\n\
                1 - вывести на экран;\n\
                2 - редактировать")
        op = input("Выберите желаемое действие: ")
        your_choice = True
    return op


def work_group():
    your_choice = False
    while not your_choice:
        print("Вы хотите:\n\
                1 - скорректировать;\n\
                2 - выйти из этого меню")
        op = input("Выберите желаемое действие: ")
        your_choice = True
    return op


def do_it():
    your_choice = False
    while not your_choice:
        print("Вы сделали это?\n\
                    1 - да;\n\
                    2 - нет")
        op = input("Ваш ответ: ")
        if op != '1':
            print("Скорректируйте файл!")
        else:
            your_choice = True
    return op


def student_choice():
    your_choice = False
    while not your_choice:
        print("Вы хотите:\n\
                1 - посмотреть свое расписание;\n\
                2 - посмотреть всех своих преподавателей;\n\
                3 - посмотреть ведомость оценок и посещения;\n\
                4 - посмотреть дз и сроки сдачи;\n\
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
