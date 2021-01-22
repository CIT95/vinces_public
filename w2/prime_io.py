#user is prompted to input number
#user will input starting number and ending number
#starting number < ending number, print should give range of prime numbers in between numbers
while True:
    print('Please input a starting number (Integers only)') #number 1
    startingnumber = int(input())

    print('Please input an ending number (Integers only)') #number 2
    endingnumber = int(input())
    
    if startingnumber < endingnumber: #Range should be printed from startingnumber to endingnumber
        for num in range(startingnumber, endingnumber):
            if num > 1:
                for i in range(2,num):
                    if(num % i) == 0:
                        break #this will avoid the else statement and bring us back around
                    else: #else activates for prime numbers 
                        print(num) 
    else:
        print('Please try again') #This should restart the loop
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