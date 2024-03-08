from technician import Technician
from customer import Customer
from service import Service


class Appointment: 
    NoOfAppointment = 0 
    
    # initialize an instance
    def __init__(self, technician: Technician, customer: Customer, dateTime, services = [], isDone = False): 
        Appointment.NoOfAppointment += 1
        
        self.__id = Appointment.NoOfAppointment
        self.__technician = technician
        self.__customer = customer
        self.__services = services
        self.__dateTime = dateTime
        self.__isDone = isDone
        
        
        
    # define the representation of an instance, display it as an receipt 
    def __repr__(self): 
        printServices = ""
        for service in self.__services: 
            printServices += str(service) + "\n"
        return f"Receipt:\nAppointment ID: {self.__id}\nTime: {self.__dateTime}\n{self.__technician}\n{self.__customer}\n{printServices}"
        

# import sqlite3
# import datetime
# cus = Customer(1, "Hoang", "phanthanh@gmail.com", 4324343243)
# # print(cus)

# connection = sqlite3.connect("./nailbar.db")

# cursor = connection.cursor()

# cursor.execute("""
#     SELECT * FROM technicians
#     WHERE id = 4
# """)

# row = cursor.fetchone()

# technician = Technician(row[0], row[1], row[2], row[3], row[4])
# # print(technician)

# cursor.execute("""
#     SELECT * FROM services
#     WHERE type = "Reflexology"
# """)

# rows = cursor.fetchall()

# services = [Service(row[0], row[1], row[2], row[4], row[5], row[2]) for row in rows]
    
# # for service in services:
# #     print(service)

# connection.commit()
# connection.close()

# currTime = datetime.datetime.now()
# # print(currTime.strftime("%Y-%m-%d"))
# # print(currTime.strftime("%X %p"))

# app = Appointment(1, technician, cus, currTime.strftime("%Y-%m-%d"), currTime.strftime("%X %p"), False, services)
# print(app)

# # Parsing the datetime string to a datetime object
# # datetime_obj = datetime.datetime.strptime("2014-05-03", "%Y-%m-%d")
# # print(datetime_obj.date())