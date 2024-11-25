class Factory:
    def __init__(self, workshops_list, services_list, factory_name, factory_access):
        self.name = factory_name
        self.workshops = workshops_list
        self.services = services_list
        self.access = factory_access


class Workshop:
    def __init__(self, workshop_id, workshop_name, areas_list):
        self.id = workshop_id
        self.name = workshop_name
        self.areas = areas_list


class Area:
    def __init__(self, area_id, area_name, area_description, area_access):
        self.id = area_id
        self.name = area_name
        self.description = area_description
        self.access = area_access
        self.readiness = False