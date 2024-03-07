class Service: 
    # initialize an instance
    def __init__(self, id, type: str, name: str, duration: float, price: float, description = ''):
        # validate the value in the parameter
        assert id > 0, f"ID {id} is invalid" # error if the value is less than 1
        assert isinstance(name, str) and len(name) > 0, f"Name {name} is invalid" # error if the value is not a string and the len is lower than 1
        assert isinstance(type, str) and len(type) > 0, f"Type {name} is invalid" # error if the value is not a string and the len is lower than 1
        assert duration > 0.0, f"Duration {duration} must be over 0.0" # error if the len is lower than 1
        assert price > 0.0, f"Price {price} must be over 0.0" # error if the len is lower than 1
        
        # initialize attributes
        self.__id = id # the id of service(int)
        self.__type = type # the type of service(str). Ex: hand, feet, and relexology
        self.__name = name # the name of service(str). Ex: with hand, it can be Manicure, or Shellac Manicure
        self.__description = description # the description of the service(str), this attribute can be empty
        self.__duration = duration # the duration of the serivce(int), calculate in minute. 
        self.__price = price # the price of the service(float)
        
    # define the representation of an instance. Ex: Service(type: Hand, name: Manicure, description: , duration: 25, price: 20.0)
    def __repr__(self): 
        return f"{self.__class__.__name__}(_id: {self.__id},type: {self.__type}, name: {self.__name}, description: {self.__description}, duration: {self.__duration}, price: {self.__price})"
