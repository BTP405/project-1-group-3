from technician import Technician
from customer import Customer
from service import Service
import sqlite3
import os

class Appointment: 
    # initialize an instance
    def __init__(self, technicianId: int, customerId: int, dateTime, services = []): 
        self.__id = Appointment.countAll() + 1
        self.__technician = technicianId
        self.__customer = customerId
        self.__services = services
        self.__dateTime = dateTime
        
        # for service in services:
        Appointment.insertOne(self.__id, technicianId, customerId, dateTime, services)
        
    # define the representation of an instance, display it as an receipt 
    def __repr__(self): 
        printServices = ""
        for service in self.__services: 
            printServices += str(service) + "\n"
        return f"Receipt:\nAppointment ID: {self.__id}\nTime: {self.__dateTime}\n{self.__technician}\n{self.__customer}\n{printServices}"
        
    @classmethod
    def printAppointment(self, customer, technicianId, serviceIds, dateTime):
        technician = Technician.findById(technicianId)
        services = [Service.findById(id) for id in serviceIds]
        os.system('cls||clear')
        print("******************************************************************")
        print("*                                                                *")
        print("*  Your information:                                             *")
        print(
            f"*    Name: {customer.name:<15}                                       *")
        print(f"*    Email: {customer.email:<30}                       *")
        print(
            f"*    Phone number: {customer.phone_number:<15}                               *")
        print("*                                                                *")
        print("*  Your booking information:                                     *")
        print(f"*    Date and Time: {dateTime:<15}                              *")
        print(
            f"*    Technician: {technician.name:<15}                                 *")
        print("*    Service:                                                    *")
        subtotal = 0
        for service in services:
            subtotal += float(service.price)
            print(
                f"*      {service.type} | {service.name:<30} {service.duration:<11} ${service.price:<6}    *")
        print(f"*                                        Subtotal:    ${subtotal:<5}     *")
        print(f"*                                             Tax:    ${str(round(subtotal*0.13, 2)):<5}     *")
        print(f"*                                       Total Due:    ${str(round(subtotal*1.13, 2)):<7}   *")
        print("*                                                                *")
        print("******************************************************************\n")
        
    @classmethod
    def insertOne(self, id, technicianId, customerId, dateTime, services): 
        connection = sqlite3.connect("./nailbar.db")
        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments(
                id INT PRIMARY KEY,
                technicianId INT,
                customerId INT, 
                dateTime TEXT, 
                services TEXT 
            )               
        """)
        
        cursor.execute(f"""
            INSERT INTO appointments VALUES
            ({id}, {technicianId}, {customerId}, "{dateTime}", "{services}")
        """)
        
        connection.commit()
        connection.close()
    
    @classmethod
    def countAll(self): 
        connection = sqlite3.connect("./nailbar.db")

        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments(
                id INT PRIMARY KEY,
                technicianId INT,
                customerId INT, 
                dateTime TEXT, 
                services TEXT 
            )               
        """)
        
        cursor.execute(f"""
            SELECT COUNT(*) FROM appointments;
        """)
        
        row = cursor.fetchone()
        connection.commit()
        connection.close()
        
        return row[0]