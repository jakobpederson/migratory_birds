import unittest
import migratory_birds


class InvalidData(Exception):
    pass


class TestBirdCounter(unittest.TestCase):

    def setUp(self):
        self.client = migratory_birds.BirdCounter()

    def test_migratory_birds(self):
        self.assertEqual(2, self.client.migratory_birds(2, [2, 2, 2, 2, 3]))
        self.assertEqual(3, self.client.migratory_birds(3, [2, 2, 2, 2, 3, 3, 3, 3, 3]))
        self.assertEqual(4, self.client.migratory_birds(4, [2, 2, 2, 2, 3, 4, 4, 4, 4, 4]))
        self.assertEqual(5, self.client.migratory_birds(5, [2, 2, 2, 2, 3, 5, 5, 5, 5, 5]))

    def test_migratory_birds_always_return_lowest_answer(self):
        self.assertEqual(2, self.client.migratory_birds(2, [2, 2, 2, 2, 2, 3, 3, 3, 3, 3]))
        self.assertEqual(3, self.client.migratory_birds(3, [4, 4, 4, 4, 4, 3, 3, 3, 3, 3]))
        self.assertEqual(4, self.client.migratory_birds(4, [7, 7, 7, 7, 7, 3, 4, 4, 4, 4, 4]))
        self.assertEqual(5, self.client.migratory_birds(5, [6, 6, 6, 6, 6, 5, 5, 5, 5, 5]))

    def test_validate_data(self):
        self.assertTrue(isinstance(self.client.validate_data(0, [2, 2, 2, 3]), Exception))

    def test_validate_data_in_migratory_birds(self):
        self.assertEqual('invalid data', self.client.migratory_birds(0, [2, 2, 2, 2, 2, 3, 3, 3, 3, 3]))
        self.assertEqual('invalid data', self.client.migratory_birds(-1, [2, 2, 2, 2, 2, 3, 3, 3, 3, 3]))
        self.assertEqual('invalid data', self.client.migratory_birds(3e15, [2, 2, 2, 2, 2, 3, 3, 3, 3, 3]))
        self.assertEqual('invalid data', self.client.migratory_birds(2, []))
        self.assertEqual('invalid data', self.client.migratory_birds(2, [7, 7, 7]))
        self.assertEqual('invalid data', self.client.migratory_birds(2, [0, 0, 2]))


