import unittest

from project.library import Library


class TestLibrary(unittest.TestCase):

    def test__init__method_for_proper_initialization(self):
        test_library = Library('Name')
        self.assertEqual(test_library.name, 'Name')
        self.assertDictEqual(test_library.books_by_authors, {})
        self.assertDictEqual(test_library.readers, {})

    def test__name__setter_when_empty_string_is_given__expect_value_error(self):
        with self.assertRaises(ValueError) as ex:
            Library('')
        self.assertEqual(str(ex.exception), "Name cannot be empty string!")

    def test__add_book_method(self):
        test = Library('Name')
        test.add_book('Author', 'BookTittle')
        self.assertDictEqual(test.books_by_authors, {'Author': ['BookTittle']})

    def test__add__reader_method_properly_working__no_message_expected(self):
        test = Library('Name')
        test.add_reader('Reader')
        self.assertDictEqual(test.readers, {'Reader': []})

    def test__add_reader__method_when_reader_already_in_readers__expect_message(self):
        test = Library('Name')
        test.add_reader('Reader')
        result = test.add_reader('Reader')
        self.assertEqual(result, "Reader is already registered in the Name library.")

    def test__rent_book__method__happy_case(self):
        test = Library('Name')
        test.add_reader('Reader')
        test.add_book('Author', 'BookTittle')
        test.rent_book('Reader', 'Author', 'BookTittle')
        self.assertDictEqual(test.readers, {'Reader': [{'Author': 'BookTittle'}]})
        self.assertDictEqual(test.books_by_authors, {'Author': []})

    def test__rent_book__method__if_reader_not_in_readers(self):
        test = Library('Name')
        test.add_book('Author', 'BookTittle')
        result = test.rent_book('Reader', 'Author', 'BookTittle')
        self.assertEqual(result, "Reader is not registered in the Name Library.")

    def test__rent_book__method__if_author_not_in_authors(self):
        test = Library('Name')
        test.add_reader('Reader')
        result = test.rent_book('Reader', 'Author', 'BookTittle')
        self.assertEqual(result, "Name Library does not have any Author's books.")

    def test__rent_book__method__if_book_not_in_author_books(self):
        test = Library('Name')
        test.add_reader('Reader')
        test.add_book('Author', 'BookTittle')
        result = test.rent_book('Reader', 'Author', 'BookTittle2')
        book_title = 'BookTittle2'
        self.assertEqual(result, f"""Name Library does not have Author's "{book_title}".""")

if __name__ == '__main__':
    unittest.main()
