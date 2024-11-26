import sqlite3
import uuid  # Для генерации уникальных идентификаторов
from datetime import date

# Подключение к существующей базе данных
connection = sqlite3.connect('factory.db')
cursor = connection.cursor()


class Request:
    def __init__(self, start_day, order_id, service_access):
        self.create_date = date.today()  # Дата создания
        self.start_day = start_day      # Дата начала
        self.order_id = order_id        # ID заказа
        self.request_id = str(uuid.uuid4())  # Уникальный идентификатор заявки
        self.access = service_access    # Доступ службы

    def save_to_db(self):
        # Преобразуем create_date и start_day в строки, если это объекты date
        create_date = self.create_date.strftime('%Y-%m-%d') if isinstance(self.create_date, date) else self.create_date

        """Сохраняет общие данные заявки в базу данных."""
        cursor.execute(
            'INSERT INTO requests (request_id, create_date, start_day, order_id, service_access) VALUES (?, ?, ?, ?, ?)',
            (self.request_id, create_date, self.start_day, self.order_id, self.access)
        )
        connection.commit()


class ProductionRequest(Request):
    def __init__(self, start_day, order_id, service_access, forest_production_type, forest_production_num, need_areas, additional_information='-'):
        super().__init__(start_day, order_id, service_access)
        self.type = forest_production_type               # Тип продукции
        self.num = forest_production_num                 # Количество продукции
        self.areas = ', '.join(need_areas)              # Список участков в строку
        self.additional_information = additional_information  # Дополнительная информация

    def save_to_db(self):
        """Сохраняет данные заявки на производство в базу данных."""
        super().save_to_db()  # Сохраняем общие данные заявки
        cursor.execute(
            'INSERT INTO production_requests (request_id, forest_production_type, forest_production_num, need_areas, additional_information) VALUES (?, ?, ?, ?, ?)',
            (self.request_id, self.type, self.num, self.areas, self.additional_information)
        )
        connection.commit()


class PreparationRequest(Request):
    def __init__(self, start_day, order_id, service_access, area_id, need_do):
        super().__init__(start_day, order_id, service_access)
        self.area_id = area_id          # ID участка
        self.need_do = need_do          # Что нужно сделать
        self.status = 'Создан'          # Статус заявки

    def save_to_db(self):
        """Сохраняет данные заявки на подготовку в базу данных."""
        super().save_to_db()  # Сохраняем общие данные заявки
        cursor.execute(
            'INSERT INTO preparation_requests (request_id, area_id, need_do, status) VALUES (?, ?, ?, ?)',
            (self.request_id, self.area_id, self.need_do, self.status)
        )
        connection.commit()
