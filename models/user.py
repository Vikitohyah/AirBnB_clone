#!usr/bin/python3
'''
Module: User
'''
from models.base_model import BaseModel


class User(BaseModel):
    ''' the user module inherits the based module
    extends some of its  user attributes '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
