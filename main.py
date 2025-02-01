import random
import time
import datetime


class ParkingGarage:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cars = []
        self.free = capacity
        self.entry_allowed = True

    def print_state(self):
        print(
            f"Capacity: {self.capacity}\nTaken: {len(self.cars)}\nFree: {self.free}\nOpen: {self.entry_allowed}"
        )

    def enter(self, plate):
        if self.entry_allowed == True:
            self.cars.append(Car(plate=plate))
            print(f"Entering: {plate} at {self.cars[-1].entry_time}")
            self.calc_free()
        else:
            print("The garage is full.")

    def exit(self, plate):
        car_to_remove = next((car for car in self.cars if car.plate == plate), None)
        if car_to_remove:
            print(f"Car with plate {plate} leaves the garage.")
            self.cars.remove(car_to_remove)
        else:
            print(f"Car with plate {plate} not found.")
        self.calc_free()

    def calc_free(self):
        self.free = self.capacity - len(self.cars)
        if self.free == 0:
            self.entry_allowed = False


class Car:
    def __init__(self, plate):
        self.plate = plate
        self.parking_time = 0
        self.paid = False
        self.entry_time = datetime.datetime.now()

    def pay(self, time):
        self.parking_time = (time - self.entry_time).total_seconds() / 3600
        self.paid = True
        print(f"Car with plate {self.plate} paid for {self.parking_time:.2f} hours.")


# Code for simulation purposes
swiss_cantons = [
    "AG", "AI", "AR", "BE", "BL", "BS", "FR", "GE", "GL", "GR", "JU", "LU", "NE", "NW", "OW", "SG", "SH", "SO", "SZ", "TG", "TI", "UR", "VD", "VS", "ZG", "ZH"
]

my_parking_garage = ParkingGarage(capacity=140)

operation = ["Enter", "Exit"]
for i in range(0, random.randint(a=1, b=540)):
    time.sleep(1)
    if random.choice(operation) == "Enter":
        my_parking_garage.enter(
            plate=f"{random.choice(swiss_cantons)}{random.randint(a=24, b=999999)}"
        )
    else:
        try:
            car_to_remove = random.choice(my_parking_garage.cars)
            car_to_remove.pay(datetime.datetime.now())
            my_parking_garage.exit(plate=car_to_remove.plate)
        # Handle the case if an exit operation is before any enter operation.
        except IndexError:
            pass

my_parking_garage.print_state()
