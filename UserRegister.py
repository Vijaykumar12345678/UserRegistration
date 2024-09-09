"""
@Author:Vijay Kumar M N
@Date: 2024-09-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-09-05
@Title : python program for to validate user input.
"""
from MyLogging import logger_init
import re

def is_valid_name(name):
    """
    Description:
        Validates if the name starts with a capital letter and has at least 3 characters.
    
    parameters:
         name: str
    
    return: 
        bool
    """
    if re.match(r'^[A-Z][a-zA-Z]{2,}$', name):
        return True
    return False

def get_valid_name(name):
    """
    Description:
        Prompts the user for a valid name and allows up to 5 attempts.
    
    parameters:
        name: str the user entered name
    
    return: 
        str or None
    """
    attempts = 5  
    
    while attempts > 0:
        if is_valid_name(name):
            print("Valid name entered!")
            return name
        else:
            attempts -= 1
            print(f"Invalid  name. You have {attempts} attempt(s) left.")
            name=input("Enter the vaild name: ")
    
    print("Sorry, you've exceeded the maximum number of attempts.")
    return None
def main():

    first_name=input("Enter the first name: ")
    vaild_name=get_valid_name(first_name)

    if  vaild_name:
        last_name=input("Enter the last name :")
        vaild_name=get_valid_name(last_name)
        if  vaild_name:
            logger_init("UC_2").info(f"Valid name entered for first name and last name.")
        else:
            logger_init("UC_2").info(f"Invalid name entered")
    else:
        logger_init("UC_2").info(f"Invalid name entered")

if __name__=="__main__":
    main()