############################################################
#
# From MIT 6.0001 course 2016
# Search for a value using bisection search
#
############################################################


def bisection_search(t, e):
    """
    :param t: The value we want to find the cube root of
    :type t: float
    :param e: The epsilon value within which to accept the answer
    :param e: float
    :return: The cube root of t
    :rtype: float
    """

    try:
        # print(target, epsilon)
        target = float(t)
        epsilon = float(e)
    except (TypeError, ValueError):
        
    #    raise AssertionError('*** wrong input type to function bisection_search() ***')

    ans = 0
    low = ans
    high = abs(target ** 3)
    guesses = 0

    while abs(ans**3 - target) >= epsilon:      # use abs to prevent comparing negative number
        if ans**3 > target:
            high = ans

        if ans**3 < target:
            low = ans
        ans = (low + high) / 2                  # remember to actually change the search area!
        guesses += 1

    print('Took', guesses, 'guesses')
    return ans


target = input("enter an integer whose cube root you wish to find:  ")
epsilon = input("enter the epsilon value for the cube search:  ")

print("The cube root of", target, "is", bisection_search(target, epsilon))
