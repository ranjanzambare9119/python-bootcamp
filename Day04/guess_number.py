secret_num = 8
while True:
    guess= int(input('Guess the number:'))
    if guess== secret_num:
        print('Congratulations you guesed it right')
        break
    else:
        print('Try again')
