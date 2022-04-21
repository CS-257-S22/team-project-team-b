"""
Written by Tin Nguyen, Cole Kleinhans & Kai R. Weiner
"""

def fits_search(datapoint,search):
    return equal_or_none(datapoint[0], search.state) & equal_or_none(datapoint[1], search.age)\
        & equal_or_none(datapoint[2], search.gender)

def equal_or_none(compared, value):
    return (value == compared) | (value == None)

def return_data_entry(datapoint, data_dictionary):
    if datapoint[3] in data_dictionary.keys():
        new_entry = {datapoint[3]: int(data_dictionary[datapoint[3]]) + int(datapoint[5])}
    else:
        new_entry = {datapoint[3]: int(datapoint[5])}
    return new_entry

def return_cause_of_death_dictionary(data_file, search_info):
    """
    Search database for the passed search info and returns a dictionary
    with all the matching causes and the number of deaths per each one.
    """
    data_dictionary = {}
    for datapoint in data_file:
        if fits_search(datapoint, search_info) and datapoint[3] != "Miscellaneous":
            new_entry = return_data_entry(datapoint, data_dictionary)
            data_dictionary.update(new_entry)
    return data_dictionary

def find_most_common_cause_of_death(data_dictionary):
    max_number_of_deaths = 0
    leading_cause_of_death = ""
    for key in data_dictionary:
        if data_dictionary[key] > max_number_of_deaths:
            max_number_of_deaths = data_dictionary[key]
            leading_cause_of_death = key
    return [leading_cause_of_death, max_number_of_deaths]

def return_leading_cause(data_file, search_info):
    data_dictionary = return_cause_of_death_dictionary(data_file, search_info)
    leading_cause = find_most_common_cause_of_death(data_dictionary)
    return leading_cause