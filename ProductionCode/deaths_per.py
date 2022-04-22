"""
Written By Kai R. Weiner, Cole Kleinhans
"""

def deaths_per(search, data):
    total_deaths = 0
    for datapoint in data:
        total_deaths += get_relevant_deaths(datapoint, search)
    return total_deaths

def get_relevant_deaths(datapoint, search):
    deaths = 0
    if fits_search(datapoint, search) and datapoint[5] != "under 10":
        deaths = int(datapoint[5])
    return deaths

def fits_search(datapoint,search):
    return equal_or_none(datapoint[0], search.state) & equal_or_none(datapoint[1], search.age)\
        & equal_or_none(datapoint[2], search.gender) & equal_or_none(datapoint[3], search.cause)

def equal_or_none(compared, value):
    return (value == compared) | (value == None)

# referenced this article to work with csv's:
# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/