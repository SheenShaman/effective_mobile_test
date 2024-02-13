import random
from main import load_phonebook, save_phonebook

# Списки данных из которых будут генерироваться контакты
list_last_name = ['Ivanov', 'Petrov', 'Sidorov', 'Smirnov', 'Sokolov', 'Popov', 'Lebedev', 'Morozov', 'Volkov',
                  'Pavlov']
list_first_name = ['Aleksandr', 'Dmitriy', 'Michail', 'Maksim', 'Mark', 'Artem', 'Ivan', 'Petr', 'Matvei', 'Pavel']
list_middle_name = ['Alekseevich', 'Ivanovich', 'Dmitrievich', 'Michailovich', 'Aleksandrovich', 'Maksimovich',
                    'Petrovich', 'Matveivich', 'Pavlovich', 'Artemovich']
list_organization_name = ['Sber', 'VK', 'Tinkoff', 'Alfabank', 'Lukoil', 'Gazpromneft', 'Yandex', 'Lego', 'Amazon',
                          'Apple']


def random_phone_number():
    """ Создание рандомного номера телефона """
    phone = random.randint(79000000000, 80000000000)
    return str(phone)


def create_contact(phonebook):
    """ Создание рандомного контакта  """
    contact = {
        'last_name': random.choice(list_last_name),
        'first_name': random.choice(list_first_name),
        'middle_name': random.choice(list_middle_name),
        'organization_name': random.choice(list_organization_name),
        'working_phone': random_phone_number(),
        'personal_phone': random_phone_number()
    }
    phonebook.append(contact)
    save_phonebook(phonebook)
    return contact


def start():
    """ Заполнение данными файл """
    phonebook = load_phonebook()
    for item in range(100):
        create_contact(phonebook)


start()
