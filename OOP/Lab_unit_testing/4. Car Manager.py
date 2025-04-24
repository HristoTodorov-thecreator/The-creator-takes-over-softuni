import unittest


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Toyota", "Corolla", 5, 50)


    def test_the_constructor(self):
        self.assertEqual(self.car.make,'Toyota')
        self.assertEqual(self.car.model,'Corolla')
        self.assertEqual(self.car.fuel_consumption,5)
        self.assertEqual(self.car.fuel_capacity,50)
        self.assertEqual(self.car.fuel_amount,0)

    def test_make_setter_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual(str(ex.exception),"Make cannot be null or empty!")

    def test_model_setter_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual(str(ex.exception),"Model cannot be null or empty!")

    def test_if_fuel_consumption_is_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -5
        self.assertEqual(str(ex.exception),"Fuel consumption cannot be zero or negative!")

    def test_if_fuel_consumption_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual(str(ex.exception),"Fuel consumption cannot be zero or negative!")

    def test_if_fuel_capacity_is_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -5
        self.assertEqual(str(ex.exception),"Fuel capacity cannot be zero or negative!")

    def test_if_fuel_capacity_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual(str(ex.exception),"Fuel capacity cannot be zero or negative!")

    def test_if_fuel_amount_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount  = -5
        self.assertEqual(str(ex.exception),"Fuel amount cannot be negative!")

    def test_if_add_fuel(self):
        self.car.refuel(1)
        self.assertEqual(self.car.fuel_amount,1)

    def test_if_you_add_more_fuel_than_capacity(self):
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_amount,50)

    def test_invalid_refuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual(str(ex.exception),"Fuel amount cannot be zero or negative!")

    def test_negative_refuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual(str(ex.exception),"Fuel amount cannot be zero or negative!")

    def test_drive_enough_fuel(self):
        self.car.refuel(10)
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 5)

    def test_drive_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(2000)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")





if __name__ == '__main__':
    unittest.main()
