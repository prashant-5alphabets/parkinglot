class Slot:
    def __init__(self, number):
        self.number = number
        self.is_empty = True
        self.car_color = None
        self.car_registration_number = None

    def make_it_empty(self):
        self.is_empty = True
        self.car_color = None
        self.car_registration_number = None

    def put_car(self, color, registration_number):
        self.car_registration_number = registration_number
        self.car_color = color
        self.is_empty = False

    def get_car_parked(self):
        return self.car_registration_number, self.car_color

    def is_empty(self):
        return self.is_empty

    def get_slot_number(self):
        return self.number