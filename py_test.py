"""
@Author:Vijay Kumar M N
@Date: 2024-09-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-09-05
@Title : python program for to validate the test cases.
"""
import pytest
from UserRegister import is_valid_name,is_valid_email

class TestfirstNameValidation:

    def test_valid_first_name(self):
        
        assert is_valid_name("Smith")==True
        assert is_valid_name("Jones")==True
        assert is_valid_name("Brown")==True
        assert is_valid_name('va')==False
        assert is_valid_name('vijay')==False
    def test_valid_last_name(self):
        
        assert is_valid_name("Smith")==True
        assert is_valid_name("Jones")==True
        assert is_valid_name("Brown")==True
        assert is_valid_name('va')==False
        assert is_valid_name('vijay')==False
    def test_valid_mail(self):
        assert is_valid_email("abc@yahoo.com")==True
        assert is_valid_email("abc-100@yahoo.com")==True
        assert is_valid_email("abc@.com.my")==False
        assert is_valid_email(".abc@abc.com")==False
        
    
def main():
    obj=TestfirstNameValidation()
    obj.test_valid_first_name()
    obj.test_valid_last_name()
    obj.test_valid_mail()

if __name__ == '__main__':
    pytest.main()
