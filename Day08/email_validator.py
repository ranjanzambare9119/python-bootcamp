print('==========')
print('Email Validator')
print('==========')
email= input('Enter your email:')
if '@' in email and '.' in email:
    print('Valid email format')
else:
    print('Invalid email format')
