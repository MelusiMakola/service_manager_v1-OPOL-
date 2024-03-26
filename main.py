#Melusi Makola 2023/31/10
#Service Manager V1 - OPOL 
import random
from login import *
import hashlib

#Assignments
database = {}
ticket = {}
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
    with open("logged_in_users.txt", "a") as file:
        file.write(username + "\n")



#A function to generate a random number 
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


#A function to print the pricelist      
def print_pricelist(pricelist):
    for category, services in pricelist.items():
        print(f"{category}:")
        for service, price in services.items():
            print(f"\t\t{service}: R{price}")


#A function to build ticket
def build_ticket(ticket):
    ticket_items = {}
    if ticket_num in ticket.keys():
        while True:
            service = input("Enter Service (or type 'done' to finish adding services): ").strip()
            if service.lower() == 'done':
                break
            while True:
                amount = input(f"Enter amount for {service}: ").strip()
                if amount.isdigit():
                    ticket_items[service] = int(amount)
                    break
                else:
                    print("Please enter a valid amount (numeric).")
        return ticket_items
    else:
        print("Ticket not in database")

#A function to view ticket
def view_ticket(ticket_num):
    total = 0
    print(f"Ticket No {ticket_num}: ")
    print("{:<20} {:<10} {:<10}".format("Service", "Amount", "Subtotal"))
    print("-" * 40)
    for service, amount in ticket_items.items():
        subtotal = amount 
        total += subtotal
        print("{:<20} {:<10} {:<10}".format(service, amount, subtotal))
    print("-" * 40)
    print(f"Total: R{total}")




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
        menu.append("[AS]to Add a Service")

    for item in menu:
        print(item, end="  ")
    
    print("")
    
    command = input(user + " : ").lower()

    print("")
    
    if command == "c":

        client = input("Enter Client Name : ").lower()
       
        number = generate_unique_numbers(num_numbers=1, min_val=1, max_val=100)

        print(f"{client.title()} Your Ticket number is {str(number)}")
        print("")
        ticket[number] = client 

    elif command == "s":
            search = int(input("Enter Ticket number: "))
            print("")

            if not search in ticket:
                print("There's no ticket with that number in the database")
            else:
                print("Ticket number found")
                print(f"Ticket number {str(search)} has been assigned to {ticket[search]}" )
                print("")
            
           
    elif command == "l":
        print("Here's a List of the Clients in our record ")
        for p in ticket:
            print(f"[{str(p)}: {ticket[p]}]")
            print("")     

    elif command == "v":
        ticket_num = input("Ticket Number: ")
        view_ticket(ticket_num)

    elif command == "p" :
        print_pricelist(services)
        print("")

    elif command == "u":
        ticket_num = int(input("Enter Ticket Number: "))
        build_ticket(ticket)

    elif command == "q":
        print("Program Ended")
        quit()
        
    elif command == "a":
        admin_alias = input("Enter Admin Username: ")
        passcode = input("Enter Passcode: ")
        addAdmin(admin_alias, passcode)
        save_admin_hash(admin_alias, passcode)  

    elif command == "as":
        
        add_service(services, input("Enter Service Catergory: "), input("Enter Service name: "), input("Enter Amount: "))
        
                            
    else:
        print("Invalid command!! Use options provided")
        print("")
    


