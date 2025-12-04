import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function.py'."""

    def test_first_last_name(self):
        """Nomes como 'Janis Jophin' funcionam?"""
        formatted_name = get_formatted_name('janis', 'jophin')
        self.assertEqual(formatted_name, 'Janis Jophin')

    def test_first_last_midle_name(self):
        """Nomes como 'Wolfgang Amadeus Mozart' funcionam?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()
