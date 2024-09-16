"""
@Author:Vijay Kumar M N
@Date: 2024-09-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-09-05
@Title : python program for to validate the test cases.
"""
import pytest
from UserRegister import is_valid_name

class TestfirstNameValidation:

    def test_valid_first_name(self):
        
        assert is_valid_name("Smith") ==True
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
def main():
    obj=TestfirstNameValidation()
    obj.test_valid_first_name()
    obj.test_valid_last_name()

if __name__ == '__main__':
    pytest.main()
