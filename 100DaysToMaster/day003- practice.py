# find all numbers between 2000 and 3200, divisible by 7 but NOT multiple of 5
# solution should be comma separated on a single line

num = []
for i in range(2000, 3201):
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


print(factorial(1, 5))
print(factorial(2, 5))
print(factorial(3, 5))
print(factorial(4, 5))
print(factorial(5, 5))


factorials = []
for i in range(1, 11):
    factorials.append(str(factorial(i, 5)))

print(factorials)
print(','.join(factorials))

# given integral number n, create a dictionary with key n, and value is the square of n
# integral is a number assigned to a function


n = int(input())
d = dict()

for i in range(1, n+1):
    d[i] = n**i

print(d)

