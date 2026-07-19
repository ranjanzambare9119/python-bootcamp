student = {}
while True:
    print("\n========== Menu ==========")
    print("1 Add Student Details")
    print("2 Update Age")
    print("3 Display Student")
    print("4 Exit")
    print("==========================")   
    choice = input("Enter your choice: ").strip()   
    if choice == "1":
        student['name'] = input("Enter Name: ")
        student['age'] = int(input("Enter Age: "))
        student['branch'] = input("Enter Branch: ")
        student['college'] = input("Enter College: ")
        print("Details added successfully!")       
    elif choice == "2":
        if 'age' in student:
            new_age = int(input("Enter new age: "))
            student['age'] = new_age
            print("Age updated successfully!")
        else:
            print("Error: No student details found. Use option 1 first.")     
    elif choice == "3":
        if student:
            print("\n--- Student Details ---")
            print(f"Name:    {student['name']}")
            print(f"Age:     {student['age']}")
            print(f"Branch:  {student['branch']}")
            print(f"College: {student['college']}")
        else:
            print("No student record to display.")
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
