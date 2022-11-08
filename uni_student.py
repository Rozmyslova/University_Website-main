from correct_enter import correct_last_name
from for_student import find_group
from user_interface import student_choice
from user_timetable import timetable_for_student
from user_interface import export_data
from export import export_stud_timetable
from for_student import find_prof
from export import export_list_prof
from for_student import print_hw
from export import export_my_hw
from for_student import print_mark
from export import export_my_mark
from for_student import choice_subject


def operation_for_student():
    us = "student"
    last_name = correct_last_name(us)
    group = find_group(last_name)
    student_op = True
    while student_op:
        operation = student_choice()
        if operation == '1':
            print(f"Расписание студента: {last_name}")
            timetable_st = timetable_for_student(group)
            export_ttable = export_data()
            if export_ttable == '1':
                export_stud_timetable(last_name, timetable_st)
            print('Файл stud_timetable.txt экспортирован')
        elif operation == '2':
            print(f"Список всех преподавателей студента: {last_name}")
            f_prof = find_prof(group)
            export_list_pr = export_data()
            if export_list_pr == '1':
                export_list_prof(last_name, f_prof)
            print('Файл list_professor.txt экспортирован')
        elif operation == '3':
            subject = choice_subject(last_name, group)
            print(f"Ведомость оценок по предмету {subject} и посещения студента: {last_name}")
            mark_of_sub = print_mark(last_name, group, subject)
            print(mark_of_sub)
            export_mark = export_data()
            if export_mark == '1':
                export_my_mark(mark_of_sub, subject)
            print('Файл my_mark.txt экспортирован')
        elif operation == '4':
            subject = choice_subject(last_name, group)
            hw_print = print_hw(group, subject)
            for k in hw_print:
                print(hw_print[k])
            export_hw = export_data()
            if export_hw == '1':
                export_my_hw(hw_print, subject, last_name)
            print('Файл my_hw.txt экспортирован')
        else:
            break
