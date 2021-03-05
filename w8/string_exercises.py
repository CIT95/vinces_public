#w3resource question 1
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('String length should be 25'))
#I solved this without needing help.

#w3resource question 5
def character_mix(a,b):
    new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(character_mix('abc', 'xyz'))
#I solved this without needing help.

#w3resource question 8
def find_longest_word(words_list):
    word_len[]
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
#I solved this without needing help.

#w3resource question 16
def insert_string_middle(str, word):
    return str(:2) + word + str(2:)

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))
#I solved this without needing help.

#w3resource question 17
def insert_end(str):
	sub_str = str[-2:]
	return sub_str * 4

print(insert_end('Python'))
print(insert_end('Exercises'))
#I solved this without needing help.

#pynative question 2
def appendMiddle(s1, s2):
  middleIndex = int(len(s1) /2)
  print("Original Strings are", s1, s2)
  middleThree = s1[:middleIndex:]+ s2 +s1[middleIndex:]
  print("After appending new string in middle", middleThree)
  
appendMiddle("Ault", "Kelly")
#I solved this without needing help.

#pynative question 5
def count_digit_char_symbol(inputstring):
    charCount = 0
    digitCount = 0
    symbolCount = 0
    for index in string:
        if index isupper() or islower():
            charCount+=1
    elif char.isnumeric():
      digitCount+=1
    else:
      symbolCount+=1
    print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)
inputString = "P@#yn26at^&i5ve"
print("total counts of chars, digits,and symbols \n")
count_digit_char_symbol(inputstring)      
#I was able to solve this without needing help.

#pynative question 8
inputString = "Welcome to USA. usa awesome, isn't it?"
substring = "USA"
tempString = inputString.lower()
count = tempString.count(substring.lower())
print("The USA count is:", count)
#I was able to solve this without needing help.

#pynative question 11
str1 = "PYnative"
print('The original string is: ', str1)

str1 = str1[::-1]
print('The reverse string is: ', str1)
#I solved this without needing help.

#pynative question 14
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print('This is the original list string.')
print(str_list)

new_str_list = list(filter(None, str_list))
print('After removing the empty strings in the list, this is what comes out.')
print(new_str_list)
#I solved this without needing help.