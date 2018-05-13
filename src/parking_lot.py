from src.slot import Slot


class ParkingLot:

    def __init__(self):
        self.slots = []

    def get_slots(self):
        return self.slots

    def create_par_king_lot(self, slots):
        self.slots = []
        for i in range(slots):
            self.slots.append(Slot(i + 1))
        print "Created a parking lot with " + str(slots) + " slots"

    #this function will be used to park a car
    def park_car(self, registration_number, color):
        for slot in self.slots:
            if slot.is_empty():
                slot.put_car(registration_number, color)
                return
        print "Sorry, parking lot is full"

    # this function will be release a slot
    def empty_slot(self, slot_number):
        self.slots[slot_number - 1].make_it_empty()

    # this function will return `Registration numbers of all cars of a particular colour`
    def get_reg_of_cars_of_particular_colors(self, color):
        reg_nums = []
        for slot in self.slots:
            reg_num, _color = slot.get_car_parked()
            if _color == color:
                reg_nums.append(reg_num)
        return reg_nums

    # this function will returns Slot number in which a car with a given registration number is parked.
    def get_slot_by_reg_number(self, registration_number):
        for slot in self.slots:
            reg_num, _color = slot.get_car_parked()
            if reg_num == registration_number:
                return slot.get_slot_number()
        return "Not found"

    #this function will return Slot numbers of all slots where a car of a particular colour is parked.
    def get_slots_by_color(self, color):
        slots = []
        for slot in self.slots:
            reg_num, _color = slot.get_car_parked()
            if _color == color:
                slots.append(str(slot.get_slot_number()))
        return slots

    def show_status(self):
        print "Slot No. Registration No Colour"
        for slot in self.slots:
            if not slot.is_empty():
                registration_number, color = slot.get_car_parked()
                print slot.get_slot_number(), registration_number, color


