class ComercialAnouncement:
    def __init__(self, name, dni, section,title, body):
        self.name = name 
        self.dni = dni
        self.section  = section
        self.title = title
        self.body = body

class ClasifiedAnouncement:
    def __init__(self,price, date, days, article_type):
        self.price = price
        self.date = date
        self.days = days
        self.article_type = article_type

class ClasifiedAnouncementVehicle(ClasifiedAnouncement):
    def __init__(self, price, date, days,brand, model, year,color,km):
        super().__init__(price, date, days, "Vehicle")
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.km = km

class ClasifiedAnouncementHouse(ClasifiedAnouncement):
    def __init__(self, price, date, days,m2,rooms, bathrooms, parking_lot, policy):
        super().__init__(price, date, days, "House")
        self.rooms = rooms
        self.m2 = m2
        self.bathrooms = bathrooms
        self.parking_lot = parking_lot
        self.policy = policy