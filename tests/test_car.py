import unittest
from src.car import Car


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car("123", "Red")

    def test_color(self):
        self.assertEqual(self.car.get_color(), 'Red')

    def test_reg_number(self):
        self.assertEqual(self.car.get_registration_number(), '123')


if __name__ == '__main__':
    unittest.main()
