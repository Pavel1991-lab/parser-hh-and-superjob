from dotenv import load_dotenv
import os
import requests
from hh_class import Engine
load_dotenv()
API_KEY = os.getenv('MY_API_KEY')

class Superjob(Engine):
    def __init__(self, keyword, city_id):
        self.__keyword = keyword
        self.__city_id = city_id
        self.__count = 100

    def get_request(self):
        headers = {
            'X-Api-App-Id': API_KEY,
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
            jobs.append(job['town'])

            result.append(jobs)
        return result

    def salary(self):
        salary = []
        for i in self.vacancy():
            money = []
            money.append(i[0])
            money.append(i[1])
            money.append(i[3])
            money.append(i[4])
            money.append(i[5])
            money.append(i[6])
            money.append(i[7])
            salary.append(money)
        return salary

    def top_vacancies(self):
        rub = []
        usd = []
        for i in self.salary():
            if i[4] == 'rub':
                rub.append(i)
        for i in self.salary():
            if i[4] == 'usd':
                usd.append(i)
        sorted_jobs_rub = sorted(rub, key=lambda x: x[3], reverse=True)
        sorted_jobs_usd = sorted(usd, key=lambda x: x[3], reverse=True)
        top_three_rub = sorted(sorted_jobs_rub[:3], reverse=True)
        top_three_usd = sorted(sorted_jobs_usd[:3], reverse=True)
        return top_three_rub, top_three_usd




