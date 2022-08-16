import json
import pdb
pdb.set_trace()


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


def vehicleDecoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])


vehicleObj = json.loads('{ "name": "Toyota Fourtuner", "engine": "3.5L", "price": 3200000 }',
                        object_hook=vehicleDecoder)

print("Type of decoded object from JSON Data")
print(type(vehicleObj))
print("Vehicle Details")
print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)
