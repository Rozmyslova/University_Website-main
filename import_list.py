def import_list(sub, gr):
    subj = sub
    group = gr
    list_sub_gr = {}
    if subj == 'Высшая математика' and group == '104 группа':
        with open("list_vmat_104_gr.txt", encoding="utf-8") as file:
            for line in file:
                key, *value = line.split("|")
                list_sub_gr[key] = value
    elif subj == 'Иностранный язык' and group == '104 группа':
        with open("list_inyaz_104_gr.txt", encoding="utf-8") as file:
            for line in file:
                key, *value = line.split("|")
                list_sub_gr[key] = value
    elif subj == 'Введение в специальность' and group == '104 группа':
        with open("list_vved_104_gr.txt", encoding="utf-8") as file:
            for line in file:
                key, *value = line.split("|")
                list_sub_gr[key] = value
    elif subj == 'Высшая математика' and group == '203 группа':
        with open("list_vmat_203_gr.txt", encoding="utf-8") as file:
            for line in file:
                key, *value = line.split("|")
                list_sub_gr[key] = value
    elif subj == 'Иностранный язык' and group == '203 группа':
        with open("list_inyaz_203_gr.txt", encoding="utf-8") as file:
            for line in file:
                key, *value = line.split("|")
                list_sub_gr[key] = value
    else:
        with open("list_terver_203_gr.txt", encoding="utf-8") as file:
            for line in file:
                key, *value = line.split("|")
                list_sub_gr[key] = value
    return list_sub_gr
