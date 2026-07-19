print('==========')
print('Password Security Check')
print('==========')
password= input('Enter your password:')
length= len(password) >= 8
digit= False
uppercase= False
for char in password:
    if char.isdigit():
        digit= True
    if char.isupper():
        uppercase= True
if length and digit and uppercase:
    print('Strong Password')
else:
    print('Weak Password')
