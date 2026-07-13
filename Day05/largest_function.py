def largest(a,b):
    if a>b:
        return a
    else:
        return b
print('==========')
print('Largest Number')
print('==========')
a= int(input('Enter a number:'))
b= int(input('Enter another number:'))
largest_number= largest(a,b)
print('Largest number is:', largest_number)
