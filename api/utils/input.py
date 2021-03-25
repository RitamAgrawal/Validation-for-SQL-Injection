SQL_INJECTION_CHARACTERS = set(
    [chr(0), "\'", "\b", '\"', "\n", "\r", "\t", chr(26), '\\', "%", "_"]
)
# It is a set containing a list of characters that could be used to do SQL injection:
# chr(0) == '\x00'(\0) An ASCII NUL (0x00) character
# \' A single quote (') character.
# \b A backspace character.
# \" A double quote (") character.
# \n A newline (linefeed) character.
# \r A carriage return character.
# \t A tab character.
# chr(26) == '\x1a'(\Z) ASCII 26 (Ctrl+Z). See note following the table
# \\ A backslash (\) character.
# \% A % character.
# \_ A _ character.


def is_valid_input(data):
    """This method validates the input.

    Parameters
    -------
    data
        Required argument

    Returns
    -------
    boolean
        True: data is a string type and the len(data) > 0 
        False: All other cases, like, when input is not a string type or 
            data is an empty string
    """
    is_string = isinstance(data, str)
    # isinstance returns boolean
    # True: if first parameter(data) is a type of second parameter(str)
    # else returns False
    if is_string and len(data) > 0:
        return True
    else:
        return False


def compare_input(data):
    """This method compares the input.

    Parameters
    -------
    data
        Required argument

    Returns
    -------
    boolean
        True: if data exists and any element in set(data) is also present in set(SQL_INJECTION_CHARACTERS)
        False: when intersection of two sets(data and SQL_INJECTION_CHARACTERS) is null.
    """
    if data and len((set(data).intersection(SQL_INJECTION_CHARACTERS))) > 0:
        return True
    return False


def key_exists(key, dictionary={}):
    """This method checks if the key exists in dictionary.

    Parameters
    -------
    key: str
        Required argument
    dictionary: dict
        Optional argument(default= {})

    Returns
    -------
    boolean
        True: if key exists in dictionary.
        False: if key doesn't exist in dictionary
    """
    if key in dictionary:
        return True
    else:
        return False
