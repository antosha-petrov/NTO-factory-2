import sqlite3

def create_db():
    # Подключение к базе данных (создаётся, если не существует)
    connection = sqlite3.connect('factory.db')
    cursor = connection.cursor()

    # Создание таблицы для общих заявок (Request)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS requests (
        request_id TEXT NOT NULL,                      -- Уникальный ID заявки
        create_date TEXT NOT NULL,                     -- Дата создания
        start_day TEXT NOT NULL,                       -- Дата начала выполнения
        order_id INTEGER NOT NULL,                     -- ID заказа
        service_access TEXT NOT NULL                   -- Доступ службы
    )
    ''')

    # Создание таблицы для заявок на производство (ProductionRequest)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS production_requests (
        request_id TEXT NOT NULL,               -- ID заявки (ссылка на requests)
        forest_production_type TEXT NOT NULL,         -- Тип продукции
        forest_production_num INTEGER NOT NULL,       -- Количество продукции
        need_areas TEXT NOT NULL,                     -- Задействованные участки
        additional_information TEXT,                  -- Дополнительная информация
        FOREIGN KEY (request_id) REFERENCES requests (request_id)
    )
    ''')

    # Создание таблицы для заявок на подготовку/оснастку (PreparationRequest)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS preparation_requests (
        request_id TEXT NOT NULL,               -- ID заявки (ссылка на requests)
        area_id INTEGER NOT NULL,                     -- ID участка
        need_do TEXT NOT NULL,                        -- Что нужно сделать
        status TEXT NOT NULL DEFAULT 'Создан',        -- Статус заявки
        FOREIGN KEY (request_id) REFERENCES requests (request_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS workshops (
        id TEXT PRIMARY KEY,         -- Уникальный идентификатор
        name TEXT NOT NULL           -- Название цеха
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS areas (
        id TEXT PRIMARY KEY,         -- Уникальный идентификатор
        name TEXT NOT NULL,          -- Название участка
        description TEXT,            -- Описание участка
        readiness INTEGER DEFAULT 0, -- Готовность участка (0 или 1)
        workshop_id TEXT,            -- Связь с цехом
        FOREIGN KEY (workshop_id) REFERENCES workshops (id)
    )
    ''')

    # Сохранение изменений и закрытие соединения
    connection.commit()
    connection.close()