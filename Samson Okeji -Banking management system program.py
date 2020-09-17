print("\t\t\t\t\t\t******Welcome! to Okeji Microfinance Bank******\n\t\t\t\t\t\t\t\t***Meet Our IT Support Lead: Samson Okeji***")

print("\n\t\t\t-----Main Menu-----")

bank_data = {}
user_data = {}

while True:
    choice = int(input("""
    1. New Customer
    2. Existing Customer
    3. Help Menu
    4. Exit
    
    Enter choice:\t"""))

    if choice == 1:
        name = input("Enter Name:\t")
        city = input("Enter city:\t")
        age = int(input("Enter Age:\t"))
        acct_type = input("Enter Account type:\t")
        amount = int(input("Enter initial Deposit Amount($):\t"))
        acct_no = int(input("Enter The account number you wish to use:\t"))
        new_password = int(input("Enter new password for this Account:\t"))

        user_data["name"] = name
        user_data["city"] = city
        user_data["age"] = age
        user_data["acct_type"] = acct_type
        user_data["amount"] = amount
        user_data["new_password"] = new_password

        bank_data["acct_no"] = acct_no
        bank_data["user_details"] = user_data

        print("\n-----Account created successfully-----")

    elif choice == 2:
        acct_no = int(input("Enter Your Account number:\t"))
        new_password = int(input("Enter Your Account Password:\t"))

        if acct_no == bank_data["acct_no"] and new_password == user_data["new_password"]:
            print("\n-----Account Exists! Welcome\t" + user_data["name"])


            while True:
                print("\n\t\t\t-----User Portal-----")

                user_choice = int(input("\n1. Check Balance \n2. Withdraw \n3. Deposit \n4. Back to Main menu \n\nEnter choice:\t"))
                if user_choice == 1:
                    print("Your Available balance:\t", bank_data["user_details"]["amount"])

                elif user_choice == 2:
                    withdraw_amt = int(input("Enter the Amount you wish to withdraw:\t"))
                    bank_data["user_details"]["amount"] = bank_data["user_details"]["amount"] - withdraw_amt
                    print("-----Amount withdrawn successfully!-----")

                elif user_choice == 3:
                    deposit_amt = int(input("Enter the amount you wish to deposit:\t"))
                    bank_data["user_details"]["amount"] = bank_data["user_details"]["amount"] + deposit_amt
                    print("\n----Amount deposited successfully!----")
                elif user_choice == 4:
                    break
                else:
                    print("\nInvalid Input! Please Enter a valid option (from 1 - 4")

        elif acct_no == bank_data["acct_no"] and not new_password == user_data["new_password"]:
            print("Invalid Password! Please login with a valid password!")
        else:
            print("\n-----Account does not Exist! Please open  a new account to start banking with us today!!!-----")
    elif choice == 3:
        print("\n-----Welcome to get help Menu-----")
        print("\nFor technical related issues, please do well to reach out to our IT support team lead, \nSamson Okeji via +2347062682400 or email @ engrsamsonokeji@gmail.com, \n\nBest Regards!")
    elif choice == 4:
        print("Program is now Exiting.......\nProgram Exited Successfully!")
        break
    else:
        print("Invalid Input! Please Enter a valid option (from 1 - 4)")
