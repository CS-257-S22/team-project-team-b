"""
Written By Kai R. Weiner, Cole Kleinhans
"""

import csv

def read_CSV(file):
    file_to_read = open(file)
    read_file = csv.reader(file_to_read)
    return read_file

def transform_CSV_data_to_array(file):
    data = []
    for datapoint in file:
        data.append(datapoint)
    return data