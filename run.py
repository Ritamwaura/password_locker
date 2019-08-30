import pyperclip
from user import User
from credential import Credential


def create_user(first_name, last_name, phone, password):
    
    new_user = User(first_name, last_name, phone, password)
    return new_user


def save_users(user):

    user.save_user()
    
    
def del_user(user):
    
    user.delete_user()


def find_user(name):

    return User.find_by_name(name)

def check_existing_users(name):

    return User.user_exist(name)
