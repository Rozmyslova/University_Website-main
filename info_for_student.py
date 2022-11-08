def list_of_mark_visit(name, group):
    last_name = name
    list_of_sub = {}
    if group == '104 группа':
        with open("list_vmat_104_gr.txt", encoding="utf-8") as file:
            for line in file:
                key, *value = line.split("|")
                list_of_sub[key] = value
        for k in list_of_sub.keys():
            if last_name not in k:
                del list_of_sub[k]
        for keys, values in list_of_sub.items():
            print(keys, ' | '.join(values))

        """with open("list_inyaz_104_gr.txt", encoding="utf-8") as file:
            for line in file:
                list_of_sub.append(line)
        with open("list_vved_104_gr.txt", encoding="utf-8") as file:
            for line in file:
                list_of_sub.append(line)
    else:
        with open("list_vmat_203_gr.txt", encoding="utf-8") as file:
            for line in file:
                list_of_sub.append(line)
        with open("list_inyaz_203_gr.txt", encoding="utf-8") as file:
            for line in file:
                list_of_sub.append(line)
        with open("list_terver_203_gr.txt", encoding="utf-8") as file:
            for line in file:
                list_of_sub.append(line)

    list_of_mark = []
    for i in range(len(list_of_sub)):
        if last_name in list_of_sub[i]:
            list_of_mark.append(list_of_sub[i])
    print(list_of_mark)
    for i in range(len(list_of_mark)):
        #list_of_mark[i] = list(list_of_mark[i])
        print(list_of_mark[i].split("|"))"""






    """last_name = name



    ttable = timetable()
    new_ttable = {}
    for k in ttable.keys():
        if group in ttable[k]:
            line = list(ttable[k])
            del line[1]
            print(k, " ".join(line))
            new_ttable.update({k: " ".join(line)})
    return new_ttable"""