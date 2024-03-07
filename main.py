from service import Service 

def displayServiceList(): 
    services = Service.findAll()
    
    for service in services: 
        print(service)

def run(): 
    displayServiceList()
 
if __name__ == "__main__": 
    choice = ''
    while True:
        while choice.upper() != 'N' and choice.upper() != 'NO' and choice.upper() != 'Y' and choice.upper() != 'YES':
            choice = input("Do you want to start booking? (y/n): ")

        if choice.upper() == 'N' or choice.upper() == 'NO': 
            exit()
        else:
            run()
            choice = ''
        
        
        
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