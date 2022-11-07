from list_of_documents import list_of_documents


def export_list_of_doc():
    l_of_d = list_of_documents()
    with open('list_of_documents.txt', 'w', encoding="utf-8") as l_d:
        l_d.write("Даты вступительных испытаний нашего университета\n")
        for key, val in l_of_d.items():
            l_d.write('{}:{}\n'.format(key, val))
