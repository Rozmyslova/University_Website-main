from user_timetable import timetable_for_professor
from user_timetable import timetable_for_student
from for_entrant import list_of_program
from for_entrant import date_of_ent_exam
from for_entrant import min_score_of_exam
from for_entrant import list_of_documents
from for_student import find_prof
from for_student import print_hw


def export_prof_timetable(name):
    table = timetable_for_professor(name)
    last_name = name
    with open('prof_timetable.txt', 'w', encoding="utf-8") as p_tt:
        p_tt.write(f"Расписание профессора: {last_name} \n")
        for key, val in table.items():
            p_tt.write('{}:{}\n'.format(key, val))


def export_stud_timetable(name, tt):
    table = tt
    last_name = name
    with open('stud_timetable.txt', 'w', encoding="utf-8") as p_tt:
        p_tt.write(f"Расписание студента: {last_name} \n")
        for key, val in table.items():
            p_tt.write('{}:{}\n'.format(key, val))


def export_list_of_program():
    l_of_pr = list_of_program()
    with open('list_of_program.txt', 'w', encoding="utf-8") as l_pr:
        l_pr.write("Перечень программ нашего университета\n")
        for key, val in l_of_pr.items():
            l_pr.write('{}:{}\n'.format(key, val))


def export_date_of_exam():
    d_of_ex = date_of_ent_exam()
    with open('date_of_exam.txt', 'w', encoding="utf-8") as d_ex:
        d_ex.write("Даты вступительных испытаний нашего университета\n")
        for key, val in d_of_ex.items():
            d_ex.write('{}:{}\n'.format(key, val))


def export_min_score():
    min_sc = min_score_of_exam()
    with open('min_score.txt', 'w', encoding="utf-8") as m_sc:
        m_sc.write("Минимальные проходные баллы\n")
        for key, val in min_sc.items():
            m_sc.write('{}:{}\n'.format(key, val))


def export_list_of_doc():
    l_of_d = list_of_documents()
    with open('list_of_documents.txt', 'w', encoding="utf-8") as l_d:
        l_d.write("Даты вступительных испытаний нашего университета\n")
        for key, val in l_of_d.items():
            l_d.write('{}:{}\n'.format(key, val))


def export_list_prof(name, f_p):
    l_prof = f_p
    last_name = name
    with open('list_professor.txt', 'w', encoding="utf-8") as l_pr:
        l_pr.write(f"Список всех преподавателей студента: {last_name} \n")
        for key, val in l_prof.items():
            l_pr.write('{}:{}\n'.format(key, val))


def export_my_hw(hw, sub, name):
    hw = hw
    with open('my_hw.txt', 'w', encoding="utf-8") as m_hw:
        m_hw.write(f"Домашнее задание для студента {name} по предмету {sub} \n")
        for key, val in hw.items():
            m_hw.write('{}:{}\n'.format(key, val))


def export_my_mark(mark, sub):
    mark_of_sub = mark
    with open('my_mark.txt', 'w', encoding="utf-8") as m_mark:
        m_mark.write(f"Оценки студента по предмету {sub}  \n")
        for key, val in mark_of_sub.items():
            m_mark.write('{} {}\n'.format(key, val))
