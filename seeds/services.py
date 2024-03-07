import sqlite3

connection = sqlite3.connect("nailbar.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS services(
        id INT PRIMARY KEY,
        type TEXT, 
        name TEXT, 
        desc TEXT, 
        duration INT, 
        price FLOAT 
    )               
""")

cursor.execute("""
    INSERT INTO services VALUES
    (1, "Hand", "Manicure", "", 25, 20),
    (2, "Hand", "Shellac Polish Change Hand", "", 35, 26),
    (3, "Hand", "Shellac Manicure", "", 15, 36),
    (4, "Hand", "Nail Design", "$5 & up", 10, 5),
    (5, "Hand", "Paraffin Treatment Hand", "", 10, 10),
    (6, "Feet", "Delux Pedicure", "", 60, 50),
    (7, "Feet", "Polish Change Feet", "", 15, 17),
    (8, "Feet", "Pedicure", "", 45, 36),
    (9, "Feet", "Shellac Pedicure", "", 60, 50),
    (10, "Feet", "Shellac Polish Change Feet", "", 25, 30),
    (11, "Reflexology", "Reflexology-10 minutes", "", 10, 15),
    (12, "Reflexology", "Reflexology-15 minutes", "", 15, 20),
    (13, "Reflexology", "Reflexology-30 minutes", "", 30, 35)
""")

connection.commit()
connection.close()
