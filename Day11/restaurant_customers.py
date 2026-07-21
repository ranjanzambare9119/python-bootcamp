# Initialize an empty set to store unique customer names
customers = set()

while True:
    print("\n========== Customer Tracker ==========")
    print("1 Add Customer")
    print("2 Remove Customer")
    print("3 Show Customers")
    print("4 Exit")
    print("======================================")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        name = input("Enter customer name: ").strip().title()
        
        # Check if the customer is already in the set
        if name in customers:
            print(f"'{name}' is already registered (Duplicates are not allowed).")
        else:
            # Use .add() to append to the set
            customers.add(name)
            print(f"Customer '{name}' added successfully.")
            
    elif choice == "2":
        name = input("Enter customer name to remove: ").strip().title()
        
        if name in customers:
            # Use .discard() to safely remove the item
            customers.discard(name)
            print(f"Customer '{name}' removed successfully.")
        else:
            print(f"Customer '{name}' was not found in the list.")
            
    elif choice == "3":
        if customers:
            print("\n--- Current Customers ---")
            # Loop through and print each name in the set
            for idx, name in enumerate(customers, 1):
                print(f"{idx}. {name}")
        else:
            print("No customers in the system yet.")
            
    elif choice == "4":
        print("Exiting customer system. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select a number from 1 to 4.")
