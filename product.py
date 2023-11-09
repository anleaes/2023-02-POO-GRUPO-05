class Category: #categoria para agrupar o tipo de produto
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description



class Product: #Informações do produto
    def __init__(self, name, description, date_fabrication, is_active, category):
        self.name = name
        self.description = description
        self.date_fabrication = date_fabrication
        self.is_active = is_active
        self.category = category