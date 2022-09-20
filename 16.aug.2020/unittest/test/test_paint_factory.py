import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.name = 'Name1'
        self.capacity = 10
        self.valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        self.test_factory = PaintFactory(self.name, self.capacity)

    def test__init__for_proper_initialization(self):
        self.assertEqual(self.test_factory.name, self.name)
        self.assertEqual(self.test_factory.capacity, self.capacity)
        self.assertListEqual(self.test_factory.valid_ingredients, self.valid_ingredients)
        self.assertDictEqual(self.test_factory.ingredients, {})

    def test__add_ingredient_method_if_product_type_not_in_ingredients__create_and_add_quantity(self):
        product_type = 'white'
        self.test_factory.add_ingredient(product_type, 5)
        self.assertEqual(len(self.test_factory.ingredients), 1)
        self.assertDictEqual(self.test_factory.ingredients, {'white': 5})
        self.assertEqual(self.test_factory.ingredients['white'], 5)

    def test__add_ingredient_method_if_product_type_is_in_ingredients__add_quantity(self):
        product_type = 'white'
        self.test_factory.add_ingredient(product_type, 5)
        self.test_factory.add_ingredient(product_type, 5)
        self.assertDictEqual(self.test_factory.ingredients, {'white': 10})
        self.assertEqual(self.test_factory.ingredients['white'], 10)

    def test__can_add_method_when_returns_true(self):
        result = self.test_factory.can_add(5)
        self.assertTrue(result)

    def test__can_add_method_when_returns_false(self):
        result = self.test_factory.can_add(11)
        self.assertFalse(result)

    def test__add_ingredient_method_when_not_enough_space__expect_error(self):
        with self.assertRaises(ValueError) as ex:
            self.test_factory.add_ingredient('white', 11)
        self.assertEqual(str(ex.exception), "Not enough space in factory")

    def test__add_ingredient_method_when_product_type_not_valid(self):
        with self.assertRaises(TypeError) as ex:
            self.test_factory.add_ingredient('Ferrari', 5)
        self.assertEqual(str(ex.exception), f"Ingredient of type Ferrari not allowed in PaintFactory")

    def test__remove_ingredient_method_when_working_as_intended__decrease_product_quantity(self):
        self.test_factory.add_ingredient('white', 5)
        self.test_factory.remove_ingredient('white', 4)
        self.assertEqual(self.test_factory.ingredients['white'], 1)
        self.assertDictEqual(self.test_factory.ingredients, {'white': 1})

    def test__remove_ingredient_method_when_product_quantity_becomes_less_than_zero__expect_error(self):
        self.test_factory.add_ingredient('white', 5)

        with self.assertRaises(ValueError) as ex:
            self.test_factory.remove_ingredient('white', 6)
        self.assertEqual(str(ex.exception), "Ingredients quantity cannot be less than zero")

    def test__remove_ingredient_method_when_no_such_ingredient__expect_error(self):
        with self.assertRaises(KeyError) as ex:
            self.test_factory.remove_ingredient('white', 6)
        self.assertEqual(str(ex.exception), repr('No such ingredient in the factory'))

    def test__products_property__returns_dict_of_ingredients(self):
        test_factory = PaintFactory('Factory', 100)
        test_factory.add_ingredient('white', 5)
        test_factory.add_ingredient('yellow', 5)
        test_factory.add_ingredient('yellow', 5)
        test_factory.add_ingredient("blue", 5)
        result = test_factory.products
        self.assertDictEqual(result, {'white': 5, 'yellow': 10, 'blue': 5})

    def test__repr__method__returns_string(self):
        self.test_factory.add_ingredient('white', 5)
        result = repr(self.test_factory)
        expected_result = f'Factory name: Name1 with capacity 10.\nwhite: 5\n'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()