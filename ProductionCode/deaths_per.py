"""
Written By Kai R. Weiner, Cole Kleinhans
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

def get_relevant_deaths(datapoint, search):
    """ Take in data and search param, return number of deaths if datapoint matches search param"""
    deaths = 0
    if fits_search(datapoint, search) and datapoint[5] != "under 10":
        deaths = int(datapoint[5])
    return deaths

def fits_search(datapoint,search):
    """ Take in datapoint, return booleans about whether datapoint matches search param or specifc search is not needed"""
    return equal_or_none(datapoint[0], search.state) & equal_or_none(datapoint[1], search.age)\
        & equal_or_none(datapoint[2], search.gender) & equal_or_none(datapoint[3], search.cause)

def equal_or_none(compared, value):
    """Take in two varibles, returns True if the value match compared or None"""
    return (value == compared) | (value == None)

# referenced this article to work with csv's:
# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
