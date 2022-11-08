from correct_enter import correct_last_name
from user_interface import professor_choice
from user_timetable import timetable_for_professor
from user_interface import export_data
from export import export_prof_timetable
from working_with_group import work_with_group


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
            print('Файл prof_timetable.txt экспортирован')
        elif operation == '2':
            work_with_group(last_name)
        else:
            professor_op = False
            #break
