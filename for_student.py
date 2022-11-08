from professors import professor
from students import student
from working_with_group import subject_selection
from user_interface import choice_func
from work_gr import list_print

from user_interface import export_data


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


def find_prof(gr):
    group = gr
    prof = professor()
    prof_list = {}
    for k in prof.keys():
        if group in prof[k]:
            line = list(prof[k])
            del line[3]
            print(" ".join(line))
            prof_list.update({k: " ".join(line)})
    return prof_list


def print_hw(name, gr):
    last_name = name
    group = gr
    choice_gr = '2'
    print(f"{last_name}, у вас есть следующие предметы")
    subj = list(enumerate(subject_selection(group)))
    for item in subj:
        print(item)
    function = "предмет"
    subject_ch = choice_func(function)
    subject = subj[subject_ch][1]
    list_subject_gr = list_print(subject, group, choice_gr)
    print(f"Домашнее задание по предмету {subject}")
    for keys, values in list_subject_gr.items():
        print(keys, ''.join(values))

