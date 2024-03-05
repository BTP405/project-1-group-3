class Technician: 
    NoOfTechnicians = 0 
    
    def __init__(self, id, name, specialization): 
        # validate the data in the parameter 
        assert isinstance(name, str) and len(name) > 0, f"Name {name} length must be between 0 and 20 characters"

        Technician.NoOfTechnicians += 1
        
        self.__id = Technician.NoOfTechnicians
        self.__name = name 
        self.__specialization = specialization
        
# specialization is an array of service
        