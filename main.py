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


def display_contacts(contacts, page, page_size=5):
    """ Вывод контактов постранично с выбором страницы """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    for index, contact in enumerate(contacts[start_index:end_index], start=start_index + 1):
        print(contact)


def main():
    # Загрузка данных из текстового файла
    phonebook = load_phonebook()

    while True:
        print("\nМеню\n"
              "1. Вывести контакты\n"
              "2. Добавить новый контакт в справочник\n"
              "3. Отредактировать контакт\n"
              "4. Поиск контактов\n"
              "5. Выход\n")
        choice = input("Введите пункт действия: ")
        if choice == '1':
            page = int(input("Введите номер страницы справочника: "))
            display_contacts(phonebook, page)
        elif choice == '2':
            break
        elif choice == '3':
            break
        elif choice == '4':
            break
        elif choice == '5':
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз")


if __name__ == '__main__':
    main()
