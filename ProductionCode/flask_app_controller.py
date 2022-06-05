""" Written by Lazuli Kleinhans """

from flask import Flask, render_template, request
from flask_app_model import *
from death_predictor import Prediction

app = Flask(__name__)
states = return_list_of_states()
causes = return_list_of_causes()

def return_render_template(function_type):
    """
    Retrieves the search arguments and requested data for the requested function,
    returns the correct render template with the this data

    Args:
        function_type: either 'dp' or 'lc', determines which function is used
        
    Returns:
        the correct render template for the passed function
    """

    returned_data = get_search_result_from_function(function_type, request.args)

    return render_template(f'{function_type}.html', states = states, causes = causes, data_boolean = True, data_points = returned_data)

@app.route('/')
def welcomepage():
    """
    Returns the welcome render template.
    
    Returns:
        the welcome render template
    """
    return render_template('welcome.html', fact = get_fact())

@app.route('/home')
def homepage():
    """
    Returns the homepage render template.
    
    Returns:
        the homepage render template
    """
    return render_template("home.html", fact = get_fact() )

@app.route('/wwid/')
def get_prediction():
    """
    Returns the render template for deaths per with no search_args.
    
    Returns:
        the render template for deaths per with no search_args
    """
    return render_template('wwid.html', states = states, data_boolean = False, data_points = Prediction(None,15,'','',''))

@app.route('/wwid/choose_arguments')
def get_prediction_from_arguments_template_arguments():
    return return_render_template('wwid')

@app.route('/dp/')
def get_deaths_per_arguments_template():
    """
    Returns the render template for deaths per with no search_args.
    
    Returns:
        the render template for deaths per with no search_args
    """
    return render_template('dp.html', states = states, data_boolean = False, causes = causes, data_points = DeathsPerSearchResult(SearchArgs(None, None, None, None), 0))

@app.route('/dp/choose_arguments')
def get_deaths_per_arguments_template_arguments():
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
    return render_template('lc.html', states = states, data_boolean = False, data_points = LeadingCauseSearchResult(SearchArgs(None, None, None, None), "None", 0))

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
    return render_template('404.html', error = e)

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
    #app.run()
    app.run(port = 5130, host = "0.0.0.0")
    #app.run(port = 5120, host = "0.0.0.0")
