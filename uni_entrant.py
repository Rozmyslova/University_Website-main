from user_interface import entrant_choice
from for_entrant import list_of_program
from user_interface import export_data
from export import export_list_of_program
from for_entrant import date_of_ent_exam
from export import export_date_of_exam
from for_entrant import min_score_of_exam
from export import export_min_score
from for_entrant import list_of_documents
from export import export_list_of_doc


def operation_for_entrant():
    entrant_op = True
    while entrant_op:
        operation = entrant_choice()
        if operation == '1':
            print("Перечень программ университета")
            l_of_p = list_of_program()
            for keys, values in l_of_p.items():
                print(keys + ' | ' + values)
            export_list_of_prog = export_data()
            if export_list_of_prog == '1':
                export_list_of_program()
            print('Файл list_of_program.txt экспортирован')
        elif operation == '2':
            print("Даты вступительных испытаний")
            d_of_exam = date_of_ent_exam()
            for keys, values in d_of_exam.items():
                print(keys + ' : ' + values)
            export_date = export_data()
            if export_date == '1':
                export_date_of_exam()
            print('Файл date_of_exam.txt экспортирован')
        elif operation == '3':
            print("Минимальные проходные баллы")
            min_sc = min_score_of_exam()
            for keys, values in min_sc.items():
                print(keys + ' : ' + values)
            export_min_sc = export_data()
            if export_min_sc == '1':
                export_min_score()
            print('Файл min_score.txt экспортирован')
        elif operation == '4':
            print("Список документов необходимых для поступления")
            list_doc = list_of_documents()
            for keys, values in list_doc.items():
                print(keys + '. ' + values)
            export_list_doc = export_data()
            if export_list_doc == '1':
                export_list_of_doc()
            print('Файл list_of_documents.txt экспортирован')
        else:
            break
