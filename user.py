class User:
    """
    class that generates new instnaces of  users
    """
    User_list=[]

   


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
