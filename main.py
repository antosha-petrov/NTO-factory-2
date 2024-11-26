import sqlite3
from Factory import Factory, Workshop, Area
from Services import ProductionService, TechnologyService
import database

database.create_db()

# Создание соединения с базой данных
connection = sqlite3.connect('factory.db')
cursor = connection.cursor()  # Инициализация курсора

# Создание участков
area_lists = [
    [
        Area('Лесопильная линия №1', 'Используется для распиловки тонкомеров, например, реек'),
        Area('Лесопильная линия №2', 'Используется для распиловки среднего леса')
    ],
    [
        Area('Сушильная камера №1', 'Пока-что тут пусто :('),
        Area('Сушильная камера №2', 'Пока-что тут пусто :('),
        Area('Сушильная камера №3', 'Пока-что тут пусто :('),
        Area('Сушильная камера №4', 'Пока-что тут пусто :(')
    ],
    [
        Area('Линия строжки №1', 'Используется для строжки тонкомеров'),
        Area('Линия строжки №2', 'Используется для строжки среднего леса'),
        Area('Линия строжки №3', 'Используется для строжки среднего леса')
    ],
    [
        Area('Дробилка', 'Пока-что тут пусто :('),
        Area('Сушилка', 'Пока-что тут пусто :('),
        Area('Гранулятор №1', 'Пока-что тут пусто :('),
        Area('Гранулятор №2', 'Пока-что тут пусто :(')
    ]
]

# Создание служб
services_list = [
    ProductionService('Служба производства'),
    TechnologyService('Служба технолога')
]

# Создание цехов и добавление участков
workshops_list = [
    Workshop('Лесопильный цех'),
    Workshop('Сушильный комплекс'),
    Workshop('Цех строжки и обработки'),
    Workshop('Пеллетный цех')
]

# Добавление участков в соответствующие цеха
for workshop, areas in zip(workshops_list, area_lists):
    for area in areas:
        workshop.add_area(area)

# Создание предприятия
factory = Factory('Лесопильный завод', workshops_list, services_list)

# Приветствие
print(f'Здравствуйте, добро пожаловать в систему предприятия. Сейчас вы находитесь на странице предприятия "{factory.name}".')
print('Для просмотра информации введите "инфо".')
print('Для дальнейшей авторизации введите ключ сотрудника.')

# Авторизация
key = input()
while key not in ['0', '1']:
    print('Невалидный ключ, пожалуйста, повторите попытку.')
    key = input()

# Логика для сотрудника службы производства
if key == '0':
    print("Вы вошли как сотрудник производства.")

    # Просмотр производственных заявок
    print("Вы можете просматривать только производственные заявки.")
    production_requests = []  # Список производственных заявок
    cursor.execute("SELECT * FROM production_requests")
    for row in cursor.fetchall():
        production_requests.append(row)

    if production_requests:
        print("Список производственных заявок:")
        for i, request in enumerate(production_requests):
            print(f"{i + 1}. {request[1]}")  # Название заявки или ID (в зависимости от структуры)

        # Выбор заявки для подробной информации
        try:
            request_index = int(input("Выберите заявку (введите номер): ")) - 1
            if 0 <= request_index < len(production_requests):
                selected_request = production_requests[request_index]
                print(f"Вы выбрали заявку {selected_request[1]}")
                print(f"Детали заявки: {selected_request}")
            else:
                print("Неверный номер заявки.")
        except ValueError:
            print("Ошибка ввода.")
    else:
        print("Нет доступных производственных заявок.")

    # Добавление новой заявки
    add_request = input("Хотите добавить новую заявку? (да/нет): ").strip().lower()
    if add_request == "да":
        # Запрос данных для новой заявки на производство
        start_day = input("Введите дату начала выполнения: ")
        order_id = int(input("Введите ID заказа: "))
        service_access = "Производство"
        forest_production_type = input("Введите тип продукции: ")
        forest_production_num = int(input("Введите количество продукции: "))
        need_areas = input("Введите цеха (через запятую): ").split(",")
        additional_information = input("Введите дополнительную информацию (по желанию): ")

        # Создание новой заявки
        prod_service = ProductionService("Служба производства")
        prod_service.create_request(
            start_day=start_day,
            order_id=order_id,
            service_access=service_access,
            forest_production_type=forest_production_type,
            forest_production_num=forest_production_num,
            need_areas=need_areas,
            additional_information=additional_information
        )
        print("Заявка успешно добавлена.")

# Логика для сотрудника службы технологов
elif key == '1':
    print("Вы вошли как сотрудник технологической службы.")

    # Просмотр технологических заявок
    print("Вы можете просматривать только технологические заявки.")
    preparation_requests = []  # Список технологических заявок
    cursor.execute("SELECT * FROM preparation_requests")
    for row in cursor.fetchall():
        preparation_requests.append(row)

    if preparation_requests:
        print("Список технологических заявок:")
        for i, request in enumerate(preparation_requests):
            print(f"{i + 1}. {request[1]}")  # Название заявки или ID (в зависимости от структуры)

        # Выбор заявки для подробной информации
        try:
            request_index = int(input("Выберите заявку (введите номер): ")) - 1
            if 0 <= request_index < len(preparation_requests):
                selected_request = preparation_requests[request_index]
                print(f"Вы выбрали заявку {selected_request[1]}")
                print(f"Детали заявки: {selected_request}")
            else:
                print("Неверный номер заявки.")
        except ValueError:
            print("Ошибка ввода.")
    else:
        print("Нет доступных технологических заявок.")

    # Добавление новой заявки
    add_request = input("Хотите добавить новую заявку? (да/нет): ").strip().lower()
    if add_request == "да":
        # Запрос данных для новой заявки на подготовку
        start_day = input("Введите дату начала выполнения: ")
        order_id = int(input("Введите ID заказа: "))
        service_access = "Технология"
        area_id = input("Введите ID участка: ")
        need_do = input("Что нужно сделать на участке? ")

        # Создание новой заявки
        tech_service = TechnologyService("Служба технолога")
        tech_service.create_request(
            start_day=start_day,
            order_id=order_id,
            service_access=service_access,
            area_id=area_id,
            need_do=need_do
        )
        print("Заявка успешно добавлена.")
