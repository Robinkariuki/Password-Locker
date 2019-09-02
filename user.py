import pyperclip

class User:
    """
    class that generates new instnaces of  users
    """
    user_list=[]

   


    def __init__ (self,first_name,last_name,number,email,password):
        """
        __init__ method helps us to define properties of our objects.
        Args:
             first_name: New user first name.
             last_name New user last name.
             number: New user number.
             password: New user password.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email  
        self.password = password   
    
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
    def find_by _number(cls,number):

         '''
        Method that takes in a number and returns a user that matches that number.
        Args:
            number: Phone number to search for
        Returns :
            User of person that matches the number.
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                return user


    @classmethod
    def user_exist(cls,number):
         '''
        Method that checks if a user exists from the user list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                return True

            return False

    @classmethod
    def display_users(cls): 
        '''
        A method that returns the user list 

        '''
        return cls.user_list

    @classmethod
    def copy_email(cls,number):
        user_found = user.find_by_number(number) 
        pyperclip.copy(user_found.email)   





