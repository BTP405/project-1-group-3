class Service: 
    def __init__(self, name, description, duration, price):
        assert isinstance(name, str) and len(name) > 0, f"Name {name} length must be between 0 and 20 characters"
 
        
        self.__name = name 
        self.__description = description
        self.__duration = duration
        self.__price = price 
    
    