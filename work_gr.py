from for_prof import list_vmat_104_gr
from for_prof import list_inyaz_104_gr
from for_prof import list_vved_104_gr
from for_prof import list_vmat_203_gr
from for_prof import list_inyaz_203_gr
from for_prof import list_terver_203_gr
from for_prof import hw_vmat_104_gr
from for_prof import hw_inyaz_104_gr
from for_prof import hw_vved_104_gr
from for_prof import hw_vmat_203_gr
from for_prof import hw_inyaz_203_gr
from for_prof import hw_terver_203_gr


def list_print(sub, gr, choice):
    subj = sub
    group = gr
    ch_l_hw = choice
    if subj == 'Высшая математика' and group == '104 группа':
        if ch_l_hw == '1':
            list_subject_gr = list_vmat_104_gr()
        else:
            list_subject_gr = hw_vmat_104_gr()
    elif subj == 'Иностранный язык' and group == '104 группа':
        if ch_l_hw == '1':
            list_subject_gr = list_inyaz_104_gr()
        else:
            list_subject_gr = hw_inyaz_104_gr()
    elif subj == 'Введение в специальность' and group == '104 группа':
        if ch_l_hw == '1':
            list_subject_gr = list_vved_104_gr()
        else:
            list_subject_gr = hw_vved_104_gr()
    elif subj == 'Высшая математика' and group == '203 группа':
        if ch_l_hw == '1':
            list_subject_gr = list_vmat_203_gr()
        else:
            list_subject_gr = hw_vmat_203_gr()
    elif subj == 'Иностранный язык' and group == '203 группа':
        if ch_l_hw == '1':
            list_subject_gr = list_inyaz_203_gr()
        else:
            list_subject_gr = hw_inyaz_203_gr()
    else:
        if ch_l_hw == '1':
            list_subject_gr = list_terver_203_gr()
        else:
            list_subject_gr = hw_terver_203_gr()
    return list_subject_gr
