import pyperclip
from user import User
from credential import Credential


def create_user(first_name, last_name, phone, password):
    
    new_user = User(first_name, last_name, phone, password)
    return new_user


def save_users(user):

    user.save_user()