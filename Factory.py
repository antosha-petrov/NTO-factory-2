import sqlite3
import uuid  # Для генерации уникальных идентификаторов

# Подключение к существующей базе данных
connection = sqlite3.connect('factory.db')
cursor = connection.cursor()


# Класс для фабрики
class Factory:
    def __init__(self, factory_name, workshops_list, services_list):
        self.name = factory_name
        self.workshops = workshops_list
        self.services = services_list


# Класс для цехов
class Workshop:
    def __init__(self, workshop_name):
        self.id = str(uuid.uuid4())  # Генерация уникального идентификатора
        self.name = workshop_name
        self.areas = []  # Список участков, принадлежащих цеху

        # Добавление цеха в базу данных
        self.save_to_db()

    def save_to_db(self):
        """Сохранение цеха в базу данных."""
        cursor.execute('INSERT INTO workshops (id, name) VALUES (?, ?)', (self.id, self.name))
        connection.commit()

    def add_area(self, area):
        """Добавление участка в список участков цеха."""
        self.areas.append(area)


# Класс для участков
class Area:
    def __init__(self, area_name, area_description):
        self.id = str(uuid.uuid4())  # Генерация уникального идентификатора
        self.name = area_name
        self.description = area_description
        self.readiness = False

        # Добавление участка в базу данных
        self.save_to_db()

    def save_to_db(self):
        """Сохранение участка в базу данных."""
        cursor.execute('INSERT INTO areas (id, name, description, readiness) VALUES (?, ?, ?, ?)',
                       (self.id, self.name, self.description, int(self.readiness)))
        connection.commit()
