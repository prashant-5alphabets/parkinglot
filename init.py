from src.parking_lot import ParkingLot
import sys

class Init:
    @staticmethod
    def take_input(input_array, iteration):
        if input_array == None:
            input = raw_input()
        else:
            input = input_array[iteration].replace('\n', '') if len(input_array) > iteration else "exit"
        return input

    @staticmethod
    def return_file_if_given(args):
        input_array = None
        if len(args) > 1:
            filename = sys.argv[1]
            with open(filename) as file:
                input_array = file.readlines()
        return input_array

    def run(self):
        parking_lot = ParkingLot()
        input_given = self.return_file_if_given(sys.argv)
        iteration = 0
        while True:
            try:
                input_string = self.take_input(input_given, iteration)
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
                elif input_array[0] == 'exit':
                    break
                else:
                    print "Command not found"
                iteration += 1
            except Exception as e:
                print e
                print "some error occured !!!"

if __name__ == '__main__':
    init = Init()
    init.run()
