"""
Written By Kai R. Weiner, Lazuli Kleinhans
"""

import csv

def read_CSV(file):
    """
    Reads a CSV file.

    Args:
        file : the CSV file to be read
    Return:
        read_file : the read version of the CSV
    """
    file_to_read = open(file)
    read_file = csv.reader(file_to_read)
    return read_file

def transform_CSV_data_to_array(file):
    """
    Transforms a CSV file into a list.

    Args:
        file : the CSV file to be transformed into a list
    Return:
        data : the CSV file in list form
    """
    data = []
    for datapoint in file:
        data.append(datapoint)
    return data
