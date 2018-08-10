#################################################################
#
# From MIT 6.0001 course 2016
# if, elif and else branches
# conditions, semicolon, indent 4 characters
#
#################################################################

Continue = False
Input = 0

print("\n" * 100)                                               # clear the screen

#x = int(input())                                               # get a number. not testing if its an integer
                                                                # this is likely to crash if in integer is not entered
while Continue is False:

    Input = (input("\nPlease enter a number:  "))
    try:                                                        # try to cast it to an integer
        Input = int(Input)
    except type:                                                     # if an error occurs, let the user know
        print("\n"*100)
        print("That's not a whole number, please try again.")

    if type(Input) is int:
        print("\n" * 100)                                       # clear the screen
        print(Input, "is an integer")
        Continue = True                                         # set the Continue flag only if the input was in integer

if Input > 50:                                                  # check the values of Input and print text based
    print("and its greater than 50")                            # on the condition test results
elif Input == 50:
    print("and its equal to 50")
else:
    print("and its less than 50")

print("\n\n")
input("Press ENTER to continue...")
print("\n" * 100)                                               # clear the screen


#################################################################
# for loops
# ###############################################################

for i in range(10):                                             # defaults, start=0, interval=1
    print(i)                                                    # this will print 0-9

RangeStart = int(input("Enter a starting number:  "))           # prompt for the range values
RangeEnd = int(input("Enter a ending number:  "))
RangeInterval = int(input("Enter an interval:  "))

for i in range(RangeStart, RangeEnd, RangeInterval):              # loop and print the values in the range
    print(i)

# code to print binary numbers
x = 2
PowerOf = int(input("I'm going to print out the values of binary digits. How many powers would you like me to list?  "))
for i in range(1, PowerOf):
    print(x, "to the power of", i, "is ", x**i)
