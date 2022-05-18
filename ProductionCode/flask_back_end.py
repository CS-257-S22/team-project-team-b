import psycopg2
import psqlConfig as config
from SearchArgs import SearchArgs
from deaths_per import *
from leading_cause import *

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

    def return_dictionary_of_arguments(self, search_arguments):
        argument_dictionary = {
            "state_choice": None,
            "age_choice": None,
            "gender_choice": None,
            "cause_choice": None
        }
        
        for key in search_arguments:
            value = search_arguments[key]
            if value != "None":
                argument_dictionary.update({key: value})
        return argument_dictionary

    def create_search_args(self):
        argument_dictionary = return_dictionary_of_arguments()
        state = argument_dictionary["state_choice"]
        age = argument_dictionary["age_choice"]
        gender = argument_dictionary["gender_choice"]
        cause = argument_dictionary["cause_choice"]
        return SearchArgs(state, age, gender, cause)

    def get_data(function_type, search_args):
        if function_type == 'dp':
            death_data = get_table()
            return get_deaths_per_arguments(death_data, search_args)
        elif function_type == 'lc':
            return return_leading_cause(death_data, search_args)
        else:
            #TODO create a better error message. Determine if this is necessary
            return "Error: function used does not exist"
    
    def get_query_result(self, query, query_inputs):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, query_inputs)
            result = cursor.fetchall()
        except Exception as e:
            print("Internal error: ", e)
            exit()
        return result
    
    def get_table(self):
        data_table = self.get_query_result("SELECT * FROM death_data;", ())
        return data_table

    def get_data_from_state(self, state):
        state_data = self.get_query_result("SELECT * FROM death_data WHERE state_name = %s;", (state,))
        return state_data

    def get_states(self):
        states = self.get_query_result("SELECT DISTINCT state_name FROM death_data;", ())
        return states

if __name__ == '__main__':
    my_source = DataSource()
    print(my_source.get_data_from_state('Wyoming'))

#referenced off of psycopg2 lab
#heavily referenced https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries