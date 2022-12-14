import json

#функция загрузки файла
def load_json() -> list[dict]:
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


#форматирование списка кандидатов
def format_candidates(candidates: list[dict]) -> str:
    result = '<pre>'

    for candidate in candidates:
        result += f"""
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}\n
        """
    result += '</pre>'
    return result


def get_all_candidates() -> list[dict]:
    return load_json()


#поиск кандидата по id
def get_candidate_by_id(uid: int) -> dict | None:
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return None


#поиск кандидата по навыку
def get_candidate_by_skill(skill: str) -> list[dict]:
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result