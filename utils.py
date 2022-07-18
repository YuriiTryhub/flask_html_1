import json

url = "http://mypictures.me/123"


def load_candidates():
    """которая загрузит данные из файла"""
    with open('candidates.json', mode='r', encoding='utf-8') as f:
        candidates = json.load(f)
    return candidates


def get_all(candidates):
    """которая покажет всех кандидатов"""
    for i in candidates:
        candidates_list = i['name']
        return candidates_list


def get_by_pk(pk):
    """которая вернет кандидата по pk"""
    candidates = load_candidates()
    for j in candidates:
        if pk == j['pk']:
            candidate_by_pk = f"""<img src='({url})'> \n
                                <pre> \n
                                    {j['name']}\n
                                    {j['position']}\n
                                    {j['skills']}\n
                                    \n
                                </pre>"""
            return candidate_by_pk


def get_by_skill(skill_name):
    """которая вернет кандидатов по навыку"""
    candidates = load_candidates()
    for k in candidates:
        if skill_name in k['skills']:
            candidate_by_skill = f"""<img src='({url})'> \n
                                <pre> \n
                                    {k['name']}\n
                                    {k['position']}\n
                                    {k['skills']}\n
                                    \n
                                </pre>"""
            return candidate_by_skill