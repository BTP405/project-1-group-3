from service import Service 
from customer import Customer
from technician import Technician
from appointment import Appointment
import os
import msvcrt
from termcolor import colored

def printServices(selectedServices): 
    os.system('cls||clear')
    services = Service.findAll()
    print("******************************************************************")
    print("*                                                                *")
    print("*    ID  Name                              Duration    Price     *")
    for service in services: 
        if service.id in selectedServices:
            print("* ", colored(f"{service.id:>3}. {service.type} | {service.name:<30} {service.duration:<11} {service.price:<6}", color="green"), "   *")
        else: 
            print(f"*  {service.id:>3}. {service.type} | {service.name:<30} {service.duration:<11} {service.price:<6}    *")
    print("*                                                                *")
    print("*              H: Hand, F: Fee, R: Reflexology                   *")
    print("*                                                                *")
    print("******************************************************************\n")
    
def printTechnician(selectedTechnician): 
    os.system('cls||clear')
    technicians = Technician.findAll()
    print("******************************************************************")
    print("*                                                                *")
    for technician in technicians: 
        if technician.id == selectedTechnician:
            print("* ", colored(f"{technician.id:>2}. {technician.name:<15} | {technician.specialization:<38}", color="green"), " *")
        else: 
            print(f"* {technician.id:>3}. {technician.name:<15} | {technician.specialization:<38}  *")
    print("*                                                                *")
    print("******************************************************************\n")
    
def printAppointment(customer, technician, services, dateTime): 
    os.system('cls||clear')
    print("******************************************************************")
    print("*                                                                *")
    print("*  Your information:                                             *")
    print(f"*    Name: {customer.name:<15}                                       *")
    print(f"*    Email: {customer.email:<30}                       *")
    print(f"*    Phone number: {customer.phone_number:<15}                               *")
    print("*                                                                *")
    print("*  Your booking information:                                     *")
    print(f"*    Date and Time: {dateTime:<15}                             *")
    print(f"*    Technician: {technician.name:<15}                                 *")
    print("*    Service:                                                    *")
    for service in services:
        print(f"*      {service.type} | {service.name:<30} {service.duration:<11} {service.price:<6}     *")
    print("*                                                                *")
    print("******************************************************************\n")
    
def printMenu(customer): 
    os.system('cls||clear')
    print("******************************************************************")
    print("*                                                                *")
    print(f"*   Hi, {customer.name:<56} *")
    print("*                                                                *")
    print("*   1. Add services                                              *")
    print("*   2. Edit personal information                                 *")
    print("*   3. Select nail technician                                    *")
    print("*   4. Pick date and time                                        *")
    print("*   5. View appointment info                                     *")
    print("*                                                                *")
    print("******************************************************************\n")
    
def addService(services):
    while True: 
        printServices(services)
        print("Press X to go back")
        print("NOTE: Input the id again to unselect the serivce")
        choice = input("Select services for the appointment by ID: ")
        
        if choice.upper() == "X": 
            break
        
        if int(choice) > 13 or int(choice) < 1:
            continue
        
        if int(choice) not in services: 
            services.append(int(choice))
        elif int(choice) in services: 
            services.remove(int(choice))
        
def customerInfo(): 
    os.system('cls||clear')
    print("Input your information")
    name = input("Name: ")
    email = input("Email: ")
    phone_number = input("Phone Number: ")
    return Customer(name, email, phone_number)
    
def editCustomerInfo(customer): 
    while True:
        os.system('cls||clear')
        print(f"Customer infomation:\nName: {customer.name}\nEmail: {customer.email}\nPhone number: {customer.phone_number}\n")
        print("Fill the new information. NOTE: leave the field empty if you don't want to change")
        new_name = input("Name: ")
        new_email = input("Email: ")
        new_phone_number = input("Phone Number: ")
        
        if not new_name:
            new_name = customer.name
        if not new_email:
            new_email = customer.email
        if not new_phone_number:
            new_phone_number = customer.phone_number  
        
        customer.update(new_name, new_email, new_phone_number)
        
        choice = input("Do you want to change your information again? (y/n): ")
        
        if choice.upper() == "NO" or choice.upper() == "N": 
            break

def selectTechnician(technician): 
    while True: 
        os.system('cls||clear')
        printTechnician(technician)
        print("Press X to go back")
        choice = input("Input the ID to select the technician: ")
        
        if choice.upper() == "X": 
            break
        
        if int(choice) > 6 or int(choice) < 1 or int(choice) == technician:
            continue
        
        technician = int(choice)
    return technician
     
def selectDateTime(dateTime): 
    while True: 
        os.system('cls||clear')
        print(f"Your selected date time: {dateTime}\n")
        print("Press X to go back")
        choice = input("Enter date and time (yyyy-mm-dd, hh-mm): ")
        
        if choice.upper() == "X": 
            break
        
        dateTime = choice
    return dateTime

def confirmBooking(cus_info, technician, services, dateTime): 
    technician = Technician.findById(technician)
    services = [Service.findById(id) for id in services]
    while True: 
        os.system('cls||clear')
        printAppointment(cus_info, technician, services, dateTime)
        choice = ""

        while choice.upper() != "N" and choice.upper() != "NO" and choice.upper() != "Y" and choice.upper() != "YES":
            choice = input("Confirm your booking? (y/n): ")
            
        if choice.upper() == "N" or choice.upper() == "NO":
            return 0
        else:
            appointment = Appointment(technician, cus_info, dateTime, services)
            print(appointment)
            return 1

def run(): 
    # cus_info = customerInfo()
    # services = []
    # technician = None
    # dateTime = None
    # appointment = None
    
    cus_info = Customer("HOansdfsg", "sfdsd@gmail.com", 2342345434)
    services = [2, 4, 5, 13]
    technician = 2
    dateTime = "2024-03-08 10:00"
    appointment = None
    
    while True:    
        printMenu(cus_info)
        choice = input("Select the next action: ")
        
        if choice.upper() == "X": 
            break
        elif int(choice) == 1: 
            addService(services)
        elif int(choice) == 2: 
            editCustomerInfo(cus_info)
        elif int(choice) == 3: 
            technician = selectTechnician(technician)
        elif int(choice) == 4: 
            dateTime = selectDateTime(dateTime)
        elif int(choice) == 5: 
            created = confirmBooking(cus_info, technician, services, dateTime)
            if created: 
                break
        else: 
            continue
        
 
if __name__ == "__main__": 
    choice = ''
    run()
    # while True:  
        # while choice.upper() != 'N' and choice.upper() != 'NO' and choice.upper() != 'Y' and choice.upper() != 'YES':
        #     choice = input("Do you want to start booking? (y/n): ")

        # if choice.upper() == 'N' or choice.upper() == 'NO': 
        #     exit()
        # else:
        #     run()
        #     choice = ''
        
        
        
# cus = Customer(1, "Hoang", "phanthanh@gmail.com", 4324343243)
# print(cus)

# connection = sqlite3.connect("./nailbar.db")

# cursor = connection.cursor()

# cursor.execute("""
#     SELECT * FROM services
# """)

# rows = cursor.fetchall()

# services = []
# for row in rows:
#     services.append(Service(row[0], row[1], row[3], row[4], row[2])) # Positions of attributes in services (type, name, desc, duration, price)
    
# for service in services:
#     print(service)

# technicians = []
# for row in rows:
#     technicians.append(Technician(row[0], row[1], row[2], row[3], row[4]))
    
# for technician in technicians: 
#     print(technician)

# connection.commit()
# connection.close()