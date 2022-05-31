from unittest import result
from flask_app_model import *
import unittest

class TestFlaskAppModel(unittest.TestCase):

    def test_get_query_results(self):
        result = get_query_result("SELECT * FROM death_data WHERE age=%s AND state_name=%s AND gender=%s;", (18, "Alaska", "M"))
        self.assertEqual(result, [('Alaska', 18, 'M', 'Miscellaneous', 42)])
    
    def test_return_list_of_states(self):
        states = return_list_of_states()
        self.assertEqual(states, ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'])

    def test_return_list_of_causes(self):
        causes = return_list_of_causes(SearchArgs("Minnesota", 18, "M", None))
        self.assertEqual(causes, ['Assault by other and unspecified firearm discharge', 'Intentional self-harm by hanging, strangulation and suffocation', 'Intentional self-harm by rifle, shotgun and larger firearm discharge', 'Miscellaneous'])

    def test_get_search_result_from_function_dp_no_parameters(self):
        result = get_search_result_from_function("dp", {"state_name": "None", "age": "None", "gender": "None", "cause": "None"})
        self.assertEqual(result.deaths, 14634955)

    def test_get_search_result_from_function_dp_parameters(self):
        result = get_search_result_from_function("dp", {"state_name": "Colorado", "age": "None", "gender": "M", "cause": "Person injured in unspecified motor-vehicle accident, traffic"})
        self.assertEqual(result.deaths, 499)

    def test_get_search_result_from_function_lc_no_parameters(self):
        result = get_search_result_from_function("lc", {"state_name": "None", "age": "None", "gender": "None", "cause": "None"})
        self.assertEqual(result.cause, "atherosclerotic heart disease")

    def test_get_search_result_from_function_lc_parameters(self):
        result = get_search_result_from_function("lc", {"state_name": "New Jersey", "age": "62", "gender": "M", "cause": "None"})
        self.assertEqual(result.cause, "covid-19")
    
    def test_get_deaths_per_arguments(self):
        result = get_deaths_per_arguments(SearchArgs("New Hampshire", 30, None, "Acidosis"))
        self.assertEqual(result.state, "New Hampshire")
    
    def test_get_deaths_per_arguments_no_arguments(self):
        result = get_deaths_per_arguments(SearchArgs(None, None, None, None))
        self.assertEqual(result.state, "all states")
        self.assertEqual(result.age, "all ages")
        self.assertEqual(result.gender, "all genders")
        self.assertEqual(result.cause, "all causes")
    
    def test_get_leading_cause_per_arguments(self):
        result = get_leading_cause_per_arguments(SearchArgs("New Hampshire", 30, "M", None))
        self.assertEqual(result.cause, "accidental poisoning by and exposure to narcotics and psychodysleptics [hallucinogens], not elsewhere classified")

    def test_get_leading_cause_per_arguments_no_arguments(self):
        result = get_leading_cause_per_arguments(SearchArgs(None, None, None, None))
        self.assertEqual(result.state, "all states")
        self.assertEqual(result.age, "all ages")
        self.assertEqual(result.gender, "all genders")
        self.assertEqual(result.cause, "atherosclerotic heart disease")
    
if __name__ == "__main__":
    unittest.main()