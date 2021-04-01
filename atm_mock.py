import datetime

allowedUsers = []
allowedPasswords = []
userBalances = []

print("Welcome to the BLAZING ATM!!!")
print("Create an account to continue using the application.")

print("\n\nWelcome to Signup :)")
print("*********************")

user = False
password = False

while not user:
    user = input("\nEnter your preferred username: ")

while not password:
    password = input("Enter your preferred password: ")

allowedUsers.append(user)
user = False
allowedPasswords.append(password)
password = False
userBalances.append(float(0))

print("You have successfully created your account!!!\n\n")


while not user or not password:
    print("Welcome to Login :)")
    print("*******************")
    user = input("\nPlease enter your username: ")

    if user in allowedUsers:
        userId = allowedUsers.index(user)
        password = input("Please enter your password: ")
        
        if password == allowedPasswords[userId]:
            print(f"\n\nWelcome {user}, logged in at {datetime.datetime.now()}")        
            
            selectedOption = False

            while not selectedOption:
                print("\n\nCustomer Self-Service Menu")
                print("****************************")
                print("1. Cash Withdraw")
                print("2. Cash Deposit")
                print("3. Log a Complaint")
                print("4. Exit")
                
                
                try:
                    selectedOption = int(input("\n\nPlease select an option to proceed: "))

                    if selectedOption in [1, 2, 3, 4]:

                        if selectedOption == 1:
                            print(f"You have selected option {selectedOption}: Withdraw")
                            print(f"\n\nYour account balance is ${userBalances[userId]}")
                            amount = float(input("How much would you like to withdraw: "))

                            if ((amount >= 0) and (amount <= userBalances[userId])):
                                userBalances[userId] -= amount
                                print(f"Take your cash. You have successfully withdrawn ${amount} and your balance is ${userBalances[userId]}\n\n")
                            else:
                                print("Insufficient Funds or negative amount to withdraw!!!\n\n")
                            
                            input("Press any key to proceed: ")
                            selectedOption = False
                        elif selectedOption == 2:
                            print(f"You have selected option {selectedOption}: Cash Deposit")
                            print(f"\n\nYour account balance is ${userBalances[userId]}")
                            amount = float(input("How much would you like to deposit: "))
                            
                            if amount > 0:
                                userBalances[userId] += amount
                                print(f"You have successfully deposited ${amount} and your balance is ${userBalances[userId]}\n\n")
                            else:
                                print("You cannot deposit a negative amount!!!\n\n")
                            
                            input("Press any key to proceed: ")
                            selectedOption = False
                        elif selectedOption == 3:
                            print(f"You have selected option {selectedOption}: Complaint")
                            
                            complaint = input("\n\nWhat issue would you like to report:\n")
                            print("Thank you for contacting us. Your issue has been successfully submitted\n\n")
                            input("Press any key to proceed: ")
                            selectedOption = False
                        else:
                            selectedOption = True
                    else:
                        selectedOption = False
                        print("Wrong selection ): Please enter a valid selection!!")
                        input("\n\nPress any key to proceed: ")
                except:
                    selectedOption = False
                    print("Wrong selection ): Please enter a valid selection!!")  
                    input("\n\nPress any key to proceed: ")      
                
        else:
            password = False
            print("Password is incorrect ): Try again")
    else:
        user = False
        print("The user does not exist ): Try again")
