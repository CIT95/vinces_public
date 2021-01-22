#User is prompted to input number
#User will input a starting number and an ending number
#starting number < ending number, print should give range between numbers
while True:
    print('Please input a starting number (Integers only)') #number 1
    startingnumber = int(input())

    print('Please input an ending number (Integers only)') #number 2
    endingnumber = int(input())

    if startingnumber < endingnumber: #Range should be printed from starting to ending number
        for num in range(startingnumber, endingnumber +1):
            print(num)
    else: 
        print('Please try again') #loop back to start if ending is not > than starting
        continue
    print('Do you wish to find another interval? Enter Y for yes, N for no.')
    reset = input()
    if reset == 'Y':
        continue #loop back to start with Y
    elif reset == 'N':
        break #breaks loop with N
    else: 
        print('Incorrect input, thank you for trying!')#program should close after
        exit()

print('Have a nice day!')