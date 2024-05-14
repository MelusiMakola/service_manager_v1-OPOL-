from main import login_attempts, printHeader, logged_in, isAdmin, line, admins, users, registerUser

while not logged_in and login_attempts != 0:
    printHeader()
    print("LOGIN".center(50, "*"))
    print(line)
    print("")
    
    user = input("Username: ").title().strip()
    passcode = input("Enter passcode: ")
    isAdmin(user)
    print("")
    
    if user in admins:
        
        if admins[user] == passcode:
            print("Access Granted (^_^)")
            print("")
            print(f"WELCOME {user}. You are an Admin")
            print("You can Create, Read, Update and Delete Data")
            print("")
            logged_in = True
            
        else:
            print("Access Denied!!")
            print("You enter something incorrectly. Please try again.")
            print("")
            login_attempts -= 1
            print("You have  " + str(login_attempts) + " Attempts remaining.")
        
    elif user in users:
       
       if users[user] == passcode:
           print("Login Successful. Welcome ")
           logged_in = True
           
           
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

            