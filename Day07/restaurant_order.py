print('==========')
print('Restaurant Order')
print('==========')
orders = []

while True:
    print("\n--- Restaurant Order Menu ---")
    print("1 Add Order")
    print("2 Cancel Last Order")
    print("3 Show Orders")
    print("4 Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        item = input("Enter the dish name to order: ")
        orders.append(item)
        print(f"'{item}' added to your order.")
        
    elif choice == '2':
        if orders:
            removed_item = orders.pop()
            print(f"Cancelled last order: '{removed_item}'")
        else:
            print("No active orders to cancel.")
            
    elif choice == '3':
        print("\n--- Current Orders ---")
        if orders:
            for idx, item in enumerate(orders, 1):
                print(f"{idx}. {item}")
        else:
            print("No active orders.")
            
    elif choice == '4':
        print("Thank you! Exiting order system.")
        break
        
    else:
        print("Invalid choice! Please choose between 1 and 4.")
