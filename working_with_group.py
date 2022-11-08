from professors import professor
from user_interface import choice_func
from user_interface import choice_gr_list_hw
from user_interface import choice_gr
from work_gr import list_print
from import_list import import_list

from user_interface import work_group
from user_interface import do_it
from change_mark_list import change_mark


def subject_selection(name):
    prof = professor()
    last_name = name
    subj_sel = []
    for k in prof.keys():
        if last_name in prof[k]:
            line = list(prof[k])
            subj_sel.append(line[2])
        set_sub_sel = set(subj_sel)
        subj_sel = list(set_sub_sel)
    return subj_sel


def group_prof_subj_selection(name, sub):
    prof = professor()
    last_name = name
    subj_prof = sub
    subj = []
    for k in prof.keys():
        if last_name in prof[k] and subj_prof in prof[k]:
            line = list(prof[k])
            subj.append(line[3])
        set_subj = set(subj)
        subj = list(set_subj)
    return subj


def work_with_group(name):
    last_name = name
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
    work_doc_ch = choice_gr_list_hw()
    if work_doc_ch == '1':
        work_doc_list = choice_gr()
        if work_doc_list == '1':
            list_subject_gr = list_print(subject, group_func, work_doc_ch)
            for keys, values in list_subject_gr.items():
                print(keys, ''.join(values))
        else:
            print('2')
    else:
        work_doc_hw = choice_gr()
        if work_doc_hw == '1':
            list_hw_gr = list_print(subject, group_func, work_doc_ch)
            for keys, values in list_hw_gr.items():
                print(keys, ''.join(values))
        else:
            print('2')










    """list_subject_gr = import_list(function, group_func)
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




