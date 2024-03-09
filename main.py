from service import Service
from customer import Customer
from technician import Technician
from appointment import Appointment
import os

# this function display the main menu for completing the booking including select services, add
# personal. The customer 
# object is passed in the parameter. 
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


def selectService(services):
    while True:
        Service.printServices(services)
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
        print(
            f"Customer infomation:\nName: {customer.name}\nEmail: {customer.email}\nPhone number: {customer.phone_number}\n")
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

        customer.update(customer.id, new_name, new_email, new_phone_number)

        choice = input("Do you want to change your information again? (y/n): ")

        if choice.upper() == "NO" or choice.upper() == "N":
            break


def selectTechnician(technician):
    while True:
        os.system('cls||clear')
        # printTechnician(technician)
        Technician.printTechnician(technician)
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


def confirmBooking(cus_info, technicianId, serviceIds, dateTime):
    if cus_info == None:
        raise Exception("Please fill your personal information")
    elif len(serviceIds) == 0: 
        raise Exception("Please select services")
    elif technicianId == None: 
        raise Exception("Please select technician")
    elif dateTime == None: 
        raise Exception("Please select Date and Time")
    else: 
        while True: 
            os.system('cls||clear')
            Appointment.printAppointment(cus_info, technicianId, serviceIds, dateTime)
            choice = ""

            while choice.upper() != "N" and choice.upper() != "NO" and choice.upper() != "Y" and choice.upper() != "YES":
                choice = input("Confirm your booking? (y/n): ")
                
            if choice.upper() == "N" or choice.upper() == "NO":
                return 0
            else:        
                appointment = Appointment(technicianId, cus_info.id, dateTime, serviceIds)
                return 1

def run(): 
    # temporary variables
    cus_info = customerInfo() # cus_info is a Customer object
    serviceIds = [] # the list of the selected services' id
    technicianId = None # the id of the selected technician
    dateTime = None # the selected date and time
    
    while True:    
        printMenu(cus_info)
        choice = input("Select the next action: ")
        
        if choice.upper() == "X": 
            break
        elif int(choice) == 1: 
            selectService(serviceIds)
        elif int(choice) == 2: 
            editCustomerInfo(cus_info)
        elif int(choice) == 3: 
            technicianId = selectTechnician(technicianId)
        elif int(choice) == 4: 
            dateTime = selectDateTime(dateTime)
        elif int(choice) == 5: 
            created = confirmBooking(cus_info, technicianId, serviceIds, dateTime)
            if created: 
                break
        else: 
            continue
        
if __name__ == "__main__": 
    choice = ''
    while True: 
        os.system('cls||clear') 
        
        # if the user's input is not "NO" or "YES", it will prompt the question again
        while choice.upper() != 'N' and choice.upper() != 'NO' and choice.upper() != 'Y' and choice.upper() != 'YES':
            choice = input("Do you want to start booking? (y/n): ")

        # if the user's input is "NO",
        if choice.upper() == 'N' or choice.upper() == 'NO': 
            exit() # exit the program
        else: # otherwise
            run() # start running the program
            print("\nYour booking is created\n")
            a = input("Press enter to continue")
            choice = ''
        
        