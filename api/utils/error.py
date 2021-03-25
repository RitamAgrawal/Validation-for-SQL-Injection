"""This script has all the error methods.
"""
def error_bad_request():
    """A helper function to error_message method. Displays error message due to 
    incorrect json format/ bad requests.
    like, {"payload":"uht99",}
    
    Returns
    -------
    string
        a string representing to verify the input.
    """
    return "Bad Request. Please verify your Input"


def error_missing_payload():
    """A helper function to error_message method.Displays error message due to 
    absence of key="payload" in the request.
    like, {"pay":"uht99"}
    
    Returns
    -------
    string
        a string informing that the payload is missing.
    """
    return "Invalid Input. Request is missing \"payload\"."


def error_invalid_input():
    """A helper function to error_message method.Displays error message due to 
    invalid input.
    like, value of payload is not a string {"payload":99}
    
    Returns
    -------
    string
        a string representing to verify the input.
    """
    return "Invalid Input. Please verify your Input"


def error_message(err_type=""):
    """This method is called everytime an error is to be displayed.

    Parameters
    -------
    err_type(default "")
        optional parameter

    Returns
    -------
    tuple
        (a helper function which returns a string, status code) 
    """
    if (err_type == "BAD_REQUEST"):
        return error_bad_request(), 400
    elif err_type == "MISSING_PAYLOAD":
        return error_missing_payload(), 400
    else:
        return error_invalid_input(), 400
