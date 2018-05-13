from src.parking_lot import ParkingLot

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
            elif input_array[0] == 'exit':
                break
            else:
                print "Command not found"
        except Exception as e:
            print e
            print "some error occured !!!"