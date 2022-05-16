""" Written by Lazuli Kleinhans """

from flask import Flask, render_template, request
from search_args import SearchArgs
from deaths_per import *
from leading_cause import *
from csv_reading import *
import random

app = Flask(__name__)

# list of states copied from here: https://python-forum.io/thread-3105.html
states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
    "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
    "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
    "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
    "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
    "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
    "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
    "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

#list of fun facts to use on welcome and home pages
facts = ["The leading cause of death for infants younger than 1 is extreme immaturity with 13,660 deaths", 
    "For people 100 and up, the leading cause of death is dementia with 16,661 deaths.", "The most common cause of death for males is atherosclerotic heart disease, with 463,155 deaths.", 
    "The age group with the most deaths is 88 years old with 399,487 deaths.", "The most common cause of death for females is alzheimer's disease with 406,313 deaths"]

causes_list = []

def load_causes_list():
    with open("causes_list.txt") as f:
        for line in f:
            causes_list.append(line[:-1])

def get_data(function_type, search_args):
    """
    Returns the data for the passed state using the passed function.

    Args:
        function_type: either 'dp' or 'lc', determines which function is used
        search_args: SearchArgs object with the search arguments
    
    Returns:
        the data for the search_args arguments using the passed function
    """
    CSV_data = get_CSV_data_as_list("data.csv")
    if function_type == 'dp':
        return deaths_per(CSV_data, search_args)
    else:
        return return_leading_cause(CSV_data, search_args)

def return_dictionary_of_arguments():
    """
    Returns a dictionary of the arguments in request.args.

    Returns:
        a dictionary of the arguments in request.args
    """
    argument_dictionary = {
        "state_choice": None,
        "age_choice": None,
        "gender_choice": None,
        "cause_choice": None
    }
    
    for key in request.args:
        value = request.args[key]
        if value != "None":
            argument_dictionary.update({key: value})
    return argument_dictionary

def create_search_args():
    """
    Creates and returns a SearchArgs object that has
    all of the arguments the user passed loaded into it.

    Returns:
        a SearchArgs object that has all of the arguments
        the user passed loaded into it
    """
    argument_dictionary = return_dictionary_of_arguments()
    state = argument_dictionary["state_choice"]
    age = argument_dictionary["age_choice"]
    gender = argument_dictionary["gender_choice"]
    cause = argument_dictionary["cause_choice"]
    return SearchArgs(state, age, gender, cause)

def return_render_template(function_type):
    """
    Creates a SearchArgs object, gets the correct data for the search arguments and
    returns the correct render template for the passed function.

    Args:
        function_type: either 'dp' or 'lc', determines which function is used
    
    Returns:
        the correct render template for the passed function
    """
    # causes_list = return_causes_list()
    search_args = create_search_args()
    returned_data = get_data(function_type, search_args)
    return render_template(f'{function_type}.html', states=states, 
        search_args=search_args, data=returned_data, causes=causes_list)

def get_fact():
    """
    Retrieve fact from facts at given random int
    
    Returns: 
        a string from facts 
    """ 
    index = random.randint(0,4)
    random_fact = facts[index]
    return random_fact

@app.route('/')
def welcomepage():
    """
    Returns the welcome render template.
    
    Returns:
        the welcome render template
    """
    return render_template('welcome.html',fact = get_fact())

@app.route('/home')
def homepage():
    """
    Returns the homepage render template.
    
    Returns:
        the homepage render template
    """
    return render_template("home.html",fact = get_fact() )

@app.route('/dp/')
def deaths_per_template():
    """
    Returns the render template for deaths per with no search_args.
    
    Returns:
        the render template for deaths per with no search_args
    """
    return render_template('dp.html', states=states, search_args=None, causes=causes_list)

@app.route('/dp/choose_arguments')
def deaths_per_template_arguments():
    """
    Returns the render template for deaths per.

    Returns:
        the render template for deaths per
    """
    return return_render_template('dp')

@app.route('/lc/')
def leading_cause_template():
    """
    Returns the render template for leading cause, with no search_args.
    
    Returns:
        the render template for leading cause, with no search_args
    """
    return render_template('lc.html', states=states, search_args=None)

@app.route('/lc/choose_arguments')
def leading_cause_template_arguments():
    """
    Returns the render template for leading cause.

    Returns:
        the render template for leading cause
    """
    return return_render_template('lc')

@app.errorhandler(404)
def page_not_found(e):
    """
    Returns the render template for a 404 error.

    Args:
        e: error that was thrown

    Returns:
        the render template for a 404 error
    """
    return render_template('404.html', error=e)

@app.errorhandler(500)
def python_bug(e):
    """
    Returns a string that has a general error.

    Returns:
        a string that has a general error
    """
    return "Sorry, my programmer is bad at their job. :)"

if __name__ == '__main__':
    """ Runs the app. """
    load_causes_list()
    app.run()
