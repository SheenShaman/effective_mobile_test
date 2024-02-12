import json

PHONEBOOK = "phonebook.txt"


def load_phonebook():
    """ Загрузка данных из текстового файла """
    try:
        with open(PHONEBOOK, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_phonebook(contact):
    """ Сохранение данных в текстовый файл """
    with open(PHONEBOOK, 'w') as file:
        json.dump(contact, file)
