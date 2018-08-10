############################################################
#
# From MIT 6.0001 course 2016
# Introduction to functions
#
############################################################


def is_even(number):                                        # this is a function
    """
    :param number: is a positive integer
    :type number: int
    :return: True if an even number, False if odd
    :rtype: int
    """
    return number % 2 == 0                                  # returns the boolean value generated here


x = input("Enter a whole number:   ")
print(is_even(int(x)))


def is_even_without_return(integer):                        # another function
    """
    :param integer: is a positive integer
    :type integer: int
    :rtype None
    """
    i = integer * 12
    print("internal state of variable =", i)
    print("If you don't specify a return in the function, Python automatically adds 'return None'")
    # notice there's no return statement


x = input("Enter a whole number:   ")
print(is_even_without_return(int(x)))
# because there is no return statement in the function
# The return value is set to None

print("all numbers between 0 and 20: even or odd")
for i in range(20):
    if is_even(i):                                          # use the function
        print(i, "even")
    else:
        print(i, "odd")

print("Even numbers")
for i in range(20):
    if is_even(i):                                          # use the function again
        print("", i)
print("Odd numbers")
for i in range(20):
    if not is_even(i):
        print("", i)

# global and local scopes


def function_a (variable):
    local_var = variable**2
    print("inside function_a")
    return local_var                                        # uses the local variable


def function_b (variable):
    print("inside function_b")
    return global_a * variable                              # variable not defined in local scope so uses global


global_a = 100
print(function_a(10))
print(function_b(1))