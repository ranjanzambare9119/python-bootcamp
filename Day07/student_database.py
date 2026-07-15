print('==========')
print('Student Database')
print('==========')
students = []

while True:
    print("\n--- Student Database Menu ---")
    print("1 Add Student")
    print("2 Remove Student")
    print("3 Display Students")
    print("4 Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        name = input("Enter student name to add: ")
        students.append(name)
        print(f"'{name}' has been added.")
        
    elif choice == '2':
        name = input("Enter student name to remove: ")
        if name in students:
            students.remove(name)
            print(f"'{name}' has been removed.")
        else:
            print(f"'{name}' not found in the database.")
            
    elif choice == '3':
        print("\n--- Student List ---")
        if students:
            for idx, student in enumerate(students, 1):
                print(f"{idx}. {student}")
        else:
            print("The database is currently empty.")
            
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
    
