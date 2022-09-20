import unittest

from project.movie import Movie


class TestMovie(unittest.TestCase):
    def test__init__method_when_data_is_as_intended(self):
        test_movie = Movie('Name1', 2001, 7.5)
        self.assertEqual(test_movie.name, 'Name1')
        self.assertEqual(test_movie.year, 2001)
        self.assertEqual(test_movie.rating, 7.5)
        self.assertListEqual(test_movie.actors, [])

    def test__name__setter_when_value_is_empty_string__expect_value_error(self):
        with self.assertRaises(ValueError) as ex:
            Movie('', 2001, 7.5)
        self.assertEqual(str(ex.exception), "Name cannot be an empty string!")

    def test__year__setter_when_value_is_less_than_min__expect_value_error(self):
        with self.assertRaises(ValueError) as ex:
            Movie('Name1', 1886, 7.5)
        self.assertEqual(str(ex.exception), "Year is not valid!")

    def test__add_actor__method_when_actor_is_non_existing__append_actor(self):
        test_movie = Movie('Name1', 2001, 7.5)
        test_movie.add_actor('Actor')
        self.assertListEqual(test_movie.actors, ['Actor'])

    def test__add_actor__method_when_actor_is_existing__return_message(self):
        test_movie = Movie('Name1', 2001, 7.5)
        test_movie.add_actor('Actor')
        result = test_movie.add_actor('Actor')
        self.assertEqual(result, "Actor is already added in the list of actors!")
        self.assertListEqual(test_movie.actors, ['Actor'])

    def test__gt__method__case1(self):
        test_movie = Movie('Name1', 2001, 7.5)
        test_movie1 = Movie('Name2', 2002, 6.5)
        result = test_movie > test_movie1
        self.assertEqual(result, '"Name1" is better than "Name2"')

    def test__gt__method_case2(self):
        test_movie = Movie('Name1', 2001, 7.5)
        test_movie1 = Movie('Name2', 2002, 8)
        result = test_movie > test_movie1
        self.assertEqual(result, '"Name2" is better than "Name1"')

    def test__repr__method_returns_string(self):
        test_movie = Movie('Name1', 2001, 7.5)
        test_movie.add_actor('Actor')
        expected = 'Name: Name1\nYear of Release: 2001\nRating: 7.50\nCast: Actor'
        self.assertEqual(repr(test_movie), expected)


if __name__ == '__main__':
    unittest.main()
