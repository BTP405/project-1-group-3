import re

class Customer: 
    NoOfCustomer = 0 # class attribute counts the number of customer book appointment
    
    # initialize a Customer instance
    def __init__(self, name, email, phoneNumber): 
        # validate the value in the parameter
        assert isinstance(name, str) and len(name) > 0, f"Name {name} length must be between 0 and 20 characters"
        assert bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)), f"Email {email} is invalid"
        assert bool(re.match(r'^\+?\d{10}$', phoneNumber)), f"Phone number {phoneNumber} length must be 10"
        
        # if the value in the parameter is valid, increare the number of customer, and initialize the instance
        Customer.noOfCustomer += 1
        
        # assign the values to the instance's attributes
        self.__id = Customer.noOfCustomer
        self.__name = name 
        self.__email = email 
        self.__phoneNumber = phoneNumber
        
    # define the representation of a instance
    def __repr__(self): 
        return f"Customer(_id: {self.__id}, name: {self.__name}, email: { self.__email}, phone number: {self.__phoneNumber})"



