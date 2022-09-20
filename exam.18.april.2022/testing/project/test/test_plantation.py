import unittest

from project.plantation import Plantation


class TestingPlantation(unittest.TestCase):

    def test__init__for_correct_result(self):
        expected_size = 1
        expected_length_of_plants_dict = {}
        expected_length_of_workers_list = []
        plantation = Plantation(1)

        self.assertEqual(plantation.size, expected_size)
        self.assertDictEqual(plantation.plants, expected_length_of_plants_dict)
        self.assertListEqual(plantation.workers, expected_length_of_workers_list)

    def test_size_setter_for_negative_value(self):
        with self.assertRaises(ValueError) as ex:
            plantation = Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test__hire_worker__exception(self):
        plantation = Plantation(10)
        plantation.hire_worker('Ivan')
        with self.assertRaises(ValueError) as ex:
            plantation.hire_worker('Ivan')
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test__hire_work__if_appending_workers_properly(self):
        plantation = Plantation(10)
        self.assertEqual(plantation.hire_worker('Ivan'), f"Ivan successfully hired.")
        self.assertListEqual(plantation.workers, ['Ivan'])


    def test__len__return_correct_count(self):
        plantation = Plantation(10)
        plantation.hire_worker('Gosho')
        plantation.planting('Gosho', 'Magnoliq')
        plantation.planting('Gosho', 'GolemiqCvqt')
        self.assertEqual(2, len(plantation))

    def test__planting__if_worker_exists(self):
        plantation = Plantation(10)
        with self.assertRaises(ValueError) as ex:
            plantation.planting('Gosho', 'Mitko')
        self.assertEqual("Worker with name Gosho is not hired!", str(ex.exception))

    def test__planting__if_size_is_enough(self):
        plantation = Plantation(1)
        plantation.hire_worker('Gosho')
        plantation.planting('Gosho', 'GolemiqCvqt')
        with self.assertRaises(ValueError) as ex:
            plantation.planting('Gosho', 'GolemiqCvqt')
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test__planting__if_everything_is_okay(self):
        plantation = Plantation(1)
        plantation.hire_worker('Gosho')
        self.assertEqual(plantation.planting('Gosho', 'GolemiqCvqt'), "Gosho planted it's first GolemiqCvqt.")

    def diff_in_dict(self):
        plantation = Plantation(1)
        plantation.hire_worker('Gosho')
        self.assertDictEqual({'Gosho': ["GolemiqCvqt"]}, plantation.plants)

    def test__str__if_correct(self):
        plantation = Plantation(5)
        plantation.hire_worker('Gosho')
        plantation.hire_worker('Ivan')
        plantation.planting('Gosho', 'GolemiqCvqt')
        plantation.planting('Gosho', 'MalkiqCvqt')
        plantation.planting('Ivan', 'Tigura')
        expected_output = 'Plantation size: 5\nGosho, Ivan\nGosho planted: GolemiqCvqt, MalkiqCvqt\nIvan planted: Tigura'
        self.assertEqual(str(plantation), expected_output)

    def test__repr__if_correct(self):
        plantation = Plantation(10)
        plantation.hire_worker('Gosho')
        plantation.hire_worker('Ivan')
        expected_output = 'Size: 10\nWorkers: Gosho, Ivan'
        self.assertEqual(repr(plantation), expected_output)

if __name__ == "__main__":
    unittest.main()
