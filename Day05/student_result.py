def calculate_total(s1, s2, s3, s4, s5):
    return s1+s2+s3+s4+s5
def calculate_percentage(total):
    return (total/500)*100
def display_grade(grade):
    if grade>=90:
        return 'A'
    elif grade>=75:
        return 'B'
    elif grade>=50:
        return 'C'
    else:
        return 'Fail'
print('==========')
print('Student Marks Calculator')
print('==========')
s1= int(input('Enter marks for subject 1:'))
s2= int(input('Enter marks for subject 2:'))
s3= int(input('Enter marks for subject 3:'))
s4= int(input('Enter marks for subject 4:'))
s5= int(input('Enter marks for subject 5:'))
total_marks= calculate_total(s1, s2, s3, s4, s5)
print('Total Marks Obtained:', total_marks)
percentage= calculate_percentage(total_marks)
print('Percentage obtained:', percentage)
grade= display_grade(percentage)
print('Grade:',grade)
