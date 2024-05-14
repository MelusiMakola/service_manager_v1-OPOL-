#Melusi Makola 2023/31/10
#Service Manager V1 - OPOL 
import random
from login import *
import hashlib
from datetime import datetime

#Assignments
ticket_database = {}
ticket_items = {}
services = {"Printing": {"Color": 7, "B&W": 5}, "Copying": {"Color": 5, "B&W": 3}}
admins = {"Melusi": "447",}
users = {"Mlungisi" : "884"}
logged_in = False
system_on = False 
login_attempts = 5
line = "*" * 50


print(line)
print(line)
print(line)
print(" Welcome ".center(50, "*"))
print(line)
print(line)
print("")

# A function for the header
def printHeader():
    version = " Service Manager V1.0 - OPOL "
    print(version.center(50, "*"))

#A function to add an admin
def addAdmin(admin_alias, passcode):
    admins[admin_alias] = passcode
    return admin_alias, passcode

# A function to hash passcode
def save_admin_hash(admin_alias, passcode):
    # Hash the admin alias and passcode using SHA-256
    hashed_admin_alias = hashlib.sha256(admin_alias.encode()).hexdigest()
    hashed_passcode = hashlib.sha256(passcode.encode()).hexdigest()
    
    # Combine admin alias and hashed passcode
    admin_data = f"{hashed_admin_alias}:{hashed_passcode}\n"
    
    # Save the data to the encrypted file
    with open("AAP.txt", 'a') as file:
        file.write(admin_data)


# A function to check if hash exists in our hash file
def is_admin_hash_present(admin_alias, passcode):
    hashed_admin_alias_to_check = hashlib.sha256(admin_alias.encode()).hexdigest()
    hashed_admin_passcode_to_check = hashlib.sha256(passcode.encode()).hexdigest()


    with open("AAP.txt", "r") as file:
        for line in file:
            stored_hashed_admin_alias, stored_admin_passcode = line.strip().split(':')
            if stored_hashed_admin_alias == hashed_admin_alias_to_check and stored_admin_passcode == hashed_admin_passcode_to_check:
                return True
    return False

#A function to check if user is admin
def isAdmin(user):
    if user in admins:
        return True

#A function to keep track of those that login            
def save_logged_in_user(username):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logged_in_users.txt", "a") as file:
        file.write(f"{current_datetime} - {username}\n")



#A function to generate a random ticket_num 
def generate_unique_numbers(num_numbers, min_val, max_val):
    generated_numbers = set()
    while len(generated_numbers) < num_numbers:
        new_number = random.randint(min_val, max_val)
        if new_number not in generated_numbers:
            generated_numbers.add(new_number)
            return new_number

    
#A Function to Add services
def add_service(main_dict, service_catergory, service, price):

    # Check if the outer key exists in the main dictionary
    if service_catergory not in main_dict:
        main_dict[service_catergory] = {}  # Create an inner dictionary if it doesn't exist
    
    # Add value to the inner dictionary
    main_dict[service_catergory][service] = price




# Define a function to capture tickets in a text document
def capture_tickets(ticket_database, file_path):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, 'a') as file:
        file.append("Tickets captured on: " + current_datetime + "\n\n")
        for ticket_num, client_name in ticket_database.items():
            file.write(f"Ticket Number: {ticket_num}, Client Name: {client_name}\n")





#A function to print the pricelist      
def print_pricelist(pricelist):
    for category, services in pricelist.items():
        print(f"{category}:")
        for service, price in services.items():
            print(f"\t\t{service}: R{price}")


def build_ticket(ticket_num, ticket_database):
    if ticket_num in ticket_database:
        ticket_items = {}
        while True:
            service = input("Enter Service (or type 'done' to finish adding services): ").strip()
            if service.lower() == 'done':
                break
            amount = input(f"Enter amount for {service}: ").strip()
            if amount.isdigit():
                ticket_items[service] = int(amount)
            else:
                print("Please enter a valid amount (numeric).")
        # Update ticket_database with ticket_items
        ticket_database[ticket_num] = ticket_items
    else:
        print("Ticket not in database")


# A function to view ticket_database
def view_ticket(ticket_num, ticket_items):
    if not ticket_items:
        print("No items in the ticket.")
        return

    total = sum(ticket_items.values())
    print(f"Ticket No {ticket_num}: ")
    print("{:<20} {:<10} {:<10}".format("Service", "Amount", "Subtotal"))
    print("-" * 40)
    for service, amount in ticket_items.items():
        print("{:<20} {:<10} {:<10}".format(service, amount, amount))
    print("-" * 40)
    print(f"Total: R{total}")





def update_ticket(ticket_num, client_name, ticket_items, ticket_database):
    if ticket_database is None:
        print("Error: Ticket database is not initialized.")
        return
    
    if ticket_num not in ticket_database:
        print("Error: Ticket not found in database.")
        return
    
    if ticket_items is None:
        print("Error: Ticket items are not provided.")
        return
    
    if not isinstance(ticket_items, dict):
        print("Error: Ticket items must be provided as a dictionary.")
        return
    
    # Check if the client name is provided
    if not client_name:
        print("Error: Client name is required.")
        return
    
    # Capture current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Update ticket information
    ticket_database[ticket_num] = {
        "client_name": client_name,
        "ticket_items": ticket_items,
        "last_updated": current_datetime
    }
    
    print("Ticket updated successfully!")


def add_ticket(ticket_num, ticket_items, ticket_database):
    if ticket_num not in ticket_database:
        ticket_database[ticket_num] = ticket_items
        print("Ticket added successfully!")
    else:
        print("Ticket already exists in the database.")

# A function to delete ticket from ticket_database
def delete_ticket(ticket_num, ticket_database):
    if ticket_num in ticket_database.keys():
        del ticket_database[ticket_num]
        print("Ticket deleted successfully!")
    else:
        print("Ticket not in database.")






#A function to register users
def registerUser():
    registered = False
    while not registered:
        user = input("Enter username: ").title()
        passcode = input("Enter passcode: ")
        passcode_verification = input("Confirm passcode: ")
        
        if passcode_verification == passcode:
            users[user] = passcode
            users.update({user : passcode})
            print(user + " Has been successfully registered")
            print("")
            registered = True
            print(users)
            
            
        elif passcode_verification != passcode:
            print("Passcodes have to match")


#Login Simulation
while not logged_in and login_attempts != 0:
    printHeader()
    print("LOGIN".center(50, "*"))
    print(line)
    print("")
    
    user = input("Username: ").title()
    passcode = input("Enter passcode: ")
    isAdmin(user)
    print("")
    
    if is_admin_hash_present(user, passcode):
        print("Access Granted (^_^)")
        print("")
        print(f"WELCOME {user}. You are an Admin")
        print("You can Create, Read, Update and Delete Data")
        print("")
        logged_in = True
        save_logged_in_user(f"{user} - Admin")    
        
    elif user in users:
       
       if users[user] == passcode:
           print("Login Successful. Welcome ")
           logged_in = True
           save_logged_in_user(f"{user} - Standard")
           
       else:
            print("Access Denied!!")
            print("You enter something incorrectly. Please try again.")
            login_attempts -= 1
            print("You have  " + str(login_attempts) + " Attempts remaining.")
               
    else:
            print("You are not registered")
            register = input("Register? [Y/N]: ").lower()
            if register == "y":
                registerUser()
            else:
                continue

            
        
command = ""

#A while loop so the  runs as long as the admin has not entered q to quit(Admin Page)
while command != "q" and logged_in:
    printHeader()
    print(line)
    print(" HOME ".center(50, "*"))
    print(line)
    
    print("")
    print((f" Logged in as {user} ").center(50, "•"))
    print("")
    
    menu = ["[C] to Create Client Ticket", "[U] to Update Client Ticket", "[S] to Search for Client", "[L] to List Clients", "[Q] to Quit", "[P] for Pricelist", "[V] to View Ticket"]
    if isAdmin(user):
        menu.append("[A]to Add Admin")
        menu.append("[AS]to Add A Service")

        

    for item in menu:
        print(item, end="  ")
    
    print("")
    
    command = input(user + " : ").lower()

    print("")
    
    # Assuming the generate_unique_numbers function is defined elsewhere in your code

    if command == "c":
        client = input("Enter Client Name: ").lower()
        ticket_num = generate_unique_numbers(num_numbers=1, min_val=1, max_val=100)  # Example usage, adjust as needed
        add_ticket(ticket_num, ticket_items, ticket_database)
        print(f"{client.title()}, your ticket ticket_num is {ticket_num}")
        ticket_database[ticket_num] = client
        # Capture tickets in the text document
        capture_tickets(ticket_database, file_path = "tickets.txt")


    elif command == "s":
            search = int(input("Enter Ticket ticket_num: "))
            print("")

            if not search in ticket_database:
                print("There's no ticket_database with that numberticket_ in the ")
            else:
                print("Ticket ticket_num found")
                print(f"Ticket ticket_num {str(search)} has been assigned to {ticket_database[search]}" )
                print("")
            
           
    elif command == "l":
        print("Here's a List of the Clients in our record ")
        for p in ticket_database:
            print(f"[{str(p)}: {ticket_database[p]}]")
            print("")     

    elif command == "v":
        ticket_num = int(input("Enter Ticket Number: "))
        ticket_items = ticket_database.get(ticket_num)
        if ticket_items:
            view_ticket(ticket_num, ticket_items)
        else:
            print("Ticket is Empty")
        

    elif command == "p" :
        print_pricelist(services)

    elif command == "u":
        ticket_num = int(input("Enter Ticket Number: "))
        ticket_items = build_ticket(ticket_num, ticket_database)
        client_name = ticket_database[ticket_num]
        update_ticket(ticket_num, client_name, ticket_items, ticket_database)


    elif command == "q":
        print("Program Ended")
        quit()
        
    elif command == "a":
        admin_alias = input("Enter Admin Username: ")
        passcode = input("Enter Passcode: ")
        addAdmin(admin_alias, passcode)
        save_admin_hash(admin_alias, passcode)  

    elif command == "d":
        ticket_num = int(input("Enter Ticket Number: "))
        delete_ticket(ticket_num, ticket_database)


    elif command == "as":
        
        add_service(services, input("Enter Service Catergory: "), input("Enter Service name: "), input("Enter Amount: "))
        
                            
    else:
        print("Invalid command!! Use options provided")
        print("")
    


