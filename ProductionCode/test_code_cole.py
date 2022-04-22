import unittest
from deaths_per import *
fr

class TestSearchResults(unittest.TestCase):

    def test_state_age_gender(self):
        """ Test that it can sum the data for a state, an age, and a gender """
        search = searchInfo("California","37","M",None)
        check_deaths_per_results(self, search, 170)

    def test_state_age_cause(self):
        """ Test that it can sum the data for a state, an age, and a cause """
        search = searchInfo("California","37",None,"Heart Attack")
        check_deaths_per_results(self, search, 180)

    def test_state_gender_cause(self):
        """ Test that it can sum the data for a state, a gender and a cause """
        search = searchInfo("California",None,"M","Heart Attack")
        check_deaths_per_results(self, search, 140)

    def test_age_gender_cause(self):
        """ Test that it can sum the data for an age, a gender and a cause """
        search = searchInfo(None,"37","F","Heart Attack")
        check_deaths_per_results(self, search, 60)
        
    def test_edge_case(self):
        """ Test that it can find a very specific data point """
        search = searchInfo("New Jersey","20","M","Infection")
        check_deaths_per_results(self, search, 50)
        
    def test_equal_or_none(self):
        """ Unit test that checks if data loads correctly """
        value1 = 30
        value2 = 30
        check_equal_or_none_results(self, value1, value2)


def check_deaths_per_results(self, search, expected_result):
    result = deaths_per(search)
    assert_equal(self, result, expected_result)

def check_equal_or_none_results(self, value1, value2):
    result = equalOrNone(value1, value2)
    assert_equal(self, result, True)

def assert_equal(self, result, expected_result):
    self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()