from professors import professor
from correct_enter import correct_last_name
from timetable import timetable
from user_interface import professor_choice
from prof_timetable import timetable_for_professor
from user_interface import export_data
from exp_prof_timetable import export_prof_timetable
from working_with_group import subject_selection
from user_interface import choice_func
from working_with_group import group_prof_subj_selection


def operation_for_professor():
    last_name = correct_last_name()
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


        else:
             break
