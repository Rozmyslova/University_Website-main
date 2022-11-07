from min_score import min_score_of_exam


def export_min_score():
    min_sc = min_score_of_exam()
    with open('min_score.txt', 'w', encoding="utf-8") as m_sc:
        m_sc.write("Минимальные проходные баллы\n")
        for key, val in min_sc.items():
            m_sc.write('{}:{}\n'.format(key, val))
