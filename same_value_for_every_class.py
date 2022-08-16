import pdb
pdb.set_trace()

class Vehicle:
    
    colour = "Yellow"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Bus", 180, 12)
print(School_bus.colour, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Range Rover", 300, 18)
print(car.colour, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)