menu = {
    1: {"Account": "User1", "Balance": "X", "Action": "X, Y", "History": "X"},
    2: {"Account": "User2", "Balance": "X", "Action": "X, Y", "History": "X"},
    3: {"Account": "User3", "Balance": "X", "Action": "X, Y", "History": "X"}
}


def actions(menu_id):
    choices = menu[menu_id]

    print(f"You currently have: {choices['Balance']}")
    print("Would you like to return to the main menu?(Y/N)")
    if input == "Y":
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

        