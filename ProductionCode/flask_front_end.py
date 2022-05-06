""" Written by Lazuli Kleinhans """

from flask import Flask, render_template, request
from command_line_interface import *

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
# states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado"]

def get_state_data(function_type, state):
    """
    Returns the data for the passed state using the passed function.

    Args:
        function_type: either 'dp' or 'lc', determines which function is used
        state: state that the user wants data about
    
    Returns:
        the data for the passed state using the passed function
    """
    if function_type == 'dp':
        return find_deaths_per([state, None, None, None], "data.csv")
    else:
        return find_leading_cause([state, None, None, None], "data.csv")

def return_render_template(function_type):
    """
    Returns the correct render template for the passed function.

    Args:
        function_type: either 'dp' or 'lc', determines which function is used
    
    Returns:
        the correct render template for the passed function
    """
    chosen_state = request.args['statechoice']
    state_data = get_state_data(function_type, chosen_state)
    return render_template(f'{function_type}.html', states=states, 
        chosen_state=chosen_state, state_data=state_data)

@app.route('/')
def homepage():
    """
    Returns the homepage render template.
    
    Returns:
        the homepage render template
    """
    return render_template('home.html')

@app.route('/dp/')
def deaths_per():
    """
    Returns the render template for deaths per, with no state chosen.
    
    Returns:
        the render template for deaths per, with no state chosen
    """
    return render_template('dp.html', states=states, chosen_state="")

@app.route('/dp/choosestate')
def deaths_per_choosestate():
    """
    Returns the render template for deaths per.

    Returns:
        the render template for deaths per
    """
    return return_render_template('dp')

@app.route('/lc/')
def leading_cause():
    """
    Returns the render template for leading cause, with no state chosen.
    
    Returns:
        the render template for leading cause, with no state chosen
    """
    return render_template('lc.html', states=states, chosen_state="")

@app.route('/lc/choosestate')
def leading_cause_choosestate():
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
    app.run()