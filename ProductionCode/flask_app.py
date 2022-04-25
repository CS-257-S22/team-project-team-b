from flask import Flask
from leading_cause import *
from csv_reading import *
from deaths_per import *
from SearchInfo import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Welcome to the Predictor of Passing website! \n" +\
           "\n" +\
           "Usage: http://127.0.0.1:5000/[deaths_per | leading_cause]/[state | age | gender | cause]/[SEARCH CONTENT] \n" +\
           "\n" +\
           "-> DEFINITIONS: \n" +\
           "-> deaths_per (dp) : prints the number of deaths that are tagged with the passed search parameters.\n" +\
           "    -> POSSIBLE SEARCH PARAMETERS:\n" +\
           "    -> state : replace SEARCH CONTENT with the name of the state you want to search for. Case sensitive.\n" +\
           "    -> age : replace SEARCH CONTENT with the age you want to search for. Takes integers.\n" +\
           "    -> gender : replace SEARCH CONTENT with the gender you want to search for. Either M or F.\n" +\
           "    -> cause : replace SEARCH CONTENT with the name of the cause you want to search for. Has to be exactly the same as a cause in data.csv.\n" +\
           "\n" +\
           "-> leading_cause (lc): prints the leading causes of death that are tagged with the passed search parameters.\n" +\
           "    -> POSSIBLE SEARCH PARAMETERS:\n" +\
           "    -> state : replace SEARCH CONTENT with the name of the state you want to search for. Case sensitive.\n" +\
           "    -> age : replace SEARCH CONTENT with the age you want to search for. Takes integers.\n" +\
           "    -> gender : replace SEARCH CONTENT with the gender you want to search for. Either M or F.\n"

def initialize_data(file_name):
    """
    Initializes and returns the passed file transformed into an array.
    
    Returns:
        the passed file transformed into an array
    """
    initialized_file = read_CSV(file_name)
    return transform_CSV_data_to_array(initialized_file)

def create_search_info(argument, value):
    """
    Creates and returns a SearchInfo object that has
    all of the arguments the user passed loaded into it.

    Returns:
        a SearchInfo object that has all of the arguments
        the user passed loaded into it
    """
    argument_dictionary = return_dictionary_of_arguments(argument, value)
    state = argument_dictionary["state"]
    age = argument_dictionary["age"]
    gender = argument_dictionary["gender"]
    cause = argument_dictionary["cause"]
    return SearchInfo(state, age, gender, cause)
    
def return_dictionary_of_arguments(argument, value):
    """
    Returns a dictionary of the arguments passed.

    Returns:
        a dictionary of the arguments passed
    """
    argument_dictionary = {
        "state": None,
        "age": None,
        "gender": None,
        "cause": None
    }
    argument_dictionary.update({argument: value})
    return argument_dictionary

@app.route('/<selected_function>/<search_parameter_type>/<search_content>', strict_slashes=False)
def get_response(selected_function, search_parameter_type, search_content):
    """
    Takes the selected function and the search parameter and returns 
    the output of the selected function when run with that search parameter.
    
    Args:
        selected_function: a string of the function that the user wants to run -----------------------------------
        state: a string of the state that the user wants the information of
    Returns:
        the output of the selected function when run with that state as the parameter
    """
    search_info = create_search_info(search_parameter_type, search_content)
    return return_response(selected_function, search_info)

def return_response(selected_function, search_info):
    data = initialize_data("data.csv")
    if selected_function == "deaths_per" or selected_function == "dp":
        deaths = deaths_per(search_info, data)
        return str(deaths)
    elif selected_function == "leading_cause" or selected_function == "lc":
        leading_cause = return_leading_cause(data, search_info)
        return str(leading_cause)
    else:
        return page_not_found(1)

def return_argument_dictionary_entry(search_parameter_type, search_content):
    """
    Takes an argument and it's value, and then returns a dictionary entry
    with the name of the value and the value itself.

    Args:
        argument: a string that is the argument identifier
        value: the value that the user passed as that argument
    Returns:
        a dictionary entry with the name of the value and the value itself.
        if the search parameter type does not exist, returns None
    """
    if search_parameter_type == "state":
        return {"state": search_content}
    if search_parameter_type == "age":
        return {"age": search_content}
    if search_parameter_type == "gender":
        return {"gender": search_content}
    if search_parameter_type == "cause":
        return {"cause": search_content}
    else:
        return None


@app.route('/<selected_function>', strict_slashes=False)
def get_response_no_state(selected_function):
    """
    Takes the selected function and returns the output
    of the selected function when run with no parameters.

    Args:
        selected_function: a string of the function that the user wants to run
    Returns:
        the output of the selected function when run with no parameters
    """
    return return_response(selected_function, None)

@app.errorhandler(404)
def page_not_found(e):
    """
    Returns a string that has the usage format within it.

    Returns:
        a string that has the usage format within it
    """
    return "INCORRECT FORMAT. Usage: http://127.0.0.1:5000/[deaths_per | leading_cause]/[STATE]"

@app.errorhandler(500)
def python_bug(e):
    """
    Returns a string that has a general error.

    Returns:
        a string that has a general error
    """
    return "Sorry, my programmer is bad at their job. :)"

if __name__ == '__main__':
    """
    Runs the app.
    """
    app.run()