
from abc import ABC, abstractmethod
import requests

class Engine(ABC):
    'Получаем запрос по Апи из hh.ru или из superjob. Так же благодаря этому методу ищем вкансии по ключевому слову и по городу'
    @abstractmethod
    def get_request(self, keyword, count):
        pass

    'Для hh.ru выставляем регион Россию, дял superjob оставляем заглушку '
    @abstractmethod
    def area(self):
        pass

    'Из отфильтрованого запроса по городу и ключевому слову, с помощью этого метода'
    'достаем по ключу нужные значения вакансий'
    @abstractmethod
    def vacancy(self):
        pass

    'Отдельно находим зарпалыт чтобы могли найти самые высокие'
    @abstractmethod
    def salary(self):
        pass

    'Достаем три самых выгодных вакансий'
    @abstractmethod
    def top_vacancies(self):
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





