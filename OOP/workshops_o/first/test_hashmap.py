from unittest import TestCase,main
from first.hash_table import HashTable


class TestHashTable(TestCase):
    def setUp(self) -> None:
        self.table = HashTable()

    def test_correct_init(self):
        self.assertEqual(4, self.table._HashTable__max_capacity)
        self.assertEqual([None] * 4,self.table._HashTable__keys)
        self.assertEqual([None] * 4, self.table._HashTable__values)
        self.assertEqual(0,self.table._HashTable__length)

    def test_get_item_correct(self):
        self.table['name'] = 'Peter'

        self.assertEqual('Peter',self.table.get('name'))

    def test_get_item_invalid_raises(self):
        with self.assertRaises(KeyError) as ex:
            result = self.table['non existing']
        self.assertEqual(
            "'not found in hash table'",
            str(ex.exception)
        )

    def test_correct_override(self):
        self.table['name'] = 'Peter'
        self.table['name'] = 'Diyan'

        self.assertEqual('Diyan',self.table['name'])
        self.assertEqual(1,len(self.table))

    def test_resize_when_table_is_full(self):
        self.table['name'] = 'Peter'
        self.table['can_swim'] = 'True'
        self.table['watch'] = '24'
        self.table['t'] = 'True'

        self.assertEqual(4,self.table._HashTable__max_capacity)

        self.table['Mitko'] = 'Patrona'

        self.assertEqual(8, self.table._HashTable__max_capacity)

    def test_index_collision(self):
        self.table['name'] = 'Peter'
        self.table['age'] = 25
        self.table['is_pet_owner'] = True

        result = self.table._HashTable__calc_index('is_driver')
        self.assertEqual(0,result)

    def test_str(self):
        self.table['name'] = 'Peter'
        self.table['age'] = 25

        expected = '{name: Peter, age: 25}'
        result = str(self.table)

        self.assertEqual(result,expected)

    def test_add(self):
        self.table.add('name','peter')
        self.assertEqual(self.table['name'],'peter')

    def test_get_without_message(self):
        result = self.table.get('non existing key')
        self.assertIsNone(result)

    def test_get_return_non_existing_key(self):
        result = self.table.get('non existing key','the message')
        self.assertEqual('the message',result)

    def test_remove_item(self):
        self.table['name'] = 'Peter'
        self.table['age'] = 25


        self.assertEqual(str(self.table), '{name: Peter, age: 25}')
        self.assertEqual(len(self.table), 2)


        self.table.remove_item('name')


        self.assertEqual(str(self.table), '{age: 25}')
        self.assertEqual(len(self.table), 1)


        with self.assertRaises(KeyError) as ex:
            self.table.remove_item('non_existing')
        self.assertEqual(str(ex.exception), "Key 'non_existing' not found!")








if __name__ == '__main__':
    main()