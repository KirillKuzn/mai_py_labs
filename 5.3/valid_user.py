from valid_name import *
from valid_uname import *


def user_validation(last_name=None, first_name=None, username=None, **kwargs):
    if len(kwargs) != 0:
        raise KeyError
    
    for arg in [last_name, first_name, username]:
        if arg is None:
            raise KeyError
        
    for arg in [last_name, first_name, username]:
        if not isinstance(arg, str):
            raise TypeError
        
    name_validation(last_name)
    name_validation(first_name)
    username_validation(username)

    return {'last_name': last_name, 'first_name': first_name, 'username': username}


print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))