import psycopg2
import psqlConfig as config

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