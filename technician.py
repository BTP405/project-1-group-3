from person import Person
import sqlite3
import os
from termcolor import colored

class Technician(Person): 
    # initialize an instance
    def __init__(self, id: int, name: str, email: str, phone_number: int, specialization: str):
        assert id > 0, f"ID {id} must be more than 0" # error if the value is lower than 1
        # validate the specialization's name
        for special in specialization: 
            assert isinstance(special, str) and len(special) > 0, f"Special {special} length must be more than 0" # error if the value is not a string and the len is lower than 1
        
        super().__init__(name, email, str(phone_number)) 
        self.__id = id # the id of technician (priv)
        self.__specialization =  [special.strip() for special in specialization.split(',')] # the array of specialization (priv), view the "technicians" file
    
    # define the representation of an instance. Ex: Technician(_id: 4, name: Pat Kim, phone_number 1234567893, specialization: ['Nail Care', 'Acrylic Nails'])
    def __repr__(self): 
        return f"{self.__class__.__name__}(_id: {self.__id}, name: {self.name}, phone_number {self.phone_number}, specialization: {self.__specialization})"
    
    # return the id of a technician
    @property
    def id(self): 
        return self.__id
    
    # return a string representing the list of a technician's specialization
    @property
    def specialization(self): 
        return f"{self.__specialization[0]}"
    
    # return all the technician objects in the database
    @classmethod
    def findAll(self): 
        connection = sqlite3.connect("./nailbar.db")

        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM technicians
        """)
        
        rows = cursor.fetchall()

        technicians = [Technician(row[0], row[1], row[2], row[3], row[4]) for row in rows]

        connection.commit()
        connection.close()

        return technicians
    
    # return a technician object in the database by id
    @classmethod
    def findById(self, id): 
        connection = sqlite3.connect("./nailbar.db")
        cursor = connection.cursor()
        
        cursor.execute(f"""
            SELECT * FROM technicians
            WHERE id = {id}
        """)
        row = cursor.fetchone()
        
        connection.commit()
        connection.close()

        return Technician(row[0], row[1], row[2], row[3], row[4])
    
    # print the information of technicians
    @classmethod
    def printTechnician(self, selectedTechnician):
        os.system('cls||clear')
        technicians = Technician.findAll()
        print("******************************************************************")
        print("*                                                                *")
        for technician in technicians:
            if technician.id == selectedTechnician:
                print(
                    "* ", colored(f"{technician.id:>2}. {technician.name:<15} | {technician.specialization:<38}", color="green"), " *")
            else:
                print(
                    f"* {technician.id:>3}. {technician.name:<15} | {technician.specialization:<38}  *")
        print("*                                                                *")
        print("******************************************************************\n")