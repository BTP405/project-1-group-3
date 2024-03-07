from person import Person
import re

class Customer(Person): 
    NoOfCustomer = 0 # class attribute counts the number of customer did book appointment
    
    # initialize an instance
    def __init__(self, id: int, name: str, email: str, phone_number: int): 
        # validate the value in the parameter
        assert id > 0, f"ID {id} must be more than 0" # error if the value is lower than 1
        
        # this statement will be used when the application is scaled.
        # Customer.noOfCustomer += 1
        # self.__id = Customer.noOfCustomer
        
        # assign the values to the instance's attributes
        self.__id = id
        super().__init__(name, email, str(phone_number))
        
    # define the representation of a instance
    def __repr__(self): 
        return f"Customer(_id: {self.__id}, name: {self.name}, email: {self.email}, phone number: {self.phone_number})"



