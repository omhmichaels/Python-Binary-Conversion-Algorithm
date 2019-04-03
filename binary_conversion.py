
"""
#
# Title: Python Binary Converter
# Author: Somhmxxgh0u1
# Description: Use python to figure out the value of a binary number. Uncomment or comment print statements
  for debugging.You can do this all at once by using search and replace. Search "#print" and replace with "print" and 
  and vice versa. Cool little way to do conversion with the material learned in class.
"""




# Variable to hold user input of binary number as a string
BINARY_NUMBER = ""

# Answer Variable as an int
answer = 0

# Introduction function created to prompt the user for input. 
def intro():
    print("Helllo there bud, I see you got a binary number to convert...\n\n")
    print("Please enter a binary number.\nExample: 0000\n\n")


# Function to gather user input of Binary number as a string. Python is capable of conversion 
# of the string BINARY_NUMBER into a integer by using int(BINARY_NUMBER). 
def get_binary_number():
    global BINARY_NUMBER
    # Use global statement to be able to change the value of BINARY_NUMBER globally. This means
    # That it will hold the same value assigned to it below outside of this function.
    BINARY_NUMBER = input()
    print("This is BINARY_NUMBER value inside the get_binary_number function", BINARY_NUMBER)    
 
# binary_value parameter is the bits binary value 1 or 0
# nth_number_bit is the distance of the bit from the start at the right
# return bit_numerical_value returns the numerical value of that bit.
def binary_conversion(binary_value, nth_number_bit):
    # Takes a binary_value and raises it to the power of nth_number_bit starting from the right
    # Example first bit is binary_value**0 Second is binary_value**1 and so on
    print("This is the value and position of the current bit being processed\n")
    print("The value of BIT is: ", binary_value, "\n")
    print("The value of NTH is : ", nth_number_bit, "\n")
    print("Now determining the NTH BIT value.")
    # Evaluation to determine if the bit is the first bit. This is because every value after this needs to be 
    # multiplied by 2 before it is raised to the nth power. This is the on value of the second bit wich
    #  is subsequently doubled for each nth bit to the left
    if (nth_number_bit == 0):
        return binary_value**nth_number_bit
    else:
        binary_value *= 2
        return binary_value**nth_number_bit
    # **CHALLENGE** 
    # Use alternate arithmetic for this portion





# Now we right the main portion of our program to iterate over the binary_conversion function

# Greet application user
intro()

# Gather user input of a 4 bit binary number
get_binary_number()


# Check to see if it retains its value outside of function
print("Value of BINARY_NUMBER outside of the function is", BINARY_NUMBER)
print("\n")


# NOTE: The way i wrote this function uses a global variable to allow the BINARY_NUMBER to retain the value
#       i had changed it to outside of the function where the change was made. Another way to do this is to 
#       specify a return value for the function like we do with our binary_conversion function. Pay attention to the
#       format and differences in the following loop.






print("The length of the Binary number is :", len(BINARY_NUMBER))
#counter = 0
counter2 = 0
"""
CAUTION:
    This was my original idea for the process. It was repeating the nested for loops arithmetic twice however.
Turns out easier alternative is to start the NTH variable outside the loop and increment it at the end
of each iteration

for NTH in range(len(BINARY_NUMBER)):
    print("FIRST LOOP ITERATION # ", str(counter))
    counter += 1
    # This for loop gathers the length of our users input binary string and returns it as
    # an integer. We can now use NTH along with bits syncroniously. Ex: BIT**0, BIT**1.. and so on. Only now it looks
    # like BIT**NTH, BIT**NTH
    # Now we loop through our bits. This is only possible because we took the user input as a string and there values
    # can be accessed with indexing. Ex: greeting = "hello" 
    # print(greeting[0])
    # This would output: h 
"""

NTH = 0
for BIT in reversed(BINARY_NUMBER):
        print("SECOND LOOP ITERATION # ", counter2, "\n\n")
        # the reversed() allows us to start iterating from the right hand side of our list
        # Use pythons int() to convert the string "1" to the int 1 for use in our binary_conversion()
        BIT = int(BIT)
        #print("BIT is now an integer and ready for processing: ", BIT)
        print("\n\n____________________")
       
        # Now we use our binary_conversion functions return value of bit_actual_value to udate our
        #  answer through each iteration of the our for loops. 
        actual_bit_value = binary_conversion(BIT, NTH)
        print("The actual value of the BIT**NTH is :", str(actual_bit_value), "\n")

        # Now we set our answer variable to be incremented each iteration by the value of actual_bit_value
        answer += actual_bit_value
        NTH += 1
        #counter2 += 1

    

    #print("_______________\nEND SECOND LOOP\n\n")
print("______________________\nEND FIRST LOOP\n\n")
print("We have finished the conversion\n\n______________\n\n")
print("The binary number", BINARY_NUMBER, "has the actual value of: ", str(answer))


        
        

    

    


