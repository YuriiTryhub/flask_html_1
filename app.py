from flask import Flask
from utils import load_candidates_from_json, get_candidate_by_id, get_candidates_by_skill, url, get_candidates_by_name

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = load_candidates_from_json()
    candidate_info = ' '
    for candidate in candidates:
        candidate_info += f"""<img src='({url})'> \n
                          <pre> \n
                            {candidate['name']}\n
                            {candidate['position']}\n
                            {candidate['skills']}\n
                            \n
                          </pre>"""
    return candidate_info


@app.route('/candidates/<int:x>')
def profile(x):
    id_candidate = get_candidate_by_id(x)
    return id_candidate


@app.route('/skills/<x>')
def by_skill_profile(x):
    candidate_skill = get_candidates_by_skill(x)
    return candidate_skill


app.run()

if __name__ == '__main__':
    pass