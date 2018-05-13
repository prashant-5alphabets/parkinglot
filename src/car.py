class Car:
    def __init__(self, registration_number, color):
        self.registration_number = registration_number
        self.color = color
        self.slot = -1

    def assign_slot(self, slot):
        self.slot = slot
        return

    def get_slot(self):
        return self.slot

    def get_color(self):
        return self.color

    def get_registration_number(self):
        return self.registration_number