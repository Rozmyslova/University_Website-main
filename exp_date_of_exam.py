from date_of_ent_exam import date_of_ent_exam


def export_date_of_exam():
    d_of_ex = date_of_ent_exam()
    with open('date_of_exam.txt', 'w', encoding="utf-8") as d_ex:
        d_ex.write("Даты вступительных испытаний нашего университета\n")
        for key, val in d_of_ex.items():
            d_ex.write('{}:{}\n'.format(key, val))
