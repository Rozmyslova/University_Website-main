from professors import professor
from students import student


def correct_last_name(users):
    prof = professor()
    stud = student()
    correct_l_name = False
    while not correct_l_name:
        l_name = input("Введите свою фамилию, например, Иванов: ")
        if users == "prof":
            for k in prof:
                for v in prof[k]:
                    if l_name in v:
                        return l_name
        else:
            for k in stud:
                for v in stud[k]:
                    if l_name in v:
                        return l_name
        if l_name not in prof.values() or stud.values():
            print("Нет пользователя с такой фамилией. Проверьте, правильно ли она написана")
            continue
        else:
            return str(l_name)


def find_group(name):
    last_name = name
    stud = student()
    for k in stud.keys():
        if last_name in stud[k]:
            line = list(stud[k])
            for i in line:
                if i == '104 группа':
                    group = '104 группа'
                else:
                    group = '203 группа'
    return group
