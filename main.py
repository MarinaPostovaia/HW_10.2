import picture as picture
from flask import Flask
from utils import load_json, get_all_candidates, format_candidates, get_candidate_by_id, get_candidate_by_skill

# инициализация приложения
app = Flask(__name__)


@app.route('/')
# главная страница
def page_main():
    candidates: list[dict] = get_all_candidates()
    result: str = format_candidates(candidates)
    return result


# поиск кандидата по id
@app.route('/candidate/<int:vid>')
def page_candidate(uid):
    candidate: dict = get_candidate_by_id(uid)
    result = f'<img src="{candidate[picture]}">'
    result += format_candidates([candidate])
    return result

#поиск по навыку
@app.route('/skills/<skill>')
def page_skills(skill):
    skill_lower = skill.lower()
    candidates: list[dict] = get_candidate_by_skill(skill_lower)
    result = format_candidates(candidates)
    return result
app.run()


