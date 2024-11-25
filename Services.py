from Requests import ProductionRequest, PreparationRequest

class Service:
    def __init__(self, service_id, service_name):
        self.id = service_id
        self.id = service_name

class ProductionService(Service):
    def __init__(self, service_id, service_name):
        super().__init__(service_id, service_name)

    def create_request(self, start_day, order_id, request_id, service_access, forest_production_type, forest_production_num, need_areas, additional_information='-'):
        request = ProductionRequest(start_day, order_id, request_id, service_access, forest_production_type, forest_production_num, need_areas, additional_information)


class TechnologyService(Service):
    def __init__(self, service_id, service_name):
        super().__init__(service_id, service_name)

    def create_request(self, start_day, order_id, request_id, service_access, area_id, need_do):
        request = PreparationRequest(start_day, order_id, request_id, service_access, area_id, need_do)