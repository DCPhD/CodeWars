#Build Tower by the following given argument:
#number of floors (integer and always greater than 0).
# tower of 3 floors:
'''
[
  '  *  ',
  ' *** ',
  '*****'
]
'''

number = -1
Range = int(input("how many layers do you want the tree?"))
for x in range(Range):
    number = number + 2
    print(" " * (Range - x), "+" * number)


# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number


def create_phone_number():
    n = int(input("Enter a series of 10 digits, from 0-9")) # receive input from user as integer
    tempNumber = [] # blank variable to call later
    n = str(n) # switch integer to string as output
    length = len(n) # generate variable for length to be used next
    if length != 10:
        print("Please provide 10 digits between 0-9") # if user does not input correctly

    for num in n:  # iterate through variable n (input)
        tempNumber.append(num) # create variable to append parens and -

    tempNumber.insert(0, "(")
    tempNumber.insert(4, ")")
    tempNumber.insert(8, "-")
    n = ''.join(tempNumber) # join parens and - to input
    print(n)


create_phone_number()

# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot
# contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.

def validate_pin():

    # receive input from user
    pinNumber = int(input("Please input a series of 4 or 6 digits (0-9)"))
    pinNumber = str(pinNumber)

    # determine if input consists of 4 or 6 numbers
    if len(pinNumber) == 4 or len(pinNumber) == 6 and pinNumber.isdigit():
        return True
    else:
        return False


print(validate_pin())

