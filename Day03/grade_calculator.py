# Program: Voting Eligibility Checker
# Author: Ranjan Zambare
# Day: 03
marks= int(input('Enter your marks:'))
print('==========')
print('Grade calculator')
print('==========')
if marks>= 90:
    print('You have obtained grade A')
elif marks>= 75:
    print('You have obtained grade B')
elif marks>= 50:
    print('You have obtained grade C')
else:
    print('You have failed in the exam')
