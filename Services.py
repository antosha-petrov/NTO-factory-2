from Requests import ProductionRequest, PreparationRequest


class Service:
    def __init__(self, service_name):
        self.name = service_name


class ProductionService(Service):
    def __init__(self, service_name):
        super().__init__(service_name)

    def create_request(self, start_day, order_id, service_access, forest_production_type, forest_production_num, need_areas, additional_information='-'):
        """Создаёт заявку на производство и автоматически добавляет её в базу данных."""
        print(f"{self.name} создаёт заявку.")

        # Создание заявки
        request = ProductionRequest(
            start_day=start_day,
            order_id=order_id,
            service_access=service_access,
            forest_production_type=forest_production_type,
            forest_production_num=forest_production_num,
            need_areas=need_areas,
            additional_information=additional_information
        )

        # Добавление заявки в базу данных
        request.save_to_db()

        return request


class TechnologyService(Service):
    def __init__(self, service_name):
        super().__init__(service_name)

    def create_request(self, start_day, order_id, service_access, area_id, need_do):
        """Создаёт заявку на подготовку и автоматически добавляет её в базу данных."""
        print(f"{self.name} создаёт заявку.")

        # Создание заявки
        request = PreparationRequest(
            start_day=start_day,
            order_id=order_id,
            service_access=service_access,
            area_id=area_id,
            need_do=need_do
        )

        # Добавление заявки в базу данных
        request.save_to_db()

        return request
