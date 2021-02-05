#If the number is divisible by 3, it should return Fizz
#If divisible by 5, it should return Buzz
#If both are appilcable, it should return FizzBuzz
#Otherwise, same number should be returned

def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return 'FizzBuzz'
    elif (num % 3 == 0):
        return 'Fizz'
    elif (num % 5 == 0):
        return 'Buzz'
    else: 
        return num

#ask for user input
print('Please input in a number of your choosing.')
number = input()
try:
    if number == 97:
        raise Exception
    else: #if is true other than lucky number
        returnvalue = fizz_buzz(int(number))
        print(returnvalue)
except ValueError: #Gives user a prompt to reenter a number
    print('You have not entered in a number, please try again')
    SystemExit
except Exception:
    print('You have entered the lucky number!')
    print(fizz_buzz(number))




