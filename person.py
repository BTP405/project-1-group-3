from abc import ABCMeta, abstractstaticmethod
import re

class Person(metaclass = ABCMeta): 
    # initialize an instance
    def __init__(self, name: str, email: str, phone_number: str): 
        # validate the values in the parameter
        assert isinstance(name, str) and len(name) > 0, f"Name {name} length must be more than 0" # error if the value is not a string and the len is lower than 1
        assert bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)), f"Email {email} is invalid" # error if the pattern is not match the requirement
        assert bool(re.match(r'^\+?\d{10}$', phone_number)), f"Phone number {phone_number} length must be 10" # error if the len is not number and the len is not equal to 10
        
        # initialize attributes
        self.name = name # the name of person(str)
        self.email = email # the email of person(str)
        self.phone_number =  phone_number # the phone number of person(str)
    
    # the abstract function for defining the representation of an instance
    @abstractstaticmethod
    def __repr__(self): 
        pass
    

    
    