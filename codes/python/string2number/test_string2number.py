import unittest
from string2number import string2number, en_numbers_dict, fa_numbers_dict


class TestStringToNumber(unittest.TestCase):

    # Test Cases English Strings

    def test_en_zero(self):
        self.assertEqual(string2number("zero", en_numbers_dict), 0)

    def test_en_one(self):
        self.assertEqual(string2number("one", en_numbers_dict), 1)

    def test_en_hundred(self):
        self.assertEqual(string2number("one hundred", en_numbers_dict), 100)

    def test_en_thousand(self):
        self.assertEqual(string2number("one thousand", en_numbers_dict), 1000)

    def test_en_million(self):
        self.assertEqual(string2number("one million", en_numbers_dict), 1000000)

    def test_en_complex(self):
        self.assertEqual(string2number("one thousand five hundred and sixty seven", en_numbers_dict), 1567)

    def test_en_large(self):
        self.assertEqual(string2number("one billion", en_numbers_dict), 1000000000)

    def test_en_with_and(self):
        self.assertEqual(string2number("one hundred and twenty three", en_numbers_dict), 123)

    def test_en_invalid(self):
        self.assertEqual(string2number("twenty and five", en_numbers_dict), 25)

    def test_en_large_combined(self):
        self.assertEqual(string2number("three million two hundred thousand and eighteen", en_numbers_dict), 3200018)

    # Test Cases for Persian Strings
    def test_fa_zero(self):
        self.assertEqual(string2number("صفر", fa_numbers_dict), 0)

    def test_fa_one(self):
        self.assertEqual(string2number("یک", fa_numbers_dict), 1)

    def test_fa_hundred(self):
        self.assertEqual(string2number("صد", fa_numbers_dict), 100)

    def test_fa_thousand(self):
        self.assertEqual(string2number("یک هزار", fa_numbers_dict), 1000)

    def test_fa_million(self):
        self.assertEqual(string2number("یک میلیون", fa_numbers_dict), 1000000)

    def test_fa_complex(self):
        self.assertEqual(string2number("یک هزار و پانصد", fa_numbers_dict), 1500)

    def test_fa_large(self):
        self.assertEqual(string2number("یک میلیارد", fa_numbers_dict), 1000000000)

    def test_fa_with_and(self):
        self.assertEqual(string2number("یک صد و بیست و سه", fa_numbers_dict), 123)

    def test_fa_large_combined(self):
        self.assertEqual(string2number("دو میلیون و پانصد هزار", fa_numbers_dict), 2500000)

    def test_fa_large_complex(self):
        self.assertEqual(string2number("دو میلیون و پانصد هزار و دویست و شصت و هفت", fa_numbers_dict), 2500267)

    # Empty Strings
    def test_fa_empty(self):
        self.assertEqual(string2number("", fa_numbers_dict), 'string is empty')

    def test_en_empty(self):
        self.assertEqual(string2number("", en_numbers_dict), 'string is empty')


if __name__ == '__main__':
    unittest.main()
