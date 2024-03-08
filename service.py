import sqlite3

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

    @property 
    def id(self): 
        return self.__id
    
    @property 
    def type(self): 
        if self.__type == "Hand": return "H"
        elif self.__type == "Feet": return "F"
        else: return "R"
    
    @property 
    def name(self): 
        return self.__name
    
    @property 
    def duration(self): 
        return f"{self.__duration} mins"
    
    @property 
    def description(self): 
        return self.__description
    
    @property 
    def price(self): 
        return self.__price
    
    # Find all values in services database
    @classmethod
    def findAll(self): 
        connection = sqlite3.connect("./nailbar.db")

        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM services
        """)

        rows = cursor.fetchall()

        services = [Service(row[0], row[1], row[2], row[4], row[5], row[2]) for row in rows]

        connection.commit()
        connection.close()

        return services
    
    # Find by Id in services database
    @classmethod
    def findById(self, id): 
        connection = sqlite3.connect("./nailbar.db")
        cursor = connection.cursor()
        
        cursor.execute(f"""
            SELECT * FROM services
            WHERE id = {id}
        """)
        row = cursor.fetchone()
        
        connection.commit()
        connection.close()

        return Service(row[0], row[1], row[2], row[4], row[5], row[2])