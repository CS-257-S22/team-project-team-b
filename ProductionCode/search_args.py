"""
Written by Kai R. Weiner
"""

"""
Stores information about a search for the amount of deaths given a set of search terms.
"""
class SearchArgs:

    def __init__(self, state, age, gender, cause):
        """
        Sets up an instance of SearchArgs.

        Args
            state : state being searched for. If this term is not being searched: None
            age : age being searched for. If this term is not being searched: None
            gender : gender being searched for. If this term is not being searched: None
            cause : cause of death being searched for. If this term is not being searched: None
        Return:
            An SearchArgs object.
        """
        self.state = state
        self.age = age
        self.gender = gender
        self.cause = cause
    
    def set_state(self, new_state):
        """
        Sets the state being searched for to a specified input.

        Args:
            new_state : the new state being searched for
        """
        self.state = new_state

    def set_age(self, new_age):
        """
        Sets the age being searched for to a specified input.

        Args:
            new_age : the new age being searched for
        """
        self.age = new_age

    def set_gender(self, new_gender):
        """
        Sets the gender being searched for to a specified input.
        Args:
            new_gender : the new gender being searched for
        """
        self.gender = new_gender

    def set_cause(self, new_cause):
        """
        Sets the cause of death being searched for to a specified input.

        Args:
            new_cause : the new cause of death being searched for
        """
        self.cause = new_cause
    
    def get_term_from_string(self, term):
        """
        Returns a search term specified by a string.

        Args:
            term : the term being requested
        Return
            the value of the term being requested or an error message if the term does not exist
        """
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