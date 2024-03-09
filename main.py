from service import Service
from customer import Customer
from technician import Technician
from appointment import Appointment
import os
import re

# this function display the main menu for completing the booking including select services, edit
# customer information, pick date and time, and view appointment info. The customer object is 
# passed in the parameter, and it doesn't return anything
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

# this function for the customer selecting the services. A list of services is passed in 
# the parameter, and it doesn't return anything
def selectService(services):
    while True:
        Service.printServices(services)
        print("Press X to go back")
        print("NOTE: Input the id again to unselect the serivce")
        choice = input("Select services for the appointment by ID: ")

        if choice.upper() == "X":
            break
        
        # if the choice is not equal to any service id, continue
        if int(choice) > 13 or int(choice) < 1:
            continue
        
        if int(choice) not in services: # if the choice doesn't exist, 
            services.append(int(choice)) # append the ervice to the list of services
        elif int(choice) in services:  # if the choice exists, 
            services.remove(int(choice)) # remove the selected service from the list

# this function prompts a form to obtain customer information. Nothing in the parameter, and 
# it returns a Customer object
def customerInfo():
    os.system('cls||clear')
    print("Input your information")
    name = input("Name: ")
    email = input("Email: ")
    phone_number = input("Phone Number: ")
    return Customer(name, email, phone_number) 

# this function prompts a form to edit customer information. If the customer leaves a field 
# empty, that field will not be changed this function also update the row of that customer 
# in the database. A customer object is passed in the parameter, and it doesn't return anything
def editCustomerInfo(customer):
    while True:
        os.system('cls||clear')
        print(f"Customer infomation:\nName: {customer.name}\nEmail: {customer.email}\nPhone number: {customer.phone_number}\n")
        print("Fill the new information. NOTE: leave the field empty if you don't want to change")
        new_name = input("Name: ")
        new_email = input("Email: ")
        new_phone_number = input("Phone Number: ")
        
        # if the new name field is not empty
        if not new_name:
            new_name = customer.name # update the new name
            
        # if the new email field is not empty
        if not new_email:
            new_email = customer.email # update the new email
            
        # if the new phone number field is not empty
        if not new_phone_number:
            new_phone_number = customer.phone_number # update the new phone number

        customer.update(customer.id, new_name, new_email, new_phone_number) # update the customer's row on database

        choice = input("Do you want to change your information again? (y/n): ")

        if choice.upper() == "NO" or choice.upper() == "N":
            break

# this function asks the customer selecting a technician for the appointment. A Technician
# object is passed in the parameter, and it return a Technician object
def selectTechnician(technician):
    while True:
        os.system('cls||clear')
        # printTechnician(technician)
        Technician.printTechnician(technician)
        print("Press X to go back")
        choice = input("Input the ID to select the technician: ")

        if choice.upper() == "X":
            break
        
        # if the choice is not equal to any technician's id, continue
        if int(choice) > 6 or int(choice) < 1 or int(choice) == technician:
            continue

        technician = int(choice)
    return technician

# this function asks the custoemr for date and time. A string is passed in the 
# parameter to hold the date and time as the format (yyyy-mm-dd, hh:mm), and it returns 
# the string of date and time. Create a subfunction to validate the customer's input. 
def selectDateTime(dateTime):
    # this function validates the string in the parameter if it follows the format(yyyy-mm-dd, hh:mm)
    def verify_date_time(datetime_str):
        pattern = r'^\d{4}-\d{2}-\d{2}, \d{2}:\d{2}$'
        if re.match(pattern, datetime_str): 
            return True
        else:
            return False
    
    while True:
        os.system('cls||clear')
        print(f"Your selected date time: {dateTime}\n")
        print("Press X to go back")
        choice = ""
        
        # if the input is not matched with the format and the choice is not 'X'
        while not verify_date_time(choice) and choice != 'x':
            choice = input("Enter date and time (yyyy-mm-dd, hh-mm): ") # keep asking for the date and time 

        if choice.upper() == "X":
            break

        dateTime = choice
    return dateTime

# this function displays the information of the appointment. In the parameter, a customer 
# object, the technician id, the list of service ids, and the date and time is passed. If 
# the parameter is valid, create an appointment object. Finally, return True if the user 
# confirms the appointment
def confirmBooking(cus_info, technicianId, serviceIds, dateTime):
    # validate the values in the parameter
    if cus_info == None:
        raise Exception("Please fill your personal information")
    elif len(serviceIds) == 0: 
        raise Exception("Please select services")
    elif technicianId == None: 
        raise Exception("Please select technician")
    elif dateTime == None: 
        raise Exception("Please select Date and Time")
    else: # if all the values are valid
        while True: 
            os.system('cls||clear')
            Appointment.printAppointment(cus_info, technicianId, serviceIds, dateTime)
            choice = ""

            while choice.upper() != "N" and choice.upper() != "NO" and choice.upper() != "Y" and choice.upper() != "YES":
                choice = input("Confirm your booking? (y/n): ")
                
            if choice.upper() == "N" or choice.upper() == "NO":
                return False
            else:        
                appointment = Appointment(technicianId, cus_info.id, dateTime, serviceIds)
                print("\nYour booking is created\n")
                a = input("Press enter to continue")
                return True

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
            choice = ''
        
        