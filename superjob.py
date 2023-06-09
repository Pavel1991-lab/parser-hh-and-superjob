import json

import requests

from hh_class import Engine


class Superjob(Engine):
    def __init__(self, keyword, city_id):
        self.__keyword = keyword
        self.__city_id = city_id
        self.__count = 100

    def get_request(self):
        headers = {
            'X-Api-App-Id': 'v3.r.120090948.572bca28fd872bb2739e14bb6605d85591462276.d2b41b0e28e946135e7cb1756bb9b86494dedd23',
            'Content-Type': 'application/json'}
        params = {
            "page": 1,
            "count": self.__count,
            "keyword": self.__keyword
        }
        responce = []
        for city_id in self.__city_id:
            params.update({"town": city_id})
            for page in range(1, 11):
                params.update({"page": page})
                data = requests.get("https://api.superjob.ru/2.0/vacancies/", headers=headers, params=params)
                responce += data.json()['objects']
        return responce

    def area(self):
        pass

    def vacancy(self):
        result = []
        for index, job in enumerate(self.get_request()):
            jobs = []
            jobs.append(index + 1)  # добавляем номер вакансии
            jobs.append(job['profession'])
            jobs.append(job['work'])
            jobs.append(job['payment_from'])
            jobs.append(job['payment_to'])
            jobs.append(job['currency'])
            jobs.append(job['experience'])
            result.append(jobs)
        return result

    def json(self):
        with open('superjob_vacancies.json', 'w', encoding='utf-8') as f:
            # записываем данные в JSON-формате с параметром ensure_ascii=False
            json.dump(self.vacancy(), f, indent=4, ensure_ascii=False)

    def salary(self):
        salary = []
        for i in self.vacancy():
            money = []
            money.append(i[0])
            money.append(i[1])
            money.append(i[3])
            money.append(i[4])
            money.append(i[5])
            salary.append(money)
        return salary

    def top_vacancies(self):
        rub = []
        for i in self.salary():
            if i[4] == 'rub':
                rub.append(i)
        sorted_jobs = sorted(rub, key=lambda x: x[3], reverse=True)
        top_three = sorted(sorted_jobs[:3], reverse=True)
        return top_three




    def top3_json(self):
        with open('top3_vacancies.json', 'w', encoding='utf-8') as f:
            # записываем данные в JSON-формате с параметром ensure_ascii=False
            json.dump(self.top_vacancies(), f, indent=4, ensure_ascii=False)

a = Superjob('python', 'Казань')

print(a.top3_json())