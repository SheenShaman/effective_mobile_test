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


def add_new_contact(phonebook):
    """ Добавление нового контакта в справочник """
    contact = {'last_name': input('Введите фамилию: '), 'first_name': input('Введите имя: '),
               'middle_name': input('Введите отчество: '), 'organization_name': input('Введите название организации: '),
               'working_phone': input('Введите рабочий телефон: '), 'personal_phone': input('Введите личный телефон: ')}
    phonebook.append(contact)
    save_phonebook(phonebook)
    print("Контакт добавлен")


def edit_contact(phonebook):
    """ Изменение существующего контакта """
    last_name = input("Введите Фамилию контакта, который хотите изменить: ")
    for contact in phonebook:
        if contact['last_name'] == last_name:
            contact['first_name'] = input("Введите новое имя: ")
            contact['middle_name'] = input("Введите новое отчество: ")
            contact['organization_name'] = input("Введите новое название организации: ")
            contact['working_phone'] = input("Введите новый рабочий телефон: ")
            contact['personal_phone'] = input("Введите новый личный телефон: ")
            save_phonebook(phonebook)
            print("Контакт изменен")
            return
    else:
        print("Контакт не найден")


def search_contacts(phonebook):
    """ Поиск контактов по заданным характеристикам """
    query = input("Введить запрос по поиску: ").lower()
    found_contacts = []
    for contact in phonebook:
        if (query in contact['last_name'].lower() or query in contact['first_name'].lower()
                or query in contact['middle_name'].lower() or query in contact['organization_name'].lower()
                or query in contact['working_phone'] or query in contact['personal_phone']):
            found_contacts.append(contact)
    if found_contacts:
        print("Найденные контакты: ")
        for contact in found_contacts:
            print(contact)
    else:
        print("Контакты не найдены")


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
            add_new_contact(phonebook)
        elif choice == '3':
            edit_contact(phonebook)
        elif choice == '4':
            search_contacts(phonebook)
        elif choice == '5':
            print("Завершение программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз")


if __name__ == '__main__':
    main()
