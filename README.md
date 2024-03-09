## 1. Project Title and Description
    - Title: Nail Salon Booking System
    - Description: This project is a nail salon booking system. The purpose of this application is for clients to securely book their appointments with the salon. This booking system is very intuitive and easy to understand. Users are able to fill in their personal information and select their nail technician, appointment date and time and the type of nail service. This application is also capable of updating the information of the customer.
## 2. Installation
    - Dependencies: 
        + termcolor
        
    - Installation Instructions: 
        + Clone the repository to your local folder. 
        + Check if the "nailbar.db" exists. If it doesn't exist, compile to files in the 'seeds' folder. 
        + Compile the main.py file to start the program.
        
## 3. Usage
    - Examples: 
        + At the beginning, you have to fill your personal information (name, email, and phone number) to start the program.
        + Then, a list of options for booking an appointment will be displayed. 
        + To confirm the booking, select option 5 to view the appointment information and confirm. 
        + NOTE: You must complete selecting the services, technician, and date and time. If any field is empty, the program will be terminated. 
    
    - Configuration: 
        + Create Services collection with values by running this command: python ./seeds/services.py
        + Create Technicians collection with values by running this command: python ./seeds/technicians.py
        
## 4. Features
### 
Classes : 
1. Person
   This is an abstract class representing a Person
   Attributes :
   - name : string
    - email: string
    - phone number : int
3. Technician
   This class is a child class of Person.
   Attribute :
   - id: int
   - specialization : list - representing the speacializations for each technician, for example ['Nail Care', 'Acrylic Nails'])
     Property :
  - id - this a query to return the id of technitican
  - 
4. Customer
   This class is a child class of Person
   Attribute :
   - id : int
   Instance Method :
   - update(self, name, email, phone_number) : update the information of a customer.
 * id for customer and technitian are of different categories, so we do not have it as an attribute in Person.
5. Appointment
   This class represents an appointment record.
   - id : int
   - technician : Technician
   - customer : Customer
   - service : []
   - datetime : datetime
   - isDone : bool
Methods :

## 5. Contributing
    - Guidelines: 
        + We use the branch in github to contribute to our project. To use branch for commiting the project, we cloned the repository to the local folder, and then creates a personal branch by Visual Studio. After pushing the code to the main file, we will verify before merging the code to the main branch
    
    - Code Style: 
        + We follow all the requirement in the project instruction, including OOP and PEP8.
        
## 6. Credits
    - Authors: 
        + Hoang Phan - 101662229
        + Arlene Pham - 11079222
        + Alyssa Maria Gamelo - 064540040
        
    - Acknowledgments: 
        + Youtube: https://www.youtube.com/watch?v=jhtbhSpV5YA&t=473s
        
## 7. License
    - License Information: Specify the license under which your project is distributed.
## 8. Additional Sections (Optional)
    - FAQ: Include frequently asked questions and their answers.
    - Troubleshooting: Provide solutions to common issues or troubleshooting tips.
    - Roadmap: Outline the future development plans for your project.
    - Changelog: Document changes and updates to your project over time.

## Markdown Formatting Tips
  - Use headings (#, ##, ###, etc.) to structure your document.
  - Utilize lists (- or 1.) for easy-to-read information.
  - Include links to relevant resources or documentation.
  - Add code blocks using triple backticks (```) for code snippets.
  - Use images or diagrams to enhance understanding where applicable.
