import csv

class searchInfo:
    def  __init__(self,state, age, gender, cause):
       self.state = state
       self.age = age
       self.gender = gender
       self.cause = cause

def initializeFile(file):
    file = open("Test Data CSV - Sheet1.csv")
    read_file = csv.reader(file)
    return read_file

def transformCSVDataToArray(file):
    data = []
    for datapoint in file:
        data.append(datapoint)
    return data

def deaths_per(search, data):
    total_deaths = 0
    for datapoint in data:
        total_deaths += getRelevantDeaths(datapoint,search)
    return total_deaths

def getRelevantDeaths(datapoint,search):
    deaths = 0
    if(dataFitsSearch(datapoint,search)):
        deaths = int(datapoint[5])
    return deaths

def dataFitsSearch(datapoint,search):
    return equalOrNone(datapoint[0],search.state) & equalOrNone(datapoint[1],search.age)\
        & equalOrNone(datapoint[2],search.gender) & equalOrNone(datapoint[3],search.cause)

def equalOrNone(compared, value):
    return (value == compared) | (value == None)

# referenced this article to work with csv's:
# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/