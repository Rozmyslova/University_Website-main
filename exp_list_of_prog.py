from list_of_program import list_of_program


def export_list_of_program():
    l_of_pr = list_of_program()
    with open('list_of_program.txt', 'w', encoding="utf-8") as l_pr:
        l_pr.write("Перечень программ нашего университета\n")
        for key, val in l_of_pr.items():
            l_pr.write('{}:{}\n'.format(key, val))
