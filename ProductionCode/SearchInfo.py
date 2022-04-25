"""
Written by Kai R. Weiner
"""

"""
Stores information about a search for the amount of deaths given a set of search terms.
"""
class SearchInfo:

    """
    Sets up an instance of SearchInfo.
    @param state : state being searched for. If this term is not being searched: None
    @param age : age being searched for. If this term is not being searched: None
    @param gender : gender being searched for. If this term is not being searched: None
    @param cause : cause of death being searched for. If this term is not being searched: None
    """
    def __init__(self, state, age, gender, cause):
       self.state = state
       self.age = age
       self.gender = gender
       self.cause = cause
    
    """
    Sets the state being searched for to a specified input.
    @param new_state : the new state being searched for
    """
    def set_state(self, new_state):
        self.state = new_state

    """
    Sets the age being searched for to a specified input.
    @param new_age : the new age being searched for
    """
    def set_age(self, new_age):
        self.age = new_age

    """
    Sets the gender being searched for to a specified input.
    @param new_gender : the new gender being searched for
    """
    def set_gender(self, new_gender):
        self.gender = new_gender

    """
    Sets the cause of death being searched for to a specified input.
    @param new_cause : the new cause of death being searched for
    """
    def set_cause(self, new_cause):
        self.cause = new_cause
    
    """
    Returns a search term specified by a string.
    @param term : the term being requested
    @return : the value of the term being requested or an error message if the term does not exist
    """
    def get_term_from_string(self, term):
        if(term == "state"):
            return self.state
        if(term == "age"):
            return self.age
        if(term == "gender"):
            return self.gender
        if(term == "cause"):
            return self.cause
        else:
            return "Term not contained in search"