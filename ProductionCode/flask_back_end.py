import psycopg2
import psqlConfig as config
from SearchArgs import SearchArgs
from deaths_per import *
from leading_cause import *
import random

class DataSource:

    def __init__(self):
        self.connection = self.connect()
    
    def connect(self):
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection
    
    def get_query_result(self, query, query_inputs):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, query_inputs)
            result = cursor.fetchall()
        except Exception as e:
            print("Internal error: ", e)
            exit()
        return result

class SiteData:

    def __init__(self):
        self.source = DataSource()
        self.states = self.return_list_of_states()
        self.causes = self.return_list_of_causes()
        self.facts = ["The leading cause of death for infants younger than 1 is extreme immaturity with 13,660 deaths", 
        "For people 100 and up, the leading cause of death is dementia with 16,661 deaths.", "The most common cause of death for males is atherosclerotic heart disease, with 463,155 deaths.", 
        "The age group with the most deaths is 88 years old with 399,487 deaths.", "The most common cause of death for females is alzheimer's disease with 406,313 deaths"]
    
    def return_list_of_states(self):
        states = self.retrieve_states_from_database()
        states.sort()
        return states
    
    #TODO find out if all this self.source.get_query_result is feature envy
    def retrieve_states_from_database(self):
        states = self.source.get_query_result("SELECT DISTINCT state_name FROM death_data;", ())
        reformatted_states = self.reformat_list(states)
        return reformatted_states
    
    def get_states(self):
        return self.states

    def return_list_of_causes(self):
        causes = self.retrieve_causes_from_database()
        causes.sort()
        return causes
    
    def retrieve_causes_from_database(self):
        causes = self.source.get_query_result("SELECT DISTINCT cause FROM death_data;", ())
        reformatted_causes = self.reformat_list(causes)
        return reformatted_causes
    
    def get_causes(self):
        return self.causes
    
    def get_fact(self):
        """
        Retrieve fact from facts at given random int
        
        Returns:
            a string from facts 
        """
        index = random.randint(0,4)
        random_fact = self.facts[index]
        return random_fact
    
    def return_arguments_as_search(self, search_arguments):
        search = SearchArgs(None, None, None, None)

        for key in search_arguments:
            value = search_arguments[key]
            if value != "None":
                search.set_term_from_string(key, value)
        
        return search
    

    def get_search_result_from_function(self, function_type, search_args):
        """
        Returns the search result for the passed arguments and function.

        Args:
            function_type: either 'dp' or 'lc', determines which function is used
            search_args: SearchArgs object with the search arguments
        
        Returns:
            the data for the search_args arguments using the passed function
        """

        new_search_args = self.return_arguments_as_search(search_args)
        death_data = self.retrieve_table_from_database()

        if function_type == 'dp':
            return get_deaths_per_arguments(death_data, new_search_args)
        elif function_type == 'lc':
            return return_leading_cause(death_data, new_search_args)
        else:
            #TODO create a better error message. Determine if this is necessary
            return "Error: function used does not exist"
    
    def retrieve_table_from_database(self):
        data_table = self.source.get_query_result("SELECT * FROM death_data;", ())
        return data_table

    # def get_data_from_state(self, state):
    #     state_data = self.source.get_query_result("SELECT * FROM death_data WHERE state_name = %s;", (state,))
    #     return state_data
    
    def reformat_list(self, list):
        new_list = []
        for item in list:
            new_list.append(item[0])
        return new_list

if __name__ == '__main__':
    my_source = SiteData()
    print(my_source.get_causes())

#referenced off of psycopg2 lab
#heavily referenced https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries
