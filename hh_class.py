import json
from abc import ABC, abstractmethod
import requests

class Engine(ABC):
    @abstractmethod
    def get_request(self, keyword, count):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def vacancy(self):
        pass

    @abstractmethod
    def json(self):
        pass

    @abstractmethod
    def salary(self):
        pass

    @abstractmethod
    def top_vacancies(self):
        pass

    @abstractmethod
    def top3_json(self):
        pass



class HH(Engine):
    def __init__(self, keyword, cities):
        self.__keyword = keyword
        self.__count = 500
        self.__cities =  cities


    def get_request(self):
        pages = int(self.__count / 100)
        params = {
            "page": 0,
            "per_page": 100
        }
        responce = []
        for page in range(pages):
            params.update({"page": page})
            data = requests.get(f"https://api.hh.ru/vacancies?text={self.__keyword}", params=params)
            responce += data.json()['items']
        return responce

    def area(self):
        job = []
        if isinstance(self.__cities, str):
            cities = [self.__cities]
        else:
            cities = self.__cities
        for area in self.get_request():
            if any(city in area['area']['name'] for city in cities):
                job.append(area)
        return job

    def vacancy(self):
        result = []
        for index, job in enumerate(self.area()):
            jobs = []
            jobs.append(index + 1)  # добавляем номер вакансии
            jobs.append(job['area']['name'])
            jobs.append(job['name'])
            jobs.append(job['snippet']['requirement'])
            jobs.append(job['salary'])
            jobs.append(job['address'])
            result.append(jobs)
        return result

    def json(self):
        with open('vacancies.json', 'w', encoding='utf-8') as f:
            # записываем данные в JSON-формате с параметром ensure_ascii=False
            json.dump(self.vacancy(), f, indent=4, ensure_ascii=False)

    def salary(self):
        salary = []
        for i in self.area():
            salary.append(i['salary'])

        return salary

    def top_vacancies(self):
        rub_vacancies = []
        usd_vacancies = []
        for i, vacancy in enumerate(self.area()):
            if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
                rub_vacancies.append((i + 1, vacancy))
            elif vacancy['salary'] and vacancy['salary']['currency'] == 'USD':
                usd_vacancies.append((i + 1, vacancy))
        rub_vacancies = sorted(rub_vacancies, key=lambda x: x[1]['salary']['to'] or x[1]['salary']['from'],
                               reverse=True)[:3]
        usd_vacancies = sorted(usd_vacancies, key=lambda x: x[1]['salary']['to'] or x[1]['salary']['from'],
                               reverse=True)[:3]
        top_vacancies_dict = {'RUR': [], 'USD': []}
        for i, vacancy in enumerate(rub_vacancies):
            top_vacancies_dict['RUR'].append({
                'name': vacancy[1]['name'],
                'position': vacancy[0],
                'salary_from': vacancy[1]['salary']['from'],
                'salary_to': vacancy[1]['salary']['to']
            })
        for i, vacancy in enumerate(usd_vacancies):
            top_vacancies_dict['USD'].append({
                'name': vacancy[1]['name'],
                'position': vacancy[0],
                'salary_from': vacancy[1]['salary']['from'],
                'salary_to': vacancy[1]['salary']['to']
            })
        return top_vacancies_dict
    def top3_json(self):
        with open('top3_vacancies.json', 'w', encoding='utf-8') as f:
        # записываем данные в JSON-формате с параметром ensure_ascii=False
            json.dump(self.top_vacancies(), f, indent=4, ensure_ascii=False)





