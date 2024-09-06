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
        Validates if the  name starts with a capital letter and has at least 3 characters.
    
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
            print("Valid  name entered!")
            return name
        else:
            attempts -= 1
            print(f"Invalid name. You have {attempts} attempt(s) left.")
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


    if re.fullmatch(r"^[\w]+([._@#$%^&*-][\w]+)*@[\w]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$",email):
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
        if is_valid_number(email):
            print("Valid mail entered!")
            return email
        else:
            attempts -= 1
            print(f"Invalid mail. You have {attempts} attempt(s) left.")
            email=input("ENter the mail : ")
    
    print("Sorry, you've exceeded the maximum number of attempts.")
    return None



def is_valid_number(phone_number):
    """
    Description:
        Validates the phone_number which user have entered    
    
    parameters:
         phone_number: str the user entered phone_number
    
    return: 
        bool
    """


    if re.fullmatch(r"[0-9]{2}\s[0-9]{10}",phone_number):
        return True
    return False


def get_valid_number(phone_number):
    
    """
    Description:
        Prompts the user for a phone number and allows up to 5 attempts.
    
    parameters:
        phone_number: str the user entered phone number
    
    return: 
        str or None
    """
    attempts = 5 
    
    while attempts > 0:
        if is_valid_number(phone_number):
            print("Valid phone number entered!")
            return phone_number
        else:
            attempts -= 1
            print(f"Invalid phone number. You have {attempts} attempt(s) left.")
            phone_number=input("Enter the number: ")
    
    print("Sorry, you've exceeded the maximum number of attempts.")
    return None


def is_valid_password(passoword):
    """
    Description:
        Validates the password which user have entered    
    
    parameters:
         password: str the user entered password
    
    return: 
        bool
    """


    if re.fullmatch(r"(?=.*[A-Z])(?=.*[0-9])[\w]{8,}",passoword):
        return True
    return False

def get_valid_password(password):
    
    """
    Description:
        Prompts the user for a password and allows up to 5 attempts.
    
    parameters:
        password: str the user entered password
    
    return: 
        str or None
    """
    attempts = 5 
    
    while attempts > 0:
        if is_valid_password(password):
            print("Valid password entered!")
            return password
        else:
            attempts -= 1
            print(f"Invalid password and it should have minimum of 8 letters. You have {attempts} attempt(s) left.")
            password=input("Enter the password: ")
    
    print("Sorry, you've exceeded the maximum number of attempts.")
    return None




def main():

    first_name=input("Enter the first name(Eg:Vij):")
    vaild_name=get_valid_name(first_name)
    

    if  vaild_name:
        last_name=input("Enter the last name (Eg: Kum):")
        vaild_name=get_valid_name(last_name)
        if  vaild_name:
            
            email=input("Enter the mail(Eg: vijay@gmail.com):")
            vaild_mail=is_valid_email(email)
            if  vaild_mail:
                phone_number=input("Enter the phone number(Eg:91 1234567890): ")
                vaild_number=get_valid_number(phone_number)
                if  vaild_number:
                    password=input("Enter the password  eg( vijaykum) : ")
                    valid_password=get_valid_password(password)
                    if   valid_password:
                        logger_init("UC_7").info(f"Valid details entered!")
                    else:
                        logger_init("UC_7").warning(f" Invalid  password entered!")

                else:
                    logger_init("uc_7").warning(f"Invalid phone number entered:")

            else:
                logger_init("UC_7").warning(f"InValid mail entered:")



        else:
            logger_init("UC_7").warning(f"Invalid  last name entered:")
    else:
        logger_init("UC_7").warning(f"Invalid first name entered:")

if __name__=="__main__":
    main()