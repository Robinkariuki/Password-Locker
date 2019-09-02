#!/usr/bin/env python3.7

from user import User

def create_user(fname,lname,phone,email,password):
    '''
    Function to create a  new user

    '''
    new_user = User(fname,lname,phone,email,password):
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()