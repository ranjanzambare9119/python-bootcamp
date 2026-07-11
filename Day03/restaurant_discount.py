# Program: Voting Eligibility Checker
# Author: Ranjan Zambare
# Day: 03
bill_amount= int(input('Enter the bill amount:'))
print('==========')
print('Restaurant Discount Calculator')
print('==========')
if bill_amount> 1000:
    discount_percent= 10
elif bill_amount >500:
    discount_percent=5
else:
    discount_percent=0
discount_amount= bill_amount * (discount_percent/100)
final_bill= bill_amount - discount_amount
print('Bill Amount:', bill_amount)
print('Discount Percentage:', discount_percent)
print('FInal Bill:', final_bill)
