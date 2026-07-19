print('==========')
print('String Slicing')
print('==========')
word= input('Enter any word:')
print(f'First 4 characters are {word[0:4]}')
print(f'Last 3 characters are {word[-3:]}')
length= len(word)
if length > 7:
    print(f'Middle characters are {word[4:-3]}')
else:
    print('Word is too short')
