#compute the factorial of a given number, result printed in csv lingle line
#factorial is the integer product of a number and all the numbers below it
# e.g. 4! 4*3*2*1 = 24


def factorial(num):

    if num == 0:
        return 1
    return num * factorial(num-1)



print("Enter an integer...")
num = int(input())
print(factorial(num))




