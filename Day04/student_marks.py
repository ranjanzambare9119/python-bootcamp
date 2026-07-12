subjects= int(input('How many subjects:'))
total_marks=0
for i in range(1, subjects+1):
    marks= float(input(f'Enter the marks for subject {i}:'))
    total_marks += marks
if subjects>0:
    avg_marks= total_marks/subjects
else:
    avg_marks=0
print('==========')
print('Result')
print('==========')
print('Total Marks:', total_marks)
print('Average Marks:', avg_marks)
