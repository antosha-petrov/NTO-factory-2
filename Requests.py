from datetime import date


class Request:
    def __init__(self, start_day, order_id, request_id, service_access):
        self.create_date = date.today()
        self.start_day = start_day
        self.order_id = order_id
        self.request_id = request_id
        self.access = service_access


class ProductionRequest(Request):
    def __init__(self, start_day, order_id, request_id, service_access, forest_production_type, forest_production_num, need_areas,
                 additional_information='-'):
        super().__init__(start_day, order_id, request_id, service_access)
        self.type = forest_production_type
        self.num = forest_production_num
        self.areas = need_areas
        self.additional_information = additional_information


class PreparationRequest(Request):
    def __init__(self, start_day, order_id, request_id, service_access, area_id, need_do):
        super().__init__(start_day, order_id, request_id, service_access)
        self.need_do = need_do
        self.areas_id = area_id
        self.status = 'Создан'