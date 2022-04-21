# credit :)
# organization

"""
Written by Cole Kleinhans
"""

from sys import argv
from deaths_per import *

def print_usage_statement():
    exit("USAGE: command_line_interface.py [deaths_per | leading_cause] [-s state | -a age | -g gender | -c cause]")

def return_argument_value(argument, value):
    if argument == "-s" or argument == "--state":
        return {"state": value}
    if argument == "-a" or argument == "--age":
        return {"age": value}
    if argument == "-g" or argument == "--gender":
        return {"gender": value}
    if argument == "-c" or argument == "--cause":
        return {"cause": value}
    else:
        print_usage_statement()

def return_dictionary_of_arguments():
    argument_dictionary = {
        "state": None,
        "age": None,
        "gender": None,
        "cause": None
    }
    for i, argument in enumerate(argv):
        if "-" == argument[0]:
            argument_value = return_argument_value(argument, argv[i+1])
            argument_dictionary.update(argument_value)
    return argument_dictionary

def create_searchInfo(argument_dictionary):
    state = argument_dictionary["state"]
    age = argument_dictionary["age"]
    gender = argument_dictionary["gender"]
    cause = argument_dictionary["cause"]
    return SearchInfo(state, age, gender, cause)

def initialize_data():
    initialized_file = initializeFile("data.csv")
    return transformCSVDataToArray(initialized_file)

def find_deaths_per():
    data = initialize_data()
    argument_dictionary = return_dictionary_of_arguments()
    searchInfo = create_searchInfo(argument_dictionary)
    return deaths_per(searchInfo, data)

def find_leading_cause():
    argument_dictionary = return_dictionary_of_arguments()

def check_length_of_argv():
    if len(argv) < 2:
        print_usage_statement()

if __name__ == "__main__":
    check_length_of_argv()
    if argv[1] == "dp" or argv[1] == "deaths_per":
        deaths = find_deaths_per()
        print(deaths)
    elif argv[1] == "lc" or argv[1] == "leading_cause":
        find_leading_cause()
    else:
        print_usage_statement()

def find_possible_causes(input):
    data = initialize_data()
    for line in data:
        if input in data:
            pass