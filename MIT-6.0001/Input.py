#################################################################
#
# From MIT 6.0001 course 2016
# simple string input and printout. All input is default a string
#
#################################################################

print("Enter anything...")
UserInputTxt = input()

# use commas to mix types and automatically add a space. use + operator to explicitly add spaces
print("You typed", UserInputTxt)

# Cast the input as an integer
print("Enter a number...")
UserInputTxt = int(input())

# include operations that work with integers. The integer is cast to a str. entering a string will throw a type error
print("Your number multiplied by 3 is" + " " + str(UserInputTxt*3))
