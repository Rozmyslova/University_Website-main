from professors import professor
from correct_enter import correct_last_name
from timetable import timetable
from user_interface import professor_choice
from prof_timetable import timetable_for_professor
from user_interface import export_data
from exp_prof_timetable import export_prof_timetable


def operation_for_professor():
    last_name = correct_last_name()
    professor_op = True
    while professor_op:
        operation = professor_choice()
        if operation == '1':
            print(f"Расписание профессора: {last_name}")
            timetable_for_professor(last_name)
            export_prof_ttable = export_data()
            if export_prof_ttable == '1':
                export_prof_timetable(last_name)





            """l_of_p = list_of_program()
            for keys, values in l_of_p.items():
                print(keys + ' | ' + values)
            export_list_of_prog = export_data()
            if export_list_of_prog == '1':
                export_list_of_program()
        elif operation == '2':
            print("Даты вступительных испытаний")
            d_of_exam = date_of_ent_exam()
            for keys, values in d_of_exam.items():
                print(keys + ' : ' + values)
            export_date = export_data()
            if export_date == '1':
                export_date_of_exam()
        elif operation == '3':
            print("Минимальные проходные баллы")
            min_sc = min_score_of_exam()
            for keys, values in min_sc.items():
                print(keys + ' : ' + values)
            export_min_sc = export_data()
            if export_min_sc == '1':
                export_min_score()
        elif operation == '4':
            print("Список документов необходимых для поступления")
            list_doc = list_of_documents()
            for keys, values in list_doc.items():
                print(keys + '. ' + values)
            export_list_doc = export_data()
            if export_list_doc == '1':
                export_list_of_doc()"""
        else:
            break
