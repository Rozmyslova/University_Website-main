from user_timetable import timetable_for_professor
from user_timetable import  timetable_for_student


def export_prof_timetable(name):
    table = timetable_for_professor(name)
    last_name = name
    with open('prof_timetable.txt', 'w', encoding="utf-8") as p_tt:
        p_tt.write(f"Расписание профессора: {last_name} \n")
        for key, val in table.items():
            p_tt.write('{}:{}\n'.format(key, val))


def export_stud_timetable(name):
    table = timetable_for_student(name)
    last_name = name
    with open('stud_timetable.txt', 'w', encoding="utf-8") as p_tt:
        p_tt.write(f"Расписание студента: {last_name} \n")
        for key, val in table.items():
            p_tt.write('{}:{}\n'.format(key, val))
