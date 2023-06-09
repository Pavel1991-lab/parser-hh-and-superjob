from hh_class import HH

def func():
    print(
        f'Здравствуйте! В данной программе вы можете по ключевому слову найти вакансии. Также вам нужно будет указать город \nв котором будем искать вакансии.\nВся информация о вакансиях будет записана в формате json.')
    print('1 - Приступить искать вкакнсии')
    print('0 - Выход')
    while True:
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


