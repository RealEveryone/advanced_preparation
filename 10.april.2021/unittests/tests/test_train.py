import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self) -> None:
        self.expected_values = {'Name': 'Train', 'Capacity': 10}
        self.test_train = Train(self.expected_values['Name'], self.expected_values['Capacity'])

    def test_class_attributes(self):
        self.assertEqual("Train is full", self.test_train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.test_train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.test_train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.test_train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.test_train.PASSENGER_REMOVED)
        self.assertEqual(0, self.test_train.ZERO_CAPACITY)

    def test__init__for_proper_initialization(self):
        self.assertEqual(self.expected_values['Name'], self.test_train.name)
        self.assertEqual(self.expected_values['Capacity'], self.test_train.capacity)
        self.assertEqual(0, len(self.test_train.passengers))
        self.assertListEqual([], self.test_train.passengers)

    def test__add__method_when_working_properly(self):
        result = self.test_train.add('Passenger1')
        expected = self.test_train.PASSENGER_ADD.format('Passenger1')
        self.assertEqual(result, expected)
        self.assertListEqual(self.test_train.passengers, ['Passenger1'])

    def test__add__method_when_passengers_are_more_than_capacity(self):
        test_train = Train('Train', 1)
        test_train.add('Passenger1')
        with self.assertRaises(ValueError) as ex:
            test_train.add('Passenger1')
        self.assertEqual(str(ex.exception), self.test_train.TRAIN_FULL)

    def test__add__method_when_passengers_already_in_list_except_error(self):
        self.test_train.add('Passenger1')
        with self.assertRaises(ValueError) as ex:
            self.test_train.add('Passenger1')
        expected = self.test_train.PASSENGER_EXISTS.format('Passenger1')
        self.assertEqual(str(ex.exception), expected)

    def test__remove__method_when_working_as_intended__remove_passenger_from_list(self):
        self.test_train.add('Passenger1')
        result = self.test_train.remove('Passenger1')
        self.assertListEqual(self.test_train.passengers, [])
        expected = self.test_train.PASSENGER_REMOVED.format('Passenger1')
        self.assertEqual(result, expected)

    def test__remove__method_passenger_not_in_list__raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.test_train.remove('Passenger1')
        result = self.test_train.PASSENGER_NOT_FOUND.format('Passenger1')
        self.assertEqual(str(ex.exception), result)

if __name__ == '__main__':
    unittest.main()
