"""
Written By Kai R. Weiner, Cole Kleinhans
"""

"""
Returns the number of deaths for a search.
@param search : the search containing factors that the user wants the number of deaths for
@param data : the data being searched
@return : the number of deaths for people who fall under the search
"""
def deaths_per(search, data):
    """" 
    Search through entire database to return the total number of deaths that matches all of the search parameters.
    
    Arg: 
      search: a SearchInfo object with all the search info loaded into it
      data: a two dimentional array with data.csv loaded into it
    Return: 
       total_deaths: a total int with all the number of deaths listed that fit the search. 
    """
    total_deaths = 0
    for datapoint in data:
        total_deaths += get_relevant_deaths(datapoint, search)
    return total_deaths

"""
Returns the number of deaths for a subset of people that are relevant to a user's search.
@param search : the search containing factors that the user wants the number of deaths for
@return : The number of deaths for the subset of people or 0 if the subset is not relevant to the search
"""
def get_relevant_deaths(datapoint, search):
    """ Take in data and search param, return number of deaths if datapoint matches search param"""
    deaths = 0
    if fits_search(datapoint, search) and datapoint[5] != "under 10":
        deaths = int(datapoint[5])
    return deaths

"""
Determines if a subset of people is relevant to a user's search.
@param datapoint : the subset of people being examined
@param search : the search containing factors that the user wants the number of deaths for
@return : True if the subset of people fits the user's search, false if not
"""
def fits_search(datapoint,search):
<<<<<<< HEAD:deaths_per.py
    return is_equal_or_none(datapoint[0], search.state) & is_equal_or_none(datapoint[1], search.age)\
        & is_equal_or_none(datapoint[2], search.gender) & is_equal_or_none(datapoint[3], search.cause)

"""
Determines whether or not a value is equal to either the compared value or None.
@param compared : the variable value is being compared with
@param value : the variable being determined to be compared or None
@return : True if the value is equal to compared or equal to None, False otherwise
"""
def is_equal_or_none(compared, value):
=======
    """ Take in datapoint, return booleans about whether datapoint matches search param or specifc search is not needed"""
    return equal_or_none(datapoint[0], search.state) & equal_or_none(datapoint[1], search.age)\
        & equal_or_none(datapoint[2], search.gender) & equal_or_none(datapoint[3], search.cause)

def equal_or_none(compared, value):
    """Take in two varibles, returns True if the value match compared or None"""
>>>>>>> 246ade12cc8db06ff8a79d6bf93969c267ad6017:ProductionCode/deaths_per.py
    return (value == compared) | (value == None)

# referenced this article to work with csv's:
# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
