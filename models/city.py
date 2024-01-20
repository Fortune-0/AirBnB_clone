#!/usr/bin/python3
import pycodestyle
#from base_model import BaseModel
style_checker = pycodestyle.StyleGuide()

class User(BaseModel):
    
    '''This collect the city the user is in'''  
    city = ""
    state_id = ""
    