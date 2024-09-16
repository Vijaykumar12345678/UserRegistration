"""
@Author: Vijay Kumar M N
@Date: 2024-09-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-09-05
@Title : Python program for validating test cases using pytest.
"""

import pytest
from UserRegister import is_valid_name

# Test class using pytest
class TestFirstNameValidation:

    def test_valid_first_name(self):
        """
        Test valid first names.
        """
        assert is_valid_name("Smith") == True
        assert is_valid_name("Jones") == True
        assert is_valid_name("Brown") == True

   
        assert is_valid_name("va") == False
        assert is_valid_name("vijay") == False


    def main():
        obj=TestFirstNameValidation()
        obj.test_valid_first_name()

if __name__ == '__main__':
    pytest.main()