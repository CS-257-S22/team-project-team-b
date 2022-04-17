import unittest
import Predictors_of_passing


state = "Alabama"
age = "22"
gender = "F"

# The test class for leading_cause(arguement) checks whether the function captures the correct items and the correct number of items. Within this class, there are functions for each combonation of arguement varible that leading_cause(arguement) can take in. This class, however, does not check for correct sorting order.
####Should there two be two assertion cases within a single function??????

class test_leading_cause(unittest.TestCase):

    def test_find_leading_cause_based_on_age(self): 
        result = leading_cause(age)
        sample_COD = ["Person injured in collision between other specified motor vehicles (traffic)","Person injured in unspecified motor-vehicle accident, traffic","Assault by other and unspecified firearm discharge"]
        for i in result:
            self.assertIn(result[i], sample_COD)
        self.assertEqual(len(result),len(sample_COD)) 


    def test_find_leading_cause_based_on_state(self): 
        result = leading_cause(state)
        sample_COD = ["Assault by handgun discharge","Intentional self-harm by other and unspecified firearm discharge","Assault by other and unspecified firearm discharge"]
        for i in result:
            self.assertIn(result[i], sample_COD)
        self.assertEqual(len(result),len(sample_COD)) 


    def test_find_leading_cause_based_on_gender(self): 
        result = leading_cause(gender)
        sample_COD = ["Assault by handgun discharge","Intentional self-harm by other and unspecified firearm discharge","Assault by other and unspecified firearm discharge"]
        for i in result:
            self.assertIn(result[i], sample_COD)
        self.assertEqual(len(result),len(sample_COD)) 
    
    def test_find_leading_cause_based_on_ageGender(self): 
        result = leading_cause(gender,age) 
        sample_COD = ["Assault by handgun discharge","Intentional self-harm by other and unspecified firearm discharge","Assault by other and unspecified firearm discharge"]
        for i in result:
            self.assertIn(result[i], sample_COD)
        self.assertEqual(len(result),len(sample_COD)) 

    def test_find_leading_cause_based_on_genderLocation(self): 
        result = leading_cause(gender, state)
        sample_COD = ["Assault by handgun discharge","Intentional self-harm by other and unspecified firearm discharge","Assault by other and unspecified firearm discharge"]
        for i in result:
            self.assertIn(result[i], sample_COD)
        self.assertEqual(len(result),len(sample_COD)) 

    def test_find_leading_cause_based_on_ageLocation(self): 
        result = leading_cause(age, state)
        sample_COD= ["Person injured in collision between other specified motor vehicles (traffic)","Person injured in unspecified motor-vehicle accident, traffic","Assault by other and unspecified firearm discharge"]
        for i in result:
            self.assertIn(result[i], sample_COD)
        self.assertEqual(len(result),len(sample_COD)) 

    def test_find_leading_cause_based_on_genderAgeLocation(self): 
        result = leading_cause(gender,age,state)
        sample_COD = ["Person injured in collision between other specified motor vehicles (traffic)","Person injured in unspecified motor-vehicle accident, traffic","Assault by other and unspecified firearm discharge"]
        for i in result:
            self.assertIn(result[i],sample_COD)
        self.assertEqual(len(result),len(sample_COD)) 


if __name__ == "__main__":
    unittest.main()
