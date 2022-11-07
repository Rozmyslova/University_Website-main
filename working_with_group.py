from professors import professor


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




