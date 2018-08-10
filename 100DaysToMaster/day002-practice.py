# find all numbers between 2000 and 3200, divisable by 7 but NOT multiple of 5
# solution should be comma separated on a single line

num = []

for i in range(2000, 2301):
    if (i % 7 == 0) and (i % 5 != 0):
        num.append(str(i))

print(','.join(num))


# compute the factorial of a given number, result printed in csv single line
# factorial is the integer product of a number and all the numbers below it
# e.g. 4! is 4 * 3 * 2 * 1


def factorial(base, exp):
    if exp == 0:
        return 1
    return base * factorial(base, exp - 1)

seq = []
for i in range(1, 9):
    seq.append(factorial(i, 2))

print(tuple(seq))


