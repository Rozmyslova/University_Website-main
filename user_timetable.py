from timetable import timetable
from students import student


def timetable_for_professor(name):
    last_name = name
    ttable = timetable()
    new_ttable = {}
    for k in ttable.keys():
        if last_name in ttable[k]:
            line = list(ttable[k])
            del line[2]
            print(k, " ".join(line))
            new_ttable.update({k: " ".join(line)})
    return new_ttable


def timetable_for_student(group):
    ttable = timetable()
    new_ttable = {}
    for k in ttable.keys():
        if group in ttable[k]:
            line = list(ttable[k])
            del line[1]
            print(k, " ".join(line))
            new_ttable.update({k: " ".join(line)})
    return new_ttable
