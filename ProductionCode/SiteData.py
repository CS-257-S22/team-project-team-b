from flask_back_end import *
import random

class SiteData:

    def __init__(self):
        self.source = DataSource()
        self.states = self.return_states_list()
        self.causes = self.return_causes_list()

        #list of fun facts to use on welcome and home pages
        self.facts = ["The leading cause of death for infants younger than 1 is extreme immaturity with 13,660 deaths", 
        "For people 100 and up, the leading cause of death is dementia with 16,661 deaths.", "The most common cause of death for males is atherosclerotic heart disease, with 463,155 deaths.", 
        "The age group with the most deaths is 88 years old with 399,487 deaths.", "The most common cause of death for females is alzheimer's disease with 406,313 deaths"]
    
    def return_states_list(self):
        states = self.source.get_states()
        states.sort()
        return states

    def return_causes_list(self):
        causes = self.source.get_causes()
        causes.sort()
        return causes

    def return_render_template(self, function_type, requested_args):
        """
        Creates a SearchArgs object, gets the correct data for the search arguments and
        returns the correct render template for the passed function.

        Args:
            function_type: either 'dp' or 'lc', determines which function is used
        
        Returns:
            the correct render template for the passed function
        """
        search_args = self.source.create_search_args(requested_args)
        returned_data = self.source.get_data(function_type, search_args)
        return render_template(f'{function_type}.html', states = self.states, 
            search_args = search_args, data = returned_data, causes = self.causes)

    def get_fact(self):
        """
        Retrieve fact from facts at given random int
        
        Returns:
            a string from facts 
        """
        index = random.randint(0,4)
        random_fact = self.facts[index]
        return random_fact