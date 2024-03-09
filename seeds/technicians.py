import sqlite3

connection = sqlite3.connect("nailbar.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS technicians(
        id INT PRIMARY KEY,
        name TEXT, 
        email TEXT, 
        phone_number INT, 
        specialization TEXT 
    )               
""")

cursor.execute("""
    INSERT INTO technicians VALUES
    ("1", "Alex Morgan", "alex@example.com", "1234567890", "Manicure and Pedicure"),
    ("2", "Jamie Lee", "jamie@example.com", "1234567891", "Nail Art, Extension"),
    ("3", "Chris Wu", "chris@example.com", "1234567892", "Shallac Manicure and Pedicure,Gel Nails"),
    ("4", "Pat Kim", "pat@example.com", "1234567893", "Nail Care,Acrylic Nails"),
    ("5", "Sam Rivera", "sam@example.com", "1234567894", "3D Nail Art"),
    ("6", "Jordan Casey", "jordan@example.com", "1234567895", "Dip Powder Nails")
""")

connection.commit()
connection.close()
