# Телефонный справочник

## В проекте реализованы возможности:
1. Постраничного вывода записей из справочника в консоль
2. Добавление новой записи в справочник
3. Возможность редактирования записей в справочнике
4. Поиск записей по заданным характеристикам
5. Заполнение текстового файла рандомной базой контактов

## Запуск проекта
1. Склонировать репозиторий на свой локальный компьютер **git clone https://github.com/SheenShaman/effective_mobile_test**
2. В консоли ввести команду **python main.py**
______________________________________________________________________________________________________________________
#### В файле main.py:
1. функция **load_phonebook** загружает данные из файла phonebook.txt
2. функция **save_phonebook** сохраняет данные в файл phonebook.txt
3. функция **display_contacts** выводит постранично записи из файла phonebook.txt, с выбором страницы
4. функция **add_new_contact** добавляет новый контакт в файл phonebook.txt
5. функция **edit_contact** изменяет существующий контакт в файле phonebook.txt
6. функция **search_contacts** ищет существующие контакты в файле phonebook.txt по заданным характеристикам и выводит их в консоль
7. функция **main** является главным меню, для взаимодействия с пользователем, который, в свою очередь, выбирает пункты меню в зависимости от того, что ему нужно

#### В файле utils.py:
1. функция **random_phone_number** создает рандомный номер телефона
2. функция **create_contact** создает рандомный контакт(запись) и сохраняет его в файл phonebook.txt
3. функция **start** заполняет файл phonebook.txt рандомной базой контактов

В файле **phonebook** хранение данных 