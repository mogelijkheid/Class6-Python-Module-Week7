import json
class Product:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
    def tojson(self):
        self.d={'name':self.name, {"name": self.name, "brand": {"brand_name": self.brand.name, "brand_year": self.brand.year}, "price": self.price}   
        with open (self.name+".json", "w") as json_file:
            json.dump(self.d, json_file, indent=4)
class Brand:
    def __init__(self, name, year):
        self.name = name
        self.year = year
brand1=Brand('Toshiba', 200)
Product1=Product('computer',brand1,2006)

Product1.price