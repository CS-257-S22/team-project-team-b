"""
Written by Tin Nguyen
"""

def initialize_dataset(input_state,input_age,input_gender): 
  """Function opens data set and calls function that determinds what the user input"""
  data_file = open("data.csv","r")
  initialize_search(data_file,input_state,input_age,input_gender)
  data_file.close()

def initialize_search(data_file, state, age,gender): 
  "Function determinds what varibles the the user input to determind how the data base should be searched"
  if state != "" and age != "" and gender != "": 
    find_leading_cause_based_on_stateAgeGender(data_file, state,age,gender) 
  elif age != "" and state != "": 
    find_leading_cause_based_on_stateAge(data_file, state,age) 
  elif age != "" and gender !="": 
    find_leading_cause_based_on_ageGender(data_file,age,gender)
  elif state != "" and gender != "": 
    find_leading_cause_based_on_stateGender(data_file,state,gender)
  elif age != "": 
    find_leading_cause_based_on_age(data_file, age) 
  elif state != "":
    find_leading_cause_based_on_state(data_file,state)
  elif gender != "": 
    find_leading_cause_based_on_gender(data_file,gender)


def find_leading_cause_based_on_state(data_file, input_state):
  """ Search  database for a specific state and create array for each instance """
  data = []
  for datapoint in data_file:
    if datapoint.split(",")[0] == input_state:
      state = datapoint.split(",")[0] 
      cause_of_death = datapoint.split(",")[3]
      num_of_death =  datapoint.split(",")[5]
      instance = [state,cause_of_death,num_of_death]
      print(instance)
      data.append(instance)
  return data

def find_leading_cause_based_on_age(data_file,input_age): 
  """ Search  database for a specific age and create array for each instance """
  data = []
  for datapoint in data_file:
    if datapoint.split(",")[1] == input_age:
      age = datapoint.split(",")[1] 
      cause_of_death = datapoint.split(",")[3]
      num_of_death =  datapoint.split(",")[5]
      instance = [age,cause_of_death,num_of_death]
      data.append(instance)
  return data

  
def find_leading_cause_based_on_gender(data_file,input_gender): 
  """ Search  database for a specific gender and create array for each instance """
  data = []
  for datapoint in data_file:
    if datapoint.split(",")[2] == input_gender:
      gender = datapoint.split(",")[2] 
      cause_of_death = datapoint.split(",")[3]
      num_of_death =  datapoint.split(",")[5]
      instance = [gender,cause_of_death,num_of_death]
      data.append(instance)
  return data


def find_leading_cause_based_on_stateAge(data_file, input_state,input_age):
  """ Search  database for a specific state and age and create array for each instance """
  data = []
  for datapoint in data_file:
    """should I put the varibles out here or in the if loop"""
    if (datapoint.split(",")[0] == input_state) and (datapoint.split(",")[1] == input_age):
      age = datapoint.split(",")[1] 
      state = datapoint.split(",")[0]
      cause_of_death = datapoint.split(",")[3]
      num_of_death =  datapoint.split(",")[5]
      instance = [state, age,cause_of_death,num_of_death]
      data.append(instance) 
  return data

def find_leading_cause_based_on_stateGender(data_file,input_state,input_gender):
  """ Search  database for a specific state and gender and create array for each instance """
  data = []
  for datapoint in data_file:
    """should I put the varibles out here or in the if loop"""
    if (datapoint.split(",")[0] == input_state) and (datapoint.split(",")[2] == input_gender):
      gender = datapoint.split(",")[2] 
      state = datapoint.split(",")[0]
      cause_of_death = datapoint.split(",")[3]
      num_of_death =  datapoint.split(",")[5]
      instance = [state,gender,cause_of_death,num_of_death]
      data.append(instance) 
  return data

def find_leading_cause_based_on_ageGender(data_file, input_age,input_gender): 
    """ Search  database for a specific age and gender and create array for each instance """
  data = []
  for datapoint in data_file:
    """should I put the varibles out here or in the if loop"""
    if (datapoint.split(",")[1] == input_age) and (datapoint.split(",")[2] == input_gender):
      gender = datapoint.split(",")[2] 
      age = datapoint.split(",")[1]
      cause_of_death = datapoint.split(",")[3]
      num_of_death =  datapoint.split(",")[5]
      instance = [age,gender,cause_of_death,num_of_death]
      data.append(instance) 
      print(instance)
  return data
  
def find_leading_cause_based_on_stateAgeGender(data_file,input_state,input_age,input_gender):
    """ Search  database for a specific state, age and gender and create array for each instance """
  data = []
  for datapoint in data_file:
    """should I put the varibles out here or in the if loop"""
    if (datapoint.split(",")[0] == input_state) and (datapoint.split(",")[1] == input_age) and (datapoint.split(",")[2] == input_gender):
      state = datapoint.split(",")[0]
      gender = datapoint.split(",")[2] 
      age = datapoint.split(",")[1]
      cause_of_death = datapoint.split(",")[3]
      num_of_death =  datapoint.split(",")[5]
      instance = [state,age,gender,cause_of_death,num_of_death]
      data.append(instance)
      print(instance)
  return data
