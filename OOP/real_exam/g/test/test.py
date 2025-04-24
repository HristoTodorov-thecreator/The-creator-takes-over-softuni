import unittest
from project.star_system import StarSystem


class TestStarSystem(unittest.TestCase):
    def setUp(self) -> None:
        self.system = StarSystem('The Big','Red dwarf','Single',3,(0.2,0.8))
        self.system2 = StarSystem('The Small','Yellow dwarf',"Binary",5,(0.5,1.5))
        self.system3 = StarSystem('The lol',"Red giant","Triple",0,None)

    def test_the_init(self):
        self.assertEqual(self.system.name,'The Big')
        self.assertEqual(self.system.star_type,'Red dwarf')
        self.assertEqual(self.system.system_type,'Single')
        self.assertEqual(self.system.num_planets,3)
        self.assertEqual(self.system.habitable_zone_range,(0.2,0.8))

    def test_empty_name_raises(self):
        with self.assertRaises(Exception) as ex:
            self.system.name = ''
        self.assertEqual(str(ex.exception),"Name must be a non-empty string.")

    def test_invalid_star_type(self):
        with self.assertRaises(Exception) as ex:
            self.system.star_type = 'Invalid_star'
        self.assertEqual(str(ex.exception),"Star type must be one of ['Blue giant', 'Brown dwarf', 'Red dwarf', 'Red giant', 'Yellow dwarf'].")

    def test_invalid_system_type(self):

        with self.assertRaises(ValueError) as ex:
            self.system.system_type = "Quadruple"
        self.assertEqual(str(ex.exception), "System type must be one of ['Binary', 'Multiple', 'Single', 'Triple'].")

    def test_invalid_num_planets_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.system.num_planets = -1
        self.assertEqual(str(ex.exception), "Number of planets must be a non-negative integer.")

    def test_with_invalid_zones_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.system.habitable_zone_range = (1.5, 0.5)
        self.assertEqual(str(ex.exception),"Habitable zone range must be a tuple of two numbers (start, end) where start < end.")

    def test_is_habitable(self):

        self.assertTrue(self.system.is_habitable)
        self.assertFalse(self.system3.is_habitable)

    def test_comparison_with_non_habitable_system(self):

        with self.assertRaises(ValueError) as ex:
            g = self.system > self.system3
        self.assertEqual(str(ex.exception), "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

    def test_comparison_valid(self):

        self.assertTrue(self.system2 > self.system)

    def test_compare_star_systems(self):

        result = StarSystem.compare_star_systems(self.system2, self.system)
        self.assertEqual(result, 'The Small has a wider habitable zone than The Big.')

    def test_habitable_zone_update(self):
        self.system.habitable_zone_range = (0.1, 1.0)
        self.assertEqual(self.system.habitable_zone_range, (0.1, 1.0))

    def test_no_planets_and_zone(self):
        system_without_planets = StarSystem('Empty', 'Red dwarf', 'Single', 0, None)
        self.assertFalse(system_without_planets.is_habitable)

    def test_comparison_with_equal_habitable_zone(self):
        system1 = StarSystem('System 1', 'Red dwarf', 'Single', 3, (0.5, 1.0))
        system2 = StarSystem('System 2', 'Yellow dwarf', 'Binary', 4, (0.5, 1.0))
        self.assertFalse(system1 > system2)

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            StarSystem("", "Red dwarf", "Single", 0)
        with self.assertRaises(ValueError):
            StarSystem("   ", "Red dwarf", "Single", 0)
        valid_system = StarSystem("Sol", "Yellow dwarf", "Single", 8, (0.5, 1.5))
        self.assertEqual(valid_system.name, "Sol")

    def test_star_type_validation(self):
        with self.assertRaises(ValueError):
            StarSystem("Test", "White dwarf", "Single", 0)
        valid_system = StarSystem("Test", "Red dwarf", "Single", 0)
        self.assertEqual(valid_system.star_type, "Red dwarf")

    def test_system_type_validation(self):
        with self.assertRaises(ValueError):
            StarSystem("Test", "Red dwarf", "Quadruple", 0)
        valid_system = StarSystem("Test", "Red dwarf", "Binary", 0)
        self.assertEqual(valid_system.system_type, "Binary")

    def test_num_planets_validation(self):
        with self.assertRaises(ValueError):
            StarSystem("Test", "Red dwarf", "Single", -1)
        valid_system = StarSystem("Test", "Red dwarf", "Single", 0)
        self.assertEqual(valid_system.num_planets, 0)
        valid_system.num_planets = 5
        self.assertEqual(valid_system.num_planets, 5)

    def test_habitable_zone_validation(self):
        valid_system = StarSystem("Test", "Red dwarf", "Single", 0, (1, 2))
        self.assertEqual(valid_system.habitable_zone_range, (1, 2))
        with self.assertRaises(ValueError):
            valid_system.habitable_zone_range = (2, 1)
        with self.assertRaises(ValueError):
            valid_system.habitable_zone_range = (1, 1)
        with self.assertRaises(ValueError):
            valid_system.habitable_zone_range = (1, 2, 3)
        valid_system.habitable_zone_range = None
        self.assertIsNone(valid_system.habitable_zone_range)


    def test_is_habitable(self):
        habitable_system = StarSystem("Habitable", "Yellow dwarf", "Single", 3, (1, 3))
        self.assertTrue(habitable_system.is_habitable)

        no_zone_system = StarSystem("NoZone", "Yellow dwarf", "Single", 3, None)
        self.assertFalse(no_zone_system.is_habitable)

        no_planets_system = StarSystem("NoPlanets", "Yellow dwarf", "Single", 0, (1, 3))
        self.assertFalse(no_planets_system.is_habitable)


    def test_gt_method_valid(self):
        system1 = StarSystem("A", "Yellow dwarf", "Single", 3, (1, 3))
        system2 = StarSystem("B", "Red dwarf", "Single", 2, (2, 5))
        self.assertTrue(system2 > system1)
        self.assertFalse(system1 > system2)

    def test_gt_method_invalid(self):
        habitable = StarSystem("H", "Yellow dwarf", "Single", 1, (1, 2))
        non_habitable1 = StarSystem("NH1", "Red dwarf", "Single", 0, (1, 2))
        non_habitable2 = StarSystem("NH2", "Red dwarf", "Single", 1, None)

        with self.assertRaises(ValueError):
            _ = habitable > non_habitable1
        with self.assertRaises(ValueError):
            _ = non_habitable1 > non_habitable2


    def test_compare_star_systems_habitable(self):
        system1 = StarSystem("A", "Yellow dwarf", "Single", 3, (1, 3))
        system2 = StarSystem("B", "Red dwarf", "Single", 2, (2, 5))

        result1 = StarSystem.compare_star_systems(system1, system2)
        self.assertEqual(result1, "B has a wider or equal habitable zone compared to A.")

        result2 = StarSystem.compare_star_systems(system2, system1)
        self.assertEqual(result2, "A has a wider habitable zone than B.")

    def test_compare_star_systems_non_habitable(self):
        habitable = StarSystem("H", "Yellow dwarf", "Single", 1, (1, 2))
        non_habitable = StarSystem("NH", "Red dwarf", "Single", 0, (1, 2))

        result = StarSystem.compare_star_systems(habitable, non_habitable)
        self.assertIn("lack a defined habitable zone or planets", result)

        result_both_non = StarSystem.compare_star_systems(non_habitable, non_habitable)
        self.assertIn("lack a defined habitable zone or planets", result_both_non)






if __name__ == '__main__':
    unittest.main()