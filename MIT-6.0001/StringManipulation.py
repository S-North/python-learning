############################################################
#
# From MIT 6.0001 course 2016
# Strings and manipulation
#
#
############################################################

# functions
s = "abcdefghijklmnopqrstuvwxyz"
print(len(s))                   # len() evaluates the length of the string i.e. 26

# indexes
print(s[2])                     # gets the letter at index 2. Indexes start at 0. so this will be the 3rd letter
print(s[-1])                    # index from the tail of the string, starting at -1 then -2, -3, etc
print(s[5:20])                  # index start:end:interval
print(s[5:20:2])                # example with intervals
print(s[::])                    # all default. equivalent to s[0:len(s):1]
print(s[::-1])                  # counts back from reverse index. equivalent to s[-1:-len(s)+1:-1]
print(s[4:1:-2])                # count back in 2s from index 4 to 1

for index in range(len(s)):                                 # making the range the length of the string
    if s.lower()[index] == "b" or s[index] == "y":          # using the iterative index var to check each string index
        print("There's a B or Y in this string")            # print the result

for char in s:                                              # variable char is given the value of each letter of s
    if char.lower() == "z":                                 # char can then be tested directly
        print("There's a Z in this string")
    else:
        print("There's no Z in this string")

# ROBOT Cheerleaders

an_letters = "aefhilmnorsx"
word = input("I will cheer for you! Give me a word:  ")
times = int(input("Enthusiasm Level (1-10):  "))

#i = 0
#while i < len(word):
for char in word:
#    char = word[i]
    if char in an_letters:
        print("Give me an " + char.lower() + "! ", char.capitalize() + "!!!")
    else:
        print("Give me a  " + char.lower() + "! ", char.capitalize() + "!!!")
#    i += 1

print("What does that spell?")
for i in range(times):
    print(word.upper() + "!!!")
