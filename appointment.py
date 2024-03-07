from technician import Technician
from customer import Customer
from service import Service

import sqlite3
import datetime

class Appointment: 
    # initialize an instance
    def __init__(self, id: int, technician: Technician, customer: Customer, service: Service, date, time, isDone = False): 
        self.__id = id
        self.__technician = technician
        self.__customer = customer
        self.__service = service
        self.__isDone = isDone
        
    # define the representation of an instance, display it as an receipt 
    def __repr__(self): 
        return f"Receipt:\nAppointment ID: {self.__id}"
        
        
cus = Customer(1, "Hoang", "phanthanh@gmail.com", 4324343243)
print(cus)

connection = sqlite3.connect("./nailbar.db")

cursor = connection.cursor()

cursor.execute("""
    SELECT * FROM technicians
    WHERE id = 4
""")

row = cursor.fetchone()

technician = Technician(row[0], row[1], row[2], row[3], row[4])
print(technician)

cursor.execute("""
    SELECT * FROM services
""")

rows = cursor.fetchall()

services = [Service(row[0], row[1], row[2], row[4], row[5], row[2]) for row in rows]
    
for service in services:
    print(service)

connection.commit()
connection.close()

currTime = datetime.datetime.now()
print(currTime.strftime("%Y-%m-%d"))
print(currTime.strftime("%X %p"))

app = Appointment(1, technician, cus, "", currTime.strftime("%Y-%m-%d"), currTime.strftime("%X %p"), False)
print(app)

