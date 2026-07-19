print('==========')
print('Restaurant Menu')
print('==========')
menu = {
    "Paneer Butter Masala":250,
    "Veg Biryani":180,
    "Cold Coffee":120,
    "Masala Dosa":90}

while True:
    print('1 Show Menu')
    print('2 Add Dish')
    print('3 Upadate Price')
    print('4 Remove Dish')
    print('Exit')
    choice = input('Enter your choice:').strip()
    if choice== '1':
        for key, value in menu.items():
            print(key, ':', value)
    elif choice== '2':
        
        new_dish = input("Enter the name of the new dish: ").strip()
        if new_dish in menu:
            print("This dish already exists! Use Option 3 to change its price.")
        else:
            new_price = int(input(f"Enter price for {new_dish}: ₹"))
            menu[new_dish] = new_price
            print(f"'{new_dish}' successfully added to the menu.")
            
    elif choice == "3":
       
        dish_to_update = input("Enter the dish name to update: ").strip()
        if dish_to_update in menu:
            updated_price = int(input(f"Enter new price for {dish_to_update}: ₹"))
            menu[dish_to_update] = updated_price
            print(f"Price for '{dish_to_update}' updated successfully.")
        else:
            print("Dish not found in the menu.")
            
    elif choice == "4":
      
        dish_to_remove = input("Enter the dish name to remove: ").strip()
        if dish_to_remove in menu:
            menu.pop(dish_to_remove)
            print(f"'{dish_to_remove}' removed from the menu.")
        else:
            print("Dish not found in the menu.")
            
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please choose a number from 1 to 5.")
