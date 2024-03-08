from person import Person
import re

class Customer(Person): 
    NoOfCustomer = 0 # class attribute counts the number of customer did book appointment
    
    # initialize an instance
    def __init__(self, name: str, email: str, phone_number: int): 
        # this statement will be used when the application is scaled.
        Customer.NoOfCustomer += 1
        
        # assign the values to the instance's attributes
        self.__id = Customer.NoOfCustomer
        super().__init__(name, email, str(phone_number))
    
    # update the customer's information
    def update(self, name, email, phone_number): 
        self.name = name
        self.email = email
        self.phone_number = phone_number
        
    # define the representation of a instance
    def __repr__(self): 
        return f"Customer(_id: {self.__id}, name: {self.name}, email: {self.email}, phone number: {self.phone_number})"



