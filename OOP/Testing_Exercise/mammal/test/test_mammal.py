import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Mammal('Joro','cat','meow')

    def test_init(self):
        self.assertEqual(self.cat.name,'Joro')
        self.assertEqual(self.cat.type, 'cat')
        self.assertEqual(self.cat.sound, 'meow')

    def test_return_sound(self):
        self.assertEqual(self.cat.make_sound(),'Joro makes meow')

    def test_return_info(self):
        self.assertEqual(self.cat.info(), 'Joro is of type cat')

    def test_return_the_kingdom(self):
        self.assertEqual(self.cat.get_kingdom(),"animals")






if __name__ == '__main__':
    unittest.main()