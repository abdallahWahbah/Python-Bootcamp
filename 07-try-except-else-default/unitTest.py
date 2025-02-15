import unittest 
from cap import cap_text

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'abdallah'
        capitalizedText = cap_text(text)
        self.assertEqual(capitalizedText, "Abdallah")

    def test_multiple_words(self):
        text = 'abdallah wahbah'
        capitalizedText = cap_text(text)
        self.assertEqual(capitalizedText, "abdallah wahbah") # AssertionError: 'Abdallah Wahbah' != 'abdallah wahbah'

if __name__ == "__main__":
    unittest.main()