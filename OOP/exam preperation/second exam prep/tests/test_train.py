import unittest

from project.train.train import Train

class TestTrain(unittest.TestCase):
    def setUp(self):
        self.train = Train('Express',3)

    def test_initialization(self):
        self.assertEqual(self.train.name, 'Express')
        self.assertEqual(self.train.capacity,3)
        self.assertEqual(len(self.train.passengers),0)

    def test_add_passenger_success(self):
        result = self.train.add('Alice')
        self.assertEqual(result,"Added passenger Alice")
        self.assertIn('Alice',self.train.passengers)

    def test_add_passenger_when_full(self):
        self.train.add("Alice")
        self.train.add('Bob')
        self.train.add('Alex')
        with self.assertRaises(ValueError) as context:
            self.train.add("Dave")
        self.assertEqual(str(context.exception), "Train is full")

    def test_add_existing_passenger(self):
        self.train.add('Alice')
        with self.assertRaises(Exception) as context:
            self.train.add('Alice')
        self.assertEqual(str(context.exception),"Passenger Alice Exists")

    def test_remove_passenger_success(self):
        self.train.add('Alice')
        result = self.train.remove('Alice')
        self.assertEqual(result,'Removed Alice')
        self.assertNotIn('Alice',self.train.passengers)

    def test_remove_nonexistent_passenger(self):
        with self.assertRaises(ValueError) as context:
            self.train.remove("Bob")
        self.assertEqual(str(context.exception), "Passenger Not Found")

    def test_zero_capacity_train(self):
        zero_capacity_train = Train("Empty", 0)
        with self.assertRaises(ValueError) as context:
            zero_capacity_train.add("Alice")
        self.assertEqual(str(context.exception), "Train is full")

    def test_multiple_operations(self):
        # Test a sequence of operations
        self.assertEqual(self.train.add("Alice"), "Added passenger Alice")
        self.assertEqual(self.train.add("Bob"), "Added passenger Bob")
        self.assertEqual(self.train.remove("Alice"), "Removed Alice")
        self.assertEqual(self.train.add("Charlie"), "Added passenger Charlie")
        self.assertEqual(self.train.remove("Bob"), "Removed Bob")
        self.assertEqual(len(self.train.passengers), 1)
        self.assertIn("Charlie", self.train.passengers)



if __name__ == '__main__':
    unittest.main()

