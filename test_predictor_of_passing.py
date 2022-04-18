from mimetypes import init
import unittest
from deaths_per import *

class TestSOMETHING(unittest.TestCase):

    def test_purposely_wrong_return(self):
        """ Test that it can sum the data for one state """
        search = searchInfo("California",None,None,None)
        result = deaths_per(search)
        self.assertEqual(result, 100)

    def test_sum_deaths_by_state(self):
        """ Test that it can sum the data for one state """
        search = searchInfo("California",None,None,None)
        result = deaths_per(search)
        self.assertEqual(result, 90)
    
    def test_sum_deaths_by_age(self):
        """ Test that it can sum the data for one age """
        search = searchInfo(None,"37",None,None)
        result = deaths_per(search)
        self.assertEqual(result, 100)
    
    def test_sum_deaths_by_gender(self):
        """ Test that it can sum the data for one gender """
        search = searchInfo(None,None,"M",None)
        result = deaths_per(search)
        self.assertEqual(result, 130)

    def test_sum_deaths_by_cause(self):
        """ Test that it can sum the data for one state """
        search = searchInfo(None,None,None,"Infection")
        result = deaths_per(search)
        self.assertEqual(result, 70)

    def test_intersection_sum_deaths_by_age_and_gender(self):
        """ Test that it can sum the data for one state """
        search = searchInfo(None,"49","F",None)
        result = deaths_per(search)
        self.assertEqual(result, 70)

    def test_get_single_datapoint_all_terms(self):
        """ Test that it can sum the data for one state """
        search = searchInfo("Nebraska","2","F","Infection")
        result = deaths_per(search)
        self.assertEqual(result, 20)
    
    def test_get_all_deaths(self):
        """ Test that it can sum the data for one state """
        search = searchInfo(None,None,None,None)
        result = deaths_per(search)
        self.assertEqual(result, 270)

if __name__ == '__main__':
    unittest.main()