
import unittest
from UserRegister import is_valid_name

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
def main():
    obj=TestfirstNameValidation()
    obj.test_valid_first_name()
    obj.test_valid_last_name()

if __name__ == '__main__':
    unittest.main()
