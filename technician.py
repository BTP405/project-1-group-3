from person import Person

class Technician(Person): 
    # initialize an instance
    def __init__(self, id: int, name: str, email: str, phone_number: int, specialization: str):
        assert id > 0, f"ID {id} must be more than 0" # error if the value is lower than 1
        for special in specialization:
            assert isinstance(special, str) and len(special) > 0, f"Special {special} length must be more than 0" # error if the value is not a string and the len is lower than 1
        
        super().__init__(name, email, str(phone_number)) 
        self.__id = id # the id of technician
        self.__specialization =  [special.strip() for special in specialization.split(',')] # the array of specialization, view the "technicians" file
    
    # define the representation of an instance. Ex: Technician(_id: 4, name: Pat Kim, phone_number 1234567893, specialization: ['Nail Care', 'Acrylic Nails'])
    def __repr__(self): 
        return f"{self.__class__.__name__}(_id: {self.__id}, name: {self.name}, phone_number {self.phone_number}, specialization: {self.__specialization})"
    
