import unittest
from user import User

class TestUser(unittest.TestCase):
        '''
        Test class that defines test cases for the User class behaviours.

        Args:
            unittest.TestCase: TestCase class that helps in creating test cases
            '''
        def setUp(self):

            '''
            Set up method to run before each test cases.
            '''
            self.new_User = User("Astrid","546789","Astrid@gmail.com","twitter")

        def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_User.User_name,"Astrid")
            self.assertEqual(self.new_User.password,"546789")
            self.assertEqual(self.new_User.email,"Astrid@gmail.com")
            self.assertEqual(self.new_User.account_name,"twitter")
            
        
if __name__ == '__main__':
    unittest.main()    
