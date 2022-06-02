import psycopg2
import psqlConfig as config
from SearchArgs import SearchArgs
import random
from death_predictor import deaths_predictor

"""
Written by Kai R. Weiner
"""

"""
Stores information about the result of a search for the amount of deaths given a set of search terms.
"""
class DeathsPerSearchResult:

    def __init__(self, search, deaths):
        """
        Sets up an instance of DeathsPerSearchResult

        Args:
            search : an object containing the terms the amount of deaths are being searched for
            deaths : the amount of deaths returned from the search
        Return:
            A DeathsPerSearchResult object
        """
        search = search.return_corrected_search_args_none_values()
        self.state = self.return_corrected_state_name(search.get_state())
        self.age = search.get_age()
        self.gender = self.return_gender_as_string(search.get_gender())
        self.cause = search.get_cause()
        self.deaths = self.return_deaths_as_int(deaths)
    
    def return_corrected_state_name(self, state):
        """
        Returns a corrected version of the state

        Args:
            state : the state being corrected
        Return:
            A corrected version of the state
        """
        if (state == "all state_names"):
            return "all states"
        return state
    
    def return_gender_as_string(self, gender):
        """
        Returns the gender as a full string

        Args:
            gender : the gender being returned as a string
        Return:
            The gender as a full string corresponding to its identity
        """
        if gender == "M":
            return "males"
        elif gender == "F":
            return "females"
        else:
            return gender
    
    def return_deaths_as_int(self, deaths):
        """
        Returns deaths as an integer

        Args:
            The deaths being returned as an integer
        Return:
            deaths as an integer
        """
        if deaths == None:
            return 0
        return deaths
    
    def get_deaths(self):
        """
        Returns the deaths returned from the search

        Return:
            The deaths returned from the search
        """
        return self.deaths
    
    def get_data_as_string(self):
        """
        Returns a string specifying the result of the search the object was created from

        Return:
            The results of the object's search in a string
        """
        return "Number of deaths due to "+self.cause+" for: "+self.gender+", age "+str(self.age)+" in "+self.state+", is: \n"+str(self.deaths)

"""
Stores information about the result of a search for the leading cause of death given a set of search terms.
"""
class LeadingCauseSearchResult(DeathsPerSearchResult):

    def __init__(self, search, cause, deaths):
        """
        Sets up an instance of LeadingCauseSearchResult

        Args:
            search : an object containing the terms the leading cause of death is being searched for
            deaths : the amount of deaths returned from the search
        Return:
            A LeadingCauseSearchResult object
        """
        search.set_cause(cause)
        super().__init__(search, deaths)
    
    def get_data_as_string(self):
        """
        Returns a string specifying the result of the search the object was created from

        Return:
            The results of the object's search in a string
        """
        if (self.deaths != 0):
            return "Leading cause of death for: "+self.gender+", age "+str(self.age)+" in "+self.state+", is: "+self.cause.lower()+", which was responsible for the deaths of "+str(self.deaths)+" people in this category."
        else:
            return "There were no deaths found for: "+self.gender+", age "+str(self.age)+" in "+self.state+"."
    
def connect():
    """
    Forms a connection to the database.

    Return:
        A connection to the database, throw an exception if the connection fails
    """
    try:
        connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection
    
def get_query_result(query, query_inputs = ()):
    """
    Returns a the information from the database specified by a inputted query and inputs

    Args:
        query : the query being requested to the database
        query_inputs : the parameters of the query
    Return:
        The result of the specified query, gives an exception if the query fails to execute
    """
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query, query_inputs)
        result = cursor.fetchall()
    except Exception as e:
        print("Internal error: ", e)
        exit()
    return result

def return_list_of_states():
    """
    Returns a sorted list of all unique states in the database

    Return:
        A sorted list of all unique states in the database
    """
    states = get_query_result("SELECT DISTINCT state_name FROM death_data;")
    reformatted_states = reformat_list(states)
    reformatted_states.sort()
    return reformatted_states

def return_list_of_causes(search = SearchArgs(None, None, None, None)):
    """
    Returns a sorted list of all unique causes in the database that match a given search

    Args:
        search : the specified terms to find unique causes of death for. By default will search all data.
    Return:
        A sorted list of all unique causes in the database that match a given search
    """
    query, query_inputs = return_query_with_search_arguments("SELECT DISTINCT cause FROM death_data WHERE TRUE", search)
    causes = get_query_result(query, query_inputs)
    causes = reformat_list(causes)
    causes.sort()
    return causes

def reformat_list(list):
    """
    Reformats a list of tuples as a list

    Args:
        list : the list being reformatted
    Return:
        A reformatted version of the provided list
    """
    new_list = []
    for item in list:
        new_list.append(item[0])
    return new_list

def get_fact():
    """
    Retrieve fact from facts at given random int
        
    Return:
        a string from facts 
    """
    index = random.randint(0, len(facts) - 1)
    random_fact = facts[index]
    return random_fact  

def get_search_result_from_function(function_type, search_args):
    """
    Returns the information about a search result for the passed arguments and function.

    Args:
        function_type : either 'dp' or 'lc', determines which function is used
        search_args : dictionary with the search arguments

    Return:
        an object containing information about the result of the search
    """
    if function_type == 'dp':
        search_args = return_arguments_as_search(search_args)
        return get_deaths_per_arguments(search_args)
    elif function_type == 'lc':
        search_args = return_arguments_as_search(search_args)
        return get_leading_cause_per_arguments(search_args)
    else:
        result = deaths_predictor(search_args)
        return result

def return_arguments_as_search(search_arguments):
    """
    Returns a string of search arguments as a SearchArgs object

    Args:
        search_arguments : a dictionary of arguments
    Return:
        search_arguments as a SearchArgs object
    """
    search = SearchArgs(None, None, None, None)

    for key in search_arguments:
        value = search_arguments[key]
        if value != "None":
            search.set_term_from_string(key, value)
    return search

def return_query_with_search_arguments(query, search):
    """
    Returns a query combined with a SearchArgs object's information

    Args:
        query : the query being requested
        search : the search the query applies to
    Return:
        A query combining the inputted query and the search's information
    """
    search_query, query_inputs = search.return_search_as_query()
    query += search_query+";"
    return query, query_inputs

def get_deaths_per_arguments(search):
    """
    Returns a DeathsPerSearchResult storing information about the amount of deaths for a specified search

    Args:
        search : a SearchArgs object containing the terms the amount of deaths is being searched for
    Return:
        A DeathsPerSearchResult storing information about the amount of deaths for the specified search
    """
    query, query_inputs = return_query_with_search_arguments("SELECT SUM(deaths) FROM death_data WHERE TRUE", search)
    total_deaths = get_query_result(query, query_inputs)
    total_deaths = reformat_list(total_deaths)

    result = DeathsPerSearchResult(search, total_deaths[0])
    return result

def get_leading_cause_per_arguments(search):
    """
    Returns a LeadingCauseSearchResult storing information about the leading cause of deaths for a specified search

    Args:
        search : a SearchArgs object containing the terms the leading cause of deaths is being searched for
    Return:
        A LeadingCauseSearchResult storing information about the leading cause of deaths for the specified search
    """
    causes = return_causes_without_misc_if_other_causes(search)
    leading_cause = ""
    leading_cause_deaths = 0

    for cause in causes:
        search_with_cause = search
        search_with_cause.set_cause(cause)

        cause_deaths = get_deaths_per_arguments(search_with_cause).get_deaths()
        leading_cause, leading_cause_deaths = return_greater_cause(cause, cause_deaths, leading_cause, leading_cause_deaths)
    result = LeadingCauseSearchResult(search, leading_cause, leading_cause_deaths)
    return result

def return_causes_without_misc_if_other_causes(search):
    """
    Returns a list of causes without the miscellaneous cause if it is not the only cause

    Args:
        Search : the search terms for the leading cause of deaths
    Return:
        A modified list of causes
    """
    causes = return_list_of_causes(search)

    if(len(causes) > 1):
        causes.remove("Miscellaneous")
        
    return causes

def return_greater_cause(cause, cause_deaths, leading_cause, leading_cause_deaths):
    """
    Returns the greater cause and death amount between compared parameters

    Args:
        cause : cause of death amount being compared
        cause_deaths : amount of deaths for new cause
        leading_cause : current leading cause of death
        leading_cause_deaths : amount of deaths for current leading cause
    Return:
        The cause and amount of deaths for the cause with more deaths
    """
    if (leading_cause_deaths < cause_deaths):
        leading_cause = cause
        leading_cause_deaths = cause_deaths
    return leading_cause, leading_cause_deaths

facts = ["The leading cause of death for infants younger than 1 is extreme immaturity with 13,660 deaths", 
    "For people 100 and up, the leading cause of death is dementia with 16,661 deaths.", "The most common cause of death for males is atherosclerotic heart disease, with 463,155 deaths.", 
    "The age group with the most deaths is 88 years old with 399,487 deaths.", "The most common cause of death for females is alzheimer's disease with 406,313 deaths"]

#referenced off of psycopg2 lab
#heavily referenced https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries


