import unittest
from src.parking_lot import ParkingLot


class TestParkingLot(unittest.TestCase):

    def setUp(self):
        self.parking_lot = ParkingLot()
        self.parking_lot.create_par_king_lot(6)

    def test_create_par_king_lot(self):
        self.assertEqual(len(self.parking_lot.get_slots()), 6)

    def test_park_car(self):
        self.parking_lot.park_car("123", "Red")
        slots = self.parking_lot.get_slots()
        self.assertEqual(slots[0].is_empty(), False)

    def test_get_reg_of_cars_of_particular_colors(self):
        self.parking_lot.park_car("123", "Red")
        reg_nums = self.parking_lot.get_reg_of_cars_of_particular_colors("Red")
        self.assertEqual(reg_nums, ["123"])

    def test_get_slots_by_color(self):
        self.parking_lot.park_car("123", "Red")
        slots = self.parking_lot.get_slots_by_color("Red")
        self.assertEqual(slots, ["1"])

    def test_get_slot_by_reg_number(self):
        self.parking_lot.park_car("123", "Red")
        slot = self.parking_lot.get_slot_by_reg_number("123")
        self.assertEqual(str(slot), "1")
        slot = self.parking_lot.get_slot_by_reg_number("1223")
        self.assertEqual(str(slot), "Not found")


if __name__ == '__main__':
    unittest.main()