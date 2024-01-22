#!/usr/bin/python3
import pycodestyle
#from base_model import BaseModel
style_checker = pycodestyle.StyleGuide()

class User(BaseModel):
    
    '''This collect the city the user is in'''  
<<<<<<< HEAD
    city = ""
    state_id = ""
    
=======
    city: str = ""
    state_id: str = ""
>>>>>>> f503673cd94fe387867fb2698b9aa6c17e3a35e1
