from professors import professor


def correct_last_name():
    prof = professor()
    correct_l_name = False
    while not correct_l_name:
        l_name = input("Введите свою фамилию, например, Иванов: ")
        for k in prof:
            for v in prof[k]:
                if l_name in v:
                    correct_l_name = True
                    return l_name


        if l_name not in prof.values():
            print("Нет пользователя с такой фамилией. Проверьте, правильно ли она написана")
            continue
        else:
            return str(l_name)
