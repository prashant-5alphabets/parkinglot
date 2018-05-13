import unittest
from src.slot import Slot

class TestSlot(unittest.TestCase):
    def setUp(self):
        self.slot = Slot(1)

    def test_put_car(self):
        self.slot.put_car("123", "Red")
        reg_num, color = self.slot.get_car_parked()
        self.assertEqual((reg_num, color), ("123", "Red"))
        self.assertEqual(self.slot.is_empty(), False)

    def test_empty(self):
        self.slot.make_it_empty()
        self.assertEqual(self.slot.is_empty(), True)

    def test_slot_number(self):
        self.assertEqual(self.slot.get_slot_number(), 1)


if __name__ == '__main__':
    unittest.main()