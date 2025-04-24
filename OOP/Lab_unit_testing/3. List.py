import unittest



class TestIntegerList(unittest.TestCase):

    def setUp(self):
        self.lst = IntegerList(1, 2, 3, 4)

    def test_init_if_only_integers(self):
        self.assertEqual(self.lst.get_data(),[1,2,3,4])

    def test_if_non_integers_are_ignored(self):
        lst = IntegerList(1,3,2.5,'g')
        self.assertEqual(lst.get_data(),[1,3])

    def test_if_the_valid_element_is_added(self):
        self.lst.add(5)
        self.assertEqual(self.lst.get_data(),[1,2,3,4,5])

    def test_add_function_if_it_ignores_wrong_data(self):
        with self.assertRaisesRegex(ValueError, "Element is not Integer"):
            self.lst.add("a")

    def test_if_valid_index_is_removed(self):
        removed = self.lst.remove_index(1)
        self.assertEqual(removed,2)
        self.assertEqual(self.lst.get_data(),[1,3,4])

    def test_if_invalid_raises_message(self):
        with self.assertRaisesRegex(IndexError, "Index is out of range"):
            self.lst.remove_index(10)

    def test_to_get_a_valid_index(self):

        self.assertEqual(self.lst.get(1),2)

    def test_get_if_the_valid_index_is_ignored(self):
        with self.assertRaisesRegex(IndexError,"Index is out of range"):
            self.lst.get(10)

    def test_get_the_biggest_num(self):
        self.lst.add(10)
        self.assertEqual(self.lst.get_biggest(),10)

    def test_get_the_index(self):
        self.assertEqual(self.lst.get_index(2),1)

    def test_if_it_will_insert_valid_element(self):
        self.lst.insert(1,99)
        self.assertEqual(self.lst.get_data(),[1,99,2,3,4])

    def test_insert_invalid_index_raises(self):
        with self.assertRaisesRegex(IndexError,"Index is out of range"):
            self.lst.insert(10,2)

    def test_insert_invalid_el_raises(self):
        with self.assertRaisesRegex(ValueError,"Element is not Integer"):
            self.lst.insert(1,'g')





if __name__ == "__main__":
    unittest.main()