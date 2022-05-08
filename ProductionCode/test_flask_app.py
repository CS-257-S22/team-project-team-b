"""
Written by Kai Weiner
"""

import unittest
from flask_app import *
from csv_reading import *

"""
The test suite for flask app
"""

class test_return_leading_cause(unittest.TestCase):

    def test_sum_deaths_by_state(self):
        
        """ Test that it can sum the data for one state """
        result = get_response("deaths_per","(-s California)")
        self.assertEqual(result, "The number of people who died under the category: state = California, age = all, gender = all, cause = all, is: 90.")

    # def test_sum_deaths_by_cause(self):
    #     """ Test that it can sum the data for one state """
    #     search = SearchInfo(None,None,None,"Infection")
    #     result = deaths_per(search, deaths_data)
    #     self.assertEqual(result, 70)

    # def test_return_leading_cause_based_on_state(self): 
    #     """Test if return_leading_cause() can find and order the top causes of death of a given state"""
    #     search = SearchInfo("California",None,None)
    #     result_state = return_leading_cause(search)
    #     sample_CoD_state = ["Assault by handgun discharge","Intentional self-harm by other and unspecified firearm discharge","Assault by other and unspecified firearm discharge"]
    #     self.assertEqual(result_state, sample_CoD_state)
    
    # def test_return_leading_cause_based_on_gender(self): 
    #     """Test if return_leading_cause() can find and order the top causes of death of a given gender"""
    #     search = SearchInfo(None,None,"F")
    #     result_gender = return_leading_cause(search)
    #     sample_CoD_gender = ["Assault by handgun discharge","Intentional self-harm by other and unspecified firearm discharge","Assault by other and unspecified firearm discharge"]
    #     self.assertEqual(result_gender, sample_CoD_gender)

if __name__ == '__main__':
    unittest.main()