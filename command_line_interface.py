# credit :)
# organization

"""
Written by Cole Kleinhans
"""

from sys import argv
from deaths_per import *
from SearchInfo import *
from csv_reading import *
from leading_cause import *

def print_usage_statement():
    exit("\nUSAGE: command_line_interface.py [deaths_per | leading_cause | --help] [--state STATE] [--age AGE] [--gender GENDER] [--cause CAUSE]\n")

def print_help_statement():
    exit("\nUSAGE: command_line_interface.py [deaths_per | leading_cause | --help] [--state STATE] [--age AGE] [--gender GENDER] [--cause CAUSE]\n" +
         "\n" +
         "deaths_per (dp) : prints the number of deaths that are tagged with the passed search parameters.\n" +
         "    POSSIBLE SEARCH PARAMETERS:\n" +
         "    --state (-s) STATE : replace STATE with the name of the state you want to search for. Case sensitive.\n" +
         "    --age (-a) AGE : replace AGE with the age you want to search for. Takes integers.\n" +
         "    --gender (-g) GENDER : replace GENDER with the gender you want to search for. Either M or F.\n" +
         "    --cause (-c) CAUSE : replace CAUSE with the name of the cause you want to search for. Has to be exactly the same as a cause in data.csv.\n" +
         "\n" +
         "leading_cause (lc): prints the leading causes of death that are tagged with the passed search parameters.\n" +
         "    POSSIBLE SEARCH PARAMETERS:\n" +
         "    --state (-s) STATE : replace STATE with the name of the state you want to search for. Case sensitive.\n" +
         "    --age (-a) AGE : replace AGE with the age you want to search for. Takes integers.\n" +
         "    --gender (-g) GENDER : replace GENDER with the gender you want to search for. Either M or F.\n" +
         "\n" +
         "--help (-h): prints this help information.\n")

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

def create_search_info():
    argument_dictionary = return_dictionary_of_arguments()
    state = argument_dictionary["state"]
    age = argument_dictionary["age"]
    gender = argument_dictionary["gender"]
    cause = argument_dictionary["cause"]
    return SearchInfo(state, age, gender, cause)

def initialize_data():
    initialized_file = read_CSV("data.csv")
    return transform_CSV_data_to_array(initialized_file)

def find_deaths_per():
    data = initialize_data()
    search_info = create_search_info()
    return deaths_per(search_info, data)

def find_leading_cause():
    data = initialize_data()
    search_info = create_search_info()
    return return_leading_cause(data, search_info)

def check_length_of_argv():
    if len(argv) < 2:
        print_usage_statement()

if __name__ == "__main__":
    check_length_of_argv()
    if argv[1] == "deaths_per" or argv[1] == "dp":
        deaths = find_deaths_per()
        print(deaths)
    elif argv[1] == "leading_cause" or argv[1] == "lc":
        leading_cause = find_leading_cause()
        print(leading_cause)
    elif argv[1] == "--help" or argv[1] == "-h":
        print_help_statement()
    else:
        print_usage_statement()