import logging

class ParkingLot:
    def __init__(self):
        self.slot_count = 0

    def create_par_king_lot(self, slots):
        self.slot_count = slots
        logging.info("Created a parking lot with " + slots + " slots")

    #this function will be used to park a car
    def park_car(self, registration_number, color):
        logging.info(registration_number, color)

    # this function will be release a slot
    def empty_slot(self, slot_number):
        logging.info(slot_number)

    # this function will return `Registration numbers of all cars of a particular colour`
    def get_reg_of_cars_of_particular_colors(self, color):
        logging.info(color)

    # this function will returns Slot number in which a car with a given registration number is parked.
    def get_slot_by_reg_number(self, registration_number):
        logging.info(registration_number)

    #this function will return Slot numbers of all slots where a car of a particular colour is parked.
    def get_slots_by_color(self, registration_number):
        logging.info(registration_number)

    def show_status(self):
        logging.info("Slot No. Registration No Colour")


if __name__ == '__main__':
    parking_lot = ParkingLot()
    while True:
        try:
            input_string = raw_input()
            input_array = input_string.split(" ")
            if input_array[0] == 'create_parking_lot':
                parking_lot.create_par_king_lot(input_array[1])
            elif input_array[0] == 'park':
                parking_lot.park_car(input_array[1], input_array[2])
            elif input_array[0] == 'leave':
                parking_lot.empty_slot(input_array[1])
            elif input_array[0] == 'status':
                parking_lot.show_status()
            elif input_array[0] == 'registration_numbers_for_cars_with_colour':
                parking_lot.get_reg_of_cars_of_particular_colors(input_array[1])
            elif input_array[0] == 'slot_numbers_for_cars_with_colour':
                parking_lot.get_slots_by_color(input_array[1])
            elif input_array[0] == 'slot_number_for_registration_number':
                parking_lot.get_slot_by_reg_number(input_array[1])
            else:
                logging.info("Command not found")
        except Exception as e:
            logging.info("some error occured !!!")


