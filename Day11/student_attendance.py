class_A={"Ranjan","Akash","Rohit","Sneha"}
class_B= {"Sneha","Akash","Rahul","Pooja"}
print('-----Student Attendance-----')
print(f'Union of Students: {class_A.union(class_B)}')
print(f'Intersection of Students: {class_A.intersection(class_B)}')
print(f'Only Class A students: {class_A.difference(class_B)}')
print(f'Only Class B students: {class_B.difference(class_A)}')
