print('==========')
print('Membership')
print('==========')
languages = {"Python","Java","SQL"}
language= input('Enter language to search:')
if language in languages:
    print('Language Found')
else:
    print('Language not found')
