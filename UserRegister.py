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
        Validates if the last name starts with a capital letter and has at least 3 characters.
    
    parameters:
         first_name: str
    
    return: 
        bool
    """
    if re.fullmatch(r'^[A-Z][a-zA-Z]{2,}$', name):
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
            print("Valid last name entered!")
            return name
        else:
            attempts -= 1
            print(f"Invalid last name. You have {attempts} attempt(s) left.")
            name=input("ENter the vaild name: ")
    
    print("Sorry, you've exceeded the maximum number of attempts.")
    return None
def is_valid_email(email):
    """
    Description:
        Validates the email which user have entered    
    
    parameters:
         email: str the user entered mail
    
    return: 
        bool
    """


    if re.fullmatch(r"^[\w]+([._-][\w]+)*@[\w]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$",email):
        return True
    return False

def get_valid_email(email):

    """
    Description:
        Prompts the user for a valid mail and allows up to 5 attempts.
    
    parameters:
        mail: str the user entered mail
    
    return: 
        str or None
    """
    attempts = 5  
    
    while attempts > 0:
        if is_valid_name(email):
            print("Valid mail entered!")
            return email
        else:
            attempts -= 1
            print(f"Invalid mail. You have {attempts} attempt(s) left.")
            email=input("ENter the mail : ")
    
    print("Sorry, you've exceeded the maximum number of attempts.")
    return None

def main():

    first_name=input("Enter the first name:(Eg:Vij) ")
    vaild_name=get_valid_name(first_name)
    

    if  vaild_name:
        last_name=input("Enter the last name :(Eg: Kum)")
        vaild_name=get_valid_name(last_name)
        if  vaild_name:
            
            email=input("Enter the mail: (Eg: vijay@gmail.com)")
            vaild_mail=is_valid_email(email)
            if  vaild_mail:
                logger_init("UC_3").info(f"Valid details:")
            else:
                logger_init("UC_3").warning(f"InValid mail entered:")



        else:
            logger_init("UC_3").warning(f"Invalid  last name entered")
    else:
        logger_init("UC_3").warning(f"Invalid first name entered")

if __name__=="__main__":
    main()