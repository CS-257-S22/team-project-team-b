"""
Written By Kai R. Weiner, Cole Kleinhans
"""

import csv

"""
Reads a CSV file.
@param file : the CSV file to be read
@return : the read version of the CSV
"""
def read_CSV(file):
    file_to_read = open(file)
    read_file = csv.reader(file_to_read)
    return read_file

"""
Transforms a CSV file into a list.
@param file : the CSV file to be transformed into a list
@return data : the CSV file in list form
"""
def transform_CSV_data_to_array(file):
    data = []
    for datapoint in file:
        data.append(datapoint)
    return data
