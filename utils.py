import json

url = "http://mypictures.me/123"


def load_candidates_from_json():
    """которая загрузит данные из файла"""
    with open('candidates.json', mode='r', encoding='utf-8') as f:
        candidates = json.load(f)
    return candidates


def get_all(candidates):
    """которая покажет всех кандидатов"""
    for i in candidates:
        candidates_list = i['name']
        return candidates_list


def get_candidate_by_id(candidate_id):
    """которая вернет кандидата по pk"""
    candidates = load_candidates_from_json()
    for j in candidates:
        if candidate_id == j['id']:
            candidate_by_id = f"""<img src='({url})'> \n
                                <pre> \n
                                    {j['name']}\n
                                    {j['position']}\n
                                    {j['skills']}\n
                                    \n
                                </pre>"""
            return candidate_by_id


def get_candidates_by_name(candidate_name):
    """которая возвращает кандидатов по имени"""
    candidates = load_candidates_from_json()
    for g in candidates:
        if candidate_name == g['name']:
            candidate_by_name = f"""<img src='({url})'> \n
                                <pre> \n
                                    {g['name']}\n
                                    {g['position']}\n
                                    {g['skills']}\n
                                    \n
                                </pre>"""
            return candidate_by_name


def get_candidates_by_skill(skill_name):
    """которая вернет кандидатов по навыку"""
    candidates = load_candidates_from_json()
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
