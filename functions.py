from hh_class import HH
from superjob import Superjob


def func():
    print(
        f'Здравствуйте! В данной программе вы можете по ключевому слову найти вакансии. Вакансии можно искаить на hh.ru или на superjob. Также вам нужно будет указать город \nв котором будем искать вакансии.\nВся информация о вакансиях будет записана в формате json.')
    print('1 - Приступить искать вкакнсии на hh.ru')
    print('2 - Приступить искать вкакнсии на superjob')
    print('0 - Выход')
    while True:
        comand_1 = input('Ищем на hh.ru или superjob?')
        if comand_1 == '1':
            print('1 - Приступить искать вкакнсии')
            print('0 - Выход')
            comand = input('Вводим слово и города?')
            if comand == '0':
                print('До свидания!')
                break
            elif comand == '1':
                word = input('Введите ключевое слово')
                towns = input('Введите города через запятую: ').split(',')
                towns = [town.strip() for town in towns]
                towns_tuple = tuple(towns)
                hh = HH(word, (towns_tuple))
                hh.json()
                hh.top3_json()
                print('Данные сохранены в формате json. Так же сохранены топ 3 самых \nвыгодных вакансий в доларах и в рублях До свидания!')
                break
            else:
                print(f'Такой команды нет')

        elif comand_1 == '2':
            print('1 - Приступить искать вкакнсии')
            print('0 - Выход')
            comand = input('Вводим слово и города?')
            if comand == '0':
                print('До свидания!')
                break
            elif comand == '1':
                word = input('Введите ключевое слово')
                towns = input('Введите города через запятую: ').split(',')
                towns = [town.strip() for town in towns]
                towns_tuple = tuple(towns)
                sj = Superjob(word, (towns_tuple))
                sj.json()
                sj.top3_json()
                print('Данные сохранены в формате json. Так же сохранены топ 3 самых \nвыгодных вакансий в доларах и в рублях До свидания!')
                break
            else:
                print(f'Такой команды нет')