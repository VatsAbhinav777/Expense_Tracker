expenses = [] 

def add_expense():
     amount=float(input("Enter amount spent: ")) 
     description=input("Enter brief description: ")
    
     expenses.append((amount, description))
     print("\n      Expense Added")

def view_summary():
    if len(expenses) == 0:
        print("\n   No Expenses Recorded.")
        return
    
    print("\n   EXPENSES SUMMARY")
    total = 0
    

    for amount, description in expenses:
        print(f"₹{amount}\t        {description}")
        total+=amount
    
    
    print(f"TOTAL SPENT: ₹",total)

while True:
    print("\n\n      MENU\n ")
    choice = int(input("1. Add Expense\n2. View Expense\n3. EXIT\n\nEnter option: "))

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_summary()

    elif choice == 3:
        print("\n      Tracker Closed.")
        break
    
    else:
        print("\n      Invalid Option.")
