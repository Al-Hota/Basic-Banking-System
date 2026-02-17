
menu = {
    1: {
        "Account": "User1", 
        "Balance": 5000, 
        "History": [], 
        "PIN": "4334", 
        "Locked": False
        },
    2: {
        "Account": "User2", 
        "Balance": 3450, 
        "History": [], 
        "PIN": "5112", 
        "Locked": False
        },
    3: {
        "Account": "User3", 
        "Balance": 10000, 
        "History": [], 
        "PIN": "5141", 
        "Locked": False
        }
}



def actions(menu_id):
    choices = menu[menu_id]

    if choices["Locked"]:
        print("Locked.")
        return

    retries = 3
    while retries > 0:
        pin = input("Please enter your bank PIN:")
        if pin == choices["PIN"]:
            print(f"You currently have: {choices['Balance']}")
            while True:
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Return to menu.")
                print("4. View Transaction History.")
                choice = input("Choose: ")
                if choice == "1":
            
                    deposit_amount = float(input("Enter amount to deposit: "))
                    if deposit_amount < 0:
                        print("Cannot deposit negative amount.")
                        continue
                    choices["Balance"]+= deposit_amount

                    transaction = {
                        "type": "deposit",
                        "amount": deposit_amount,
                        "balance": choices["Balance"]

                    }
                    choices["History"].append(transaction)
                    print(f"New Balance: ${choices['Balance']:,.2f}")


                elif choice == "2":
            
                    withdraw_amount = float(input("Enter amount to withdraw: "))
                    if withdraw_amount > choices["Balance"]:
                        print("Cannot overdraft, please try again.")
                        continue
                    choices["Balance"]-= withdraw_amount

                    transaction = {
                        "type": "withdraw",
                        "amount": withdraw_amount,
                        "balance": choices["Balance"]

                    }
                    choices["History"].append(transaction)
                    print(f'New Balance: ${choices["Balance"]:,.2f}')


                       
 
                elif choice == "4":
                    for t in choices["History"]:
                        print(f"{t['type']} of ${t['amount']} Balance: ${t['balance']}")
                    continue
                elif choice == "3":
                    return
        else:
            retries -= 1
            print(f"Incorrect PIN, you have {retries} left")
    if retries == 0:
        choices["Locked"] = True
        print("Retries used up, returning to menu...")
        return
    





loop = True
while loop:
    print("==PYTHON BANK==")
    for menu_id, data in menu.items():
        print(f"{menu_id}. {data['Account']}")
    try:
        choice = int(input("Please select an option(1-4): "))
    except ValueError:
        print("Invalid input.")
        continue

    if choice == 4:
        print("Thank you for operating with us.")
        loop = False
    elif choice in menu:
        actions(choice)
    else:
        print("Invalid input.")

        