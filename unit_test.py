"""
@Author:Vijay Kumar M N
@Date: 2024-09-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-09-05
@Title : python program for to validate the test cases.
"""
import unittest
from UserRegister import is_valid_name,is_valid_email,is_valid_number,is_valid_password

class TestfirstNameValidation(unittest.TestCase):

    def test_valid_first_name(self):
        
        self.assertTrue(is_valid_name("Smith"))
        self.assertTrue(is_valid_name("Jones"))
        self.assertTrue(is_valid_name("Brown"))
        self.assertFalse(is_valid_name('va'))
        self.assertFalse(is_valid_name('vijay'))
    def test_valid_last_name(self):
        
        self.assertTrue(is_valid_name("Smith"))
        self.assertTrue(is_valid_name("Jones"))
        self.assertTrue(is_valid_name("Brown"))
        self.assertFalse(is_valid_name('va'))
        self.assertFalse(is_valid_name('vijay'))
    def test_valid_mail(self):
        self.assertTrue(is_valid_email("abc@yahoo.com"))
        self.assertTrue(is_valid_email("abc-100@yahoo.com"))
        self.assertFalse(is_valid_email("abc@.com.my"))
        self.assertFalse(is_valid_email(".abc@abc.com"))
    def test_valid_number(self):
        self.assertTrue(is_valid_number("91 8861912891"))
        self.assertTrue(is_valid_number("12 1234567890"))
        self.assertFalse(is_valid_number("8861912891"))
        self.assertFalse(is_valid_number("12 p61912891"))

    def test_valid_password(self):
        self.assertTrue(is_valid_password("Vijaykum"))
        self.assertTrue(is_valid_password("V2345678"))
        self.assertFalse(is_valid_password("vijay kumar"))
        self.assertFalse(is_valid_password("vijay"))

        
    
def main():
    obj=TestfirstNameValidation()
    obj.test_valid_first_name()
    obj.test_valid_last_name()
    obj.test_valid_mail()
    obj.test_valid_number()
    obj.test_valid_password()

if __name__ == '__main__':
    unittest.main()
