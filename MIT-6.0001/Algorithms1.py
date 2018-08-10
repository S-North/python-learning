############################################################
#
# From MIT 6.0001 course 2016
# Cube root algorithms
#
############################################################

Cube = 863436543245678
Epsilon = 0.0001
Low = 0.0
High = Cube
Guess = (Low + High) / 2.0
Num_Guesses = 0

while abs(Guess**3 - Cube) >= Epsilon:
        if Guess**3 < Cube:
            Low = Guess
        else:
            High = Guess
        Guess = (Low + High) / 2.0
        Num_Guesses += 1

print("num guesses =", Num_Guesses)
print("Guess is close to the value", Guess)


