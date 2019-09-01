import string
import random
class User:
    """
    class that generates new instnaces of  users
    """
    user_list=[]

    def passGen(self,size = 8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        gen = ''.join(random.choice(char) for _ in range(size))
        return gen


    def __init__ (self,User_name,password,email,account_name):
        """
        __init__ method helps us to define properties of our objects.
        Args:
             account_name: New user account name.
             User_name: New user name.
             password: New user password.
             email: New user email.
        """

        self.account_name = account_name
        self.User_name = User_name
        self.password = password
        self.email = email     
    
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

