from user_interface import choice_func


def change_mark(list_gr):
    list_sub_gr = list_gr
    print(list_sub_gr.keys())
    correct = False
    while not correct:
        st_name = input('Введите фамилию и имя студента, как показано выше в соответствии с ключами (со всеми пробелами)  ')
        if st_name in list_sub_gr.keys():
            correct = True
        else:
            print("Проверьте, правильно ли введена фамилия")
            continue
    print("Вы хотите:\n\
                       1 - скорректировать оценку, которая уже выставлена;\n\
                       2 - добавить оценку по новому уроку")
    act = 'действие'
    action = choice_func(act)
    line = list(list_sub_gr[st_name])
    mark = input("Введите оценку ")
    new_list = {}
    if action == '1':
        lesson = input("Введите номер занятия, где хотите изменить оценку ")
        line[lesson-1] = mark
    else:
        line.append(mark)
    new_list.update({st_name: "|".join(line)})
    return new_list



