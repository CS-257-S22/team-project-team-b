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
    return is_equal_or_none(datapoint[0], search.state) & is_equal_or_none(datapoint[1], search.age)\
        & is_equal_or_none(datapoint[2], search.gender) & is_equal_or_none(datapoint[3], search.cause)

"""
Determines whether or not a value is equal to either the compared value or None.
@param compared : the variable value is being compared with
@param value : the variable being determined to be compared or None
@return : True if the value is equal to compared or equal to None, False otherwise
"""
def is_equal_or_none(compared, value):
    return (value == compared) | (value == None)

# referenced this article to work with csv's:
# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/