from src.car import Car


class Slot:

    def __init__(self, number):
        self.number = number
        self.empty = True
        self.car = None

    def make_it_empty(self):
        self.empty = True
        del self.car
        self.car = None
        print "Slot number " + str(self.number) + " is free"

    def put_car(self, registration_number, color):
        self.car = Car(registration_number, color)
        self.empty = False
        print "Allocated slot number: " + str(self.get_slot_number())

    def get_car_parked(self):
        if self.empty:
            return None, None
        return self.car.get_registration_number(), self.car.get_color()

    def is_empty(self):
        return self.empty

    def get_slot_number(self):
        return self.number
