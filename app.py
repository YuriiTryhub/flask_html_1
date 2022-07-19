from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidates_by_skill, get_candidate_by_id

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidates/<int:x>/')
def profile(x):
    candidates = get_candidate_by_id(x)
    return render_template('card.html', candidates=candidates)


@app.route('/skills/<x>')
def by_skill_profile(x):
    candidate_skill = get_candidates_by_skill(x)
    return candidate_skill


app.run()

if __name__ == '__main__':
    pass