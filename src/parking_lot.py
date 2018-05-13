from src.slot import Slot

class ParkingLot:
    def __init__(self):
        self.slot_count = 0
        self.parked_cars = {}
        self.slots = []

    def create_par_king_lot(self, slots):
        self.slot_count = slots
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
        print ", ".join(reg_nums)

    # this function will returns Slot number in which a car with a given registration number is parked.
    def get_slot_by_reg_number(self, registration_number):
        for slot in self.slots:
            reg_num, _color = slot.get_car_parked()
            if reg_num == registration_number:
                print slot.get_slot_number()
                return
        print "Not found"

    #this function will return Slot numbers of all slots where a car of a particular colour is parked.
    def get_slots_by_color(self, color):
        slots = []
        for slot in self.slots:
            reg_num, _color = slot.get_car_parked()
            if _color == color:
                slots.append(str(slot.get_slot_number()))
        print ", ".join(slots)

    def show_status(self):
        print "Slot No. Registration No Colour"
        for slot in self.slots:
            if not slot.is_empty():
                registration_number, color = slot.get_car_parked()
                print slot.get_slot_number(), registration_number, color


if __name__ == '__main__':
    parking_lot = ParkingLot()
    while True:
        try:
            input_string = raw_input()
            input_array = input_string.split(" ")
            if input_array[0] == 'create_parking_lot':
                parking_lot.create_par_king_lot(int(input_array[1]))
            elif input_array[0] == 'park':
                parking_lot.park_car(input_array[1], input_array[2])
            elif input_array[0] == 'leave':
                parking_lot.empty_slot(int(input_array[1]))
            elif input_array[0] == 'status':
                parking_lot.show_status()
            elif input_array[0] == 'registration_numbers_for_cars_with_colour':
                parking_lot.get_reg_of_cars_of_particular_colors(input_array[1])
            elif input_array[0] == 'slot_numbers_for_cars_with_colour':
                parking_lot.get_slots_by_color(input_array[1])
            elif input_array[0] == 'slot_number_for_registration_number':
                parking_lot.get_slot_by_reg_number(input_array[1])
            else:
                print "Command not found"
        except Exception as e:
            print e
            print "some error occured !!!"


