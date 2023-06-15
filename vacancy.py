import json

"Класс который сохраняет вакансии в json"
class Vacancy:

    def __init__(self, vacancy:list, top_vacancy:list):
        self.__vacancy = vacancy
        self.__top_vacancy = top_vacancy


    def top3_json_vac(self):
        with open('top3_vacancies.json', 'w', encoding='utf-8') as f:
            # записываем данные в JSON-формате с параметром ensure_ascii=False
            json.dump(self.__top_vacancy, f, indent=4, ensure_ascii=False)


    def json_vac(self):
        with open('vacancies.json', 'w', encoding='utf-8') as f:
            # записываем данные в JSON-формате с параметром ensure_ascii=False
            json.dump(self.__vacancy, f, indent=4, ensure_ascii=False)







