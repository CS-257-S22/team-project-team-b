import psycopg2
from search_args import SearchArgs
from deaths_per import *
from leading_cause import *

class databaseCursor:
    database_connection = None
    database_cursor = None

    def __init__(self, database_name, database_user):
        self.database_connection = psycopg2.connect("dbname="+database_name+" user="+database_user)
    
    def open_connection_and_cursor(self):
        self.database_cursor = self.database_connection.cursor()
    
    def close_connection_and_cursor(self):
        self.database_cursor.close()
        self.database_connection.close()
    
    def execute_command(self, command):
        self.database_cursor.execute(command)

cursor = databaseCursor("teamb", "postgress")
path_to_csv_data = 'data_smaller.csv'

def initialize_data_table():
    cursor.open_connection_and_cursor()

    #TODO currently age discludes those over 100 and deaths disculdes those under 10, need to fix this
    cursor.execute_command("CREATE TABLE deaths_data (d_state text, d_age int, d_gender text, d_cause text, d_deaths int);")
    cursor.execute_command("\copy deaths_data FROM "+path_to_csv_data+" DELIMITER ',' CSV;")

    cursor.close_connection_and_cursor()

# cursor.execute("SELECT * FROM deaths_data;")

def return_dictionary_of_arguments(search_arguments):
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

def create_search_args():
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

def get_table():
    return cursor.execute_command()

def get_states():
    return cursor.execute_command()



#heavily referenced https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries