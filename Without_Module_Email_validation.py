
input  = input('Enter your email: ')


if len(input) >= 6: # check length
    if input[0].isalpha(): # Check first letter if alphabet
        if "@" in input and input.count('@') == 1: # check @ in email and only one @ in email
            if (input[-4] == '.') ^ (input[-3] == '.'): # check dot in email last
                if ' ' not in input: # check if any space in email
                    email = input.lower() # convert email into lower case
                    print(email)
                else:
                    print('Email not valid, do not use space in email')
            else:
                print('Email not valid, cannot find dot in last')
        else:
            print('Email not valid, @ is required or use only one @ in email')
    else:
        print('Email not valid, First letter will be Alphabet')
else:
    print('Email not valid, minimum 6 characters required')
