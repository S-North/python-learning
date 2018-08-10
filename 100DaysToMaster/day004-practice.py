# find all numbers between 2000 and 3200, divisible by 7 but NOT multiple of 5
# solution should be comma separated on a single line

list = ''
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 5):
        list = list + (str(i) + ',')        # remembered different this time round, built the string in the loop
        #                                     rather than building a list, then joining the list in the print()
        #                                     maybe the list method is better as the list can be reused
print(list)

list = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 5):
        list.append(str(i))                 # with the list.append method

print(','.join(list))                       # joining in the print()

# compute the factorial of a given number, result printed in csv single line
# factorial is the integer product of a number and all the numbers below it
# e.g. 4! is 4 * 3 * 2 * 1


def factor(base, exp):
    if exp == 0:
        return 1
    return base * factor(base, exp - 1)

list = []
for i in range(1, 129):
    list.append(str(factor(2, i)))

print(','.join(list))


# given integral number n, create a dictionary with key n, and value is the square of n
# integral is a number assigned to a function

n = int(input('enter an integer:  '))
d = dict()

for i in range(1, n+1):
    d[i] = i*i

print(d)


# for a given input of comma separated numbers, store each number in a list element
# convert the list into a tuple, then print the list and the tuple
# note the different way they are expressed

values = input('enter some comma separated values:')
list = values.split(',')
t = tuple(list)

print(t)




