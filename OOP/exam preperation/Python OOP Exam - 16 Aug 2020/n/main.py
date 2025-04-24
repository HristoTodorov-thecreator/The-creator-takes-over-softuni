from system import System


def zero_test():
    System.register_power_hardware("HDD", 200, 200)
    System.register_heavy_hardware("SSD", 400, 400)
    print(System.analyze())
    System.register_light_software("HDD", "Test", 0, 10)
    print(System.register_express_software("HDD", "Test2", 100, 100))
    System.register_express_software("HDD", "Test3", 50, 100)
    System.register_light_software("SSD", "Windows", 20, 50)
    System.register_express_software("SSD", "Linux", 50, 100)
    System.register_light_software("SSD", "Unix", 20, 50)
    print(System.analyze())
    System.release_software_component("SSD", "Linux")
    print(System.system_split())


if __name__ == "__main__":
    zero_test()

import unittest
from project.system import System

class TestsSystem(unittest.TestCase):
    def setUp(self):
        System._hardware = []
        System._software = []

    def test_register_express_software_on_not_enough_space_or_memory_should_raise_error(self):
        System.register_power_hardware("TestHardware", 200, 50)
        with self.assertRaises(Exception) as cm:
            result = System.register_express_software("TestHardware", "Test", 200, 50)
        self.assertEqual(str(cm.exception), "Software cannot be installed")
        self.assertEqual(len(System._software), 0)

if __name__ == "__main__":
    unittest.main()