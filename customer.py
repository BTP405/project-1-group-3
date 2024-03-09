from person import Person
import sqlite3

class Customer(Person): 
    # initialize an instance
    def __init__(self, name: str, email: str, phone_number: int): 
        # assign the values to the instance's attributes
        self.id = Customer.countAll() + 1
        super().__init__(name, email, str(phone_number))
        Customer.insertOne(self.id, self.name, self.email, self.phone_number)
    
    # update the customer's information
    def update(self, id, name, email, phone_number): 
        self.name = name
        self.email = email
        self.phone_number = phone_number
        Customer.updateByID(id, name, email, phone_number)
        
    # define the representation of a instance
    def __repr__(self): 
        return f"Customer(_id: {self.id}, name: {self.name}, email: {self.email}, phone number: {self.phone_number})"

    # insert a new customer to the database
    @classmethod 
    def insertOne(self, id, name, email, phone_number): 
        print("Insert")
        connection = sqlite3.connect("./nailbar.db")

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers(
                id INT PRIMARY KEY,
                name TEXT, 
                email TEXT, 
                phone_number INT
            )               
        """)

        cursor.execute(f"""
            INSERT INTO customers VALUES
            ({id}, "{name}", "{email}", {phone_number})
        """)
        
        connection.commit()
        connection.close()
        
    @classmethod
    def countAll(self): 
        connection = sqlite3.connect("./nailbar.db")

        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers(
                id INT PRIMARY KEY,
                name TEXT, 
                email TEXT, 
                phone_number INT
            )               
        """)
        
        cursor.execute(f"""
            SELECT COUNT(*) FROM customers;
        """)
        
        row = cursor.fetchone()
        connection.commit()
        connection.close()
        
        return row[0]

    @classmethod
    def updateByID(self, id, name, email, phone_number): 
        connection = sqlite3.connect("./nailbar.db")

        cursor = connection.cursor()
        
        cursor.execute(f"""
            UPDATE customers              
            SET name = "{name}", email = "{email}", phone_number = "{phone_number}"
            WHERE id = {id}
        """)
        
        row = cursor.fetchone()
        connection.commit()
        connection.close()
        
    


