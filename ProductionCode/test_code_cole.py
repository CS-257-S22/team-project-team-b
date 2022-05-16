import unittest
from deaths_per import *
from SearchInfo import *
from csv_reading import *

class TestSearchResults(unittest.TestCase):

    def test_state_age_gender(self):
        """ Test that it can sum the data for a state, an age, and a gender """
        search = SearchInfo("California","37","M",None)
        check_deaths_per_results(self, search, 80)

    def test_state_age_cause(self):
        """ Test that it can sum the data for a state, an age, and a cause """
        search = SearchInfo("California","37",None,"Heart Attack")
        check_deaths_per_results(self, search, 80)

    def test_state_gender_cause(self):
        """ Test that it can sum the data for a state, a gender and a cause """
        search = SearchInfo("California",None,"M","Heart Attack")
        check_deaths_per_results(self, search, 80)

    def test_age_gender_cause(self):
        """ Test that it can sum the data for an age, a gender and a cause """
        search = SearchInfo(None,"37","F","Heart Attack")
        check_deaths_per_results(self, search, 20)
        
    def test_edge_case(self):
        """ Test that it can find a very specific data point """
        search = SearchInfo("New Jersey","20","M","Infection")
        check_deaths_per_results(self, search, 50)
        
    def test_equal_or_none(self):
        """ Unit test that checks if data loads correctly """
        value1 = 30
        value2 = 30
        check_equal_or_none_results(self, value1, value2)


def check_deaths_per_results(self, search, expected_result):
    result = get_deaths_per_arguments(search, data)
    assert_equal(self, result, expected_result)

def check_equal_or_none_results(self, value1, value2):
    result = is_equal_or_none(value1, value2)
    assert_equal(self, result, True)

def assert_equal(self, result, expected_result):
    self.assertEqual(result, expected_result)

if __name__ == '__main__':
    data = get_CSV_data_as_list("Test Data CSV - Sheet1.csv")
    unittest.main()