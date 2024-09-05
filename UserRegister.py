
from MyLogging import logger_init
import re

def is_valid_first_name(first_name):
    """
    Description:
        Validates if the last name starts with a capital letter and has at least 3 characters.
    
    parameters:
         first_name: str
    
    return: 
        bool
    """
    if re.match(r'^[A-Z][a-zA-Z]{2,}$', first_name):
        return True
    return False

def get_valid_first_name(name):
    """
    Description:
        Prompts the user for a valid last name and allows up to 5 attempts.
    
    parameters:
        name: str the user entered name
    
    return: 
        str or None
    """
    attempts = 5  
    
    while attempts > 0:
        if is_valid_first_name(name):
            print("Valid last name entered!")
            return name
        else:
            attempts -= 1
            print(f"Invalid last name. You have {attempts} attempt(s) left.")
            name=input("ENter the vaild name: ")
    
    print("Sorry, you've exceeded the maximum number of attempts.")
    return None
def main():

    first_name=input("Enter the name: ")
    vaild_name=get_valid_first_name(first_name)

    if  vaild_name:
        logger_init("UC_1").info(f"Valid name entered: {vaild_name}")
    else:
        logger_init("UC_1").info(f"Invalid name entered")

if __name__=="__main__":
    main()