from correct_enter import correct_last_name
from correct_enter import find_group
from user_interface import student_choice
from user_timetable import timetable_for_student
from user_interface import export_data
from export import export_stud_timetable
from info_for_student import list_of_mark_visit


def operation_for_student():
    us = "student"
    last_name = correct_last_name(us)
    group = find_group(last_name)
    student_op = True
    while student_op:
        operation = student_choice()
        if operation == '1':
            print(f"Расписание студента: {last_name}")
            timetable_for_student(group)
            export_ttable = export_data()
            if export_ttable == '1':
                export_stud_timetable(last_name)
                print('Файл stud_timetable.txt экспортирован')
        elif operation == '2':
            list_of_mark_visit(last_name, group)




            """print(f"{last_name}, вы ведете следующие предметы")
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
                        print(keys, ' | '.join(values))"""




        else:
             break