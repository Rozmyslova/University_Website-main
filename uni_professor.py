from professors import professor
from correct_enter import correct_last_name
from timetable import timetable
from user_interface import professor_choice
from user_timetable import timetable_for_professor
from user_interface import export_data
from export import export_prof_timetable
from working_with_group import subject_selection
from user_interface import choice_func
from working_with_group import group_prof_subj_selection
from import_list import import_list
from user_interface import work_group
from user_interface import do_it
from change_mark_list import change_mark


def operation_for_professor():
    us = "prof"
    last_name = correct_last_name(us)
    professor_op = True
    while professor_op:
        operation = professor_choice()
        if operation == '1':
            print(f"Расписание профессора: {last_name}")
            timetable_for_professor(last_name)
            export_prof_ttable = export_data()
            if export_prof_ttable == '1':
                export_prof_timetable(last_name)
        elif operation == '2':
            print(f"{last_name}, вы ведете следующие предметы")
            subj = list(enumerate(subject_selection(last_name)))
            for item in subj:
                print(item)
            function = "предмет"
            subject_ch = choice_func(function)
            subject = subj[subject_ch][1]
            print(f"Вы ведете предмет {subject} в следующих группах")
            group_subj = list(enumerate(group_prof_subj_selection(last_name, subject)))
            for item in group_subj:
                print(item)
            group_func = "группу"
            group_ch = choice_func(group_func)
            subject = group_subj[group_ch][1]
            print(subject)
            list_subject_gr = import_list(function, group_func)
            for keys, values in list_subject_gr.items():
                print(keys, ' | '.join(values))
            action = work_group()
            if action == '1':
                print("Вы хотите:\n\
                    1 - скорректировать файл и импортировать его;\n\
                    2 - внести изменения в программе")
                act = 'действие'
                list_action = choice_func(act)
                if list_action == '1':
                    print("скорректируйте файл группы и импортируйте его")
                    do_it()
                    list_subject_gr = import_list(function, group_func)
                    for keys, values in list_subject_gr.items():
                        print(keys, ' | '.join(values))
                else:
                    new_list_subject_gr = change_mark(list_subject_gr)
                    for keys, values in new_list_subject_gr.items():
                        print(keys, ' | '.join(values))




        else:
             break
