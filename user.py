class User:
    """
    class that generates new instnaces of  users
    """
    user_list=[]

   


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

    def delete_user(self):
        '''
        delete_user method deletes user objects from user_list
        '''
        User.user_list.remove(self)


    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list


class credentails:
        """
        Class that generates new instances of Credentials
        """
        accounts=[]
def __init__(self,accountusername,accountname,accountpassword):
        """
        __init__ method that helps us define properties for our objectsself.
        Args:
        accountusername: New Credentials accountusername
        accountname: New Credentials accountname
        accountpassword: New Credentials accountpassword
        """
        self.accountusername= accountusername
        self.accountname = accountname
        self.accountpassword = accountpassword
