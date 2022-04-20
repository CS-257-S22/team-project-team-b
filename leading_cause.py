"""
Written by Tin Nguyen
"""
def find_leading_cause_based_on_state(input_state):
  """ Do I need to write a caption? I do not know what is needed that is not explained by the title """
  data_file = open("data.csv","r")
  data = []
  for datapoint in data_file:
    if datapoint.split(",")[0] == input_state:
      state = datapoint.split(",")[0] 
      cause_of_death = datapoint.split(",")[3]
      num_of_death =  datapoint.split(",")[5]
      instance = [state,cause_of_death,num_of_death]
      print(instance)
      data.append(instance)
  data_file.close()
  return data

def find_leading_cause_based_on_age(input_age): 
  data_file = open("data.csv","r")
  data = []
  for datapoint in data_file:
    if datapoint.split(",")[1] == input_age:
      age = datapoint.split(",")[1] 
      cause_of_death = datapoint.split(",")[3]
      num_of_death =  datapoint.split(",")[5]
      instance = [age,cause_of_death,num_of_death]
      data.append(instance)
  data_file.close()
  return data

  
def find_leading_cause_based_on_gender(input_gender): 
  data_file = open("data.csv","r")
  data = []
  for datapoint in data_file:
    if datapoint.split(",")[2] == input_gender:
      gender = datapoint.split(",")[2] 
      cause_of_death = datapoint.split(",")[3]
      num_of_death =  datapoint.split(",")[5]
      instance = [gender,cause_of_death,num_of_death]
      data.append(instance)
  data_file.close()
  return data


def find_leading_cause_based_on_ageState(input_state,input_age): 
  data_file = open("data.csv","r")
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
  data_file.close()
  return data

def find_leading_cause_based_on_stateGender(input_state,input_gender):
  data_file = open("data.csv","r")
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
  data_file.close()
  return data

def find_leading_cause_based_on_ageGender(input_age,input_gender): 
  data_file = open("data.csv","r")
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
  data_file.close()
  return data
  
def find_leading_cause_based_on_stateAgeGender(input_state,input_age,input_gender): 
  data_file = open("data.csv","r")
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
  data_file.close()
  return data


def main():
   find_leading_cause_based_on_stateAgeGender('"New York"',"49",'"F"')

if __name__ == "__main__": 
   main() 
