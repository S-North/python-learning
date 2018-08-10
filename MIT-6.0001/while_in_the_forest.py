#################################################################
#
# From MIT 6.0001 course 2016
# while loops
# try and except, error handling
# also some basic arrays and the in/not in operator
#
#################################################################

DistanceRight = 0                                               # declare the counter
n = "right"                                                     # initialise the input variable

# define the input controls
PermittedCommands = ["right","r","left","l","4df8fbcf-d66d-4b5c-b0b8-9e8c249dc923"]
RightCommands = ["right","r"]
LeftCommands = ["left","l"]

while DistanceRight >= 0 or (n == "right" or n == "Right"):     # keep looping as long as user
                                                                # keeps going right, or right counter is incremented
    # DEBUGGING   print("n =",n,"\nDistanceRight =", DistanceRight)

    try:                                                        # message displayed every 4th right
        if DistanceRight > 1 and DistanceRight% 4 == 0 and n in RightCommands:
            print("Aaaargh!\n(╯°□°）╯︵ ┻━┻")
    except type:
        break

    n = input(
          "\nYou are in the lost forest\n\n"                    # The optional prompt text can be broken
                                                                # over several lines to make it more readable
                                                                # but its the \n that signifies a new line.
          
          "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
          "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n"
          "     :[\n\n"
          "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
          "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n"
          "Turn left or right?   ")
    n = n.lower()                                               # convert the input string to lowercase

    if n in PermittedCommands:                                  # check the input for permitted options

        if n in RightCommands:
            DistanceRight += 1                                  # increase counter if input right
            print("\n" * 100)                                   # clear the screen

        elif n in LeftCommands:
            DistanceRight -= 1                                  # decrease counter if input left
            print("\n" * 100)                                   # clear the screen

    else:                                                       # restart loop if input is not permitted option
        print("\n" * 100)  # clear the screen
        print("\n*** You Can't Go In That Direction ***")
        n = "4df8fbcf-d66d-4b5c-b0b8-9e8c249dc923"

else:                                                           # end the program
    print("\n" * 100)                                           # clear the screen
    print("\nYou have escaped the forest\n\n"
          "XXXXXXX\nXXXXXXX\n"
          "XXXXXXX\nXXXXXXX\n"
          "                yippee!\n"
          "           \o/ \n\n"
          "XXXXXXX\nXXXXXXX\n"
          "XXXXXXX\nXXXXXXX\n" )
