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
           "Usage: http://127.0.0.1:5000/[deaths_per | leading_cause]/(SEARCH CONTENT) \n" +\
           "\n" +\
           "(SEARCH CONTENT) takes the form:" +\
           "\n" +\
           "(-s STATE -a AGE -g GENDER -c CAUSE)" +\
           "\n" +\
           "or"+\
           "\n" +\
           "(-state STATE -age AGE -gender GENDER -cause CAUSE)" +\
           "\n" +\
           "Note: Make sure to keep your search terms contained in parenthesis." +\
           "\n" +\
           "-> DEFINITIONS: \n" +\
           "-> deaths_per (dp) : prints the number of deaths that are tagged with the passed search parameters.\n" +\
           "    -> POSSIBLE SEARCH PARAMETERS:\n" +\
           "    -> state : replace STATE with the name of the state you want to search for. Case sensitive.\n" +\
           "    -> age : replace AGE with the age you want to search for. Takes integers.\n" +\
           "    -> gender : replace GENDER with the gender you want to search for. Either M or F.\n" +\
           "    -> cause : replace CAUSE with the name of the cause you want to search for. Has to be exactly the same as a cause in data.csv.\n" +\
           "\n" +\
           "-> leading_cause (lc): prints the leading causes of death that are tagged with the passed search parameters.\n" +\
           "    -> POSSIBLE SEARCH PARAMETERS:\n" +\
           "    -> state : replace STATE with the name of the state you want to search for. Case sensitive.\n" +\
           "    -> age : replace AGE with the age you want to search for. Takes integers.\n" +\
           "    -> gender : replace GENDER with the gender you want to search for. Either M or F.\n"

@app.route('/<selected_function>/<search>', strict_slashes=False)
def get_response(selected_function, search):
    """
    Takes the selected function and the search parameter and returns 
    the output of the selected function when run with that search parameter.
    
    Args:
        selected_function: a string of the function that the user wants to run
        search: a search the user wants the death information about
    Returns:
        the output of the selected function when run with that state as the parameter
    """
    search = create_search_info(search)

    if selected_function == "deaths_per" or selected_function == "dp":
        return print_deaths_per_search(search)
    elif selected_function == "leading_cause" or selected_function == "lc":
        return print_leading_cause(search)
    else:
        return page_not_found(1)

def create_search_info(search_terms):
    """
    Creates and returns a SearchInfo object that has all of the arguments the user passed loaded into it.

    Returns:
        a SearchInfo object that has all of the arguments
        the user passed loaded into it
    """
    search_terms = remove_parenthesis(search_terms)
    search_terms = fix_string_spaces(search_terms)
    search = convert_string_to_search(search_terms)
    return search

def remove_parenthesis(string):
    """
    Removes the parenthesis from a string

    Args:
        string : the string to remove the parenthesis of
    Returns:
        the given string without parenthesis
    """
    return string[1:len(string)-1]

def fix_string_spaces(string):
    """
    Splits a string into different terms by '%20'
    
    Args:
        string : the string being split
    Returns:
        a split version of the given string
    """
    string = string.split("%20")
    string = string[0].split(" ")
    return string

def convert_string_to_search(string):
    """
    Converts a string with search terms into the SearchInfo class.

    Args:
        string : the string with search term
    Returns:
        a SearchInfo object with the search terms provided by the initial string
    """
    search = SearchInfo(None, None, None, None)
    for word_index, word in enumerate(string):
        if word[0] == "-":
            search = update_argument_value(word[1:], string[word_index + 1:], search)
    return search

def update_argument_value(term, new_value, search):
    """
    Updates a SearchInfo object based on a given term and new value for that term.

    Args:
        term : the term whose value is being updated
        new_value : the new value for the term
        search : the search containing factors that the user wants the death information for
    Returns:
        the updated search containing factors that the user wants the death information for
    """
    if(term == "s" or term == "state"):
        search.set_state(new_value[0])
    if(term == "a" or term == "age"):
        search.set_age(new_value[0])
    if(term == "g" or term == "gender"):
        search.set_gender(new_value[0])
    if(term == "c" or term == "cause"):
        new_value = fix_cause(new_value)
        search.set_cause(new_value)
    return search

def fix_cause(string):
    """
    Puts a list of words for cause of death into string form.

    Args:
        string : the string containing cause of death and starting with cause of death
    Returns:
        the cause of death in string form
    """
    cause = []
    for i in string:
        if(i == "-s") | (i == "-a") | (i == "-g") | (i == "-c") | (i == "-state") | (i == "-age") | (i == "-gender") | (i == "-cause"):
            return " ".join(cause)
        cause.append(i)
    return " ".join(cause)

def print_deaths_per_search(search):
    """
    Displays a string containing a search's terms and the number of deaths per the search.

    Args:
        search : the search containing factors that the user wants the number of deaths for
    Returns:
        a string containing a search's terms and the number of deaths per the search.
    """
    string = "The number of people who died under the category:"
    string = add_search_term_to_string(string, "state", search)
    string = add_search_term_to_string(string, "age", search)
    string = add_search_term_to_string(string, "gender", search)
    string = add_search_term_to_string(string, "cause", search)
    string += " is: "+str(deaths_per(deaths_data, search))+"."
    return string

def print_leading_cause(search):
    """
    Displays a string containing a search's terms and the leading causes of death for the search.

    Args:
        search : the search containing factors that the user wants the leading causes of death for
    Returns:
        a string containing a search's terms and the leading causes of death per the search.
    """
    string = "The number of people who died under the category:"
    string = add_search_term_to_string(string, "state", search)
    string = add_search_term_to_string(string, "age", search)
    string = add_search_term_to_string(string, "gender", search)
    string += " is: "+str(return_leading_cause(deaths_data, search))+"."
    return string

def add_search_term_to_string(string, term, search):
    """
    Adds a specified term of a search to a string.

    Args:
        string : the string terms are being added to
        term : the term the user wants from the search
        search : the search containing factors that the user wants the death information for
    Returns:
        the provided string with terms added
    """
    string += " "+term+" = "
    if(search.get_term_from_string(term) != None):
        string += str(search.get_term_from_string(term))+","
    else:
        string += "all,"
    return string

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
    initialized_file = read_CSV("Test Data CSV - Sheet1.csv")
    deaths_data = transform_CSV_data_to_array(initialized_file)
    app.run()