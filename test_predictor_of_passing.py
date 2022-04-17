import unittest

class TestSOMETHING(unittest.TestCase):
    def test_A_GOOD_NAME(self):
        """ A GOOD DOCSTRING """
        #make a bit of dummy data
        #call your non-existent function
        #check if the result of the call is what it should be
        #   probably using self.assertEqual(something, something_else)
        data = search()
        result = deaths_per(data)
        self.assertEqual(result, 6)

    def test_A_GOOD_NAME(self):
        """ A GOOD DOCSTRING """
        #make a bit of dummy data
        #call your non-existent function
        #check if the result of the call is what it should be
        #   probably using self.assertEqual(something, something_else)


if __name__ == '__main__':
    unittest.main()