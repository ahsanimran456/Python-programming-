class Car:
    def __init__(self,make ,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def Car_info(self):
            return f"make:{self.make} this is year:{self.year} color:{self.color} model:{self.model}"
    

# Example usage
my_car = Car("Toyota", "Corolla", 2020, "Blue")
print(my_car.Car_info())