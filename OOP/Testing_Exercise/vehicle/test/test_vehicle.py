import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(50,150)

    def test_init(self):
        self.assertEqual(self.car.fuel,50)
        self.assertEqual(self.car.capacity,50)
        self.assertEqual(self.car.horse_power,150)
        self.assertEqual(self.car.fuel_consumption,1.25)

    def test_drive_with_enough_fuel(self):
        self.car.drive(10)
        self.assertAlmostEqual(self.car.fuel, 37.5)

    def test_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual(str(ex.exception),"Not enough fuel")

    def test_refuel_within_capacity(self):
        self.car.drive(10)
        self.car.refuel(10)
        self.assertAlmostEqual(self.car.fuel, 47.5)

    def test_refuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(10)
        self.assertEqual(str(ex.exception),"Too much fuel")

    def test_the_str_method(self):
        expected = "The vehicle has 150 horse power with 50 fuel left and 1.25 fuel consumption"
        self.assertEqual(str(self.car),expected)











if __name__ == '__main__':
    unittest.main()
