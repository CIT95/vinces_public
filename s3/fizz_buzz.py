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

returnvalue = fizz_buzz(int(number))
print(returnvalue)