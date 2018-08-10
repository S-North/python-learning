##################################
#
# brain melting recursion examples
#
##################################



# recursive function for exponents. from 'Stanford CS106B' YouTube
##################################################################


def powers(base, exp):
    if exp == 0:                        # base case; anything to the power of 0 = 1
        return 1
    return base * powers(base, exp - 1)


print(powers(2, 3))

# e.g. if base = 2 & exp = 4
# exp != 0 so skip the return = 1 and go to recursion;
#
# 2 * powers(exp -1)                                exp = 4
#       2 * powers(exp -1)                          exp = 3
#             2 * powers(exp -1)                    exp = 2
#                   2 * powers(exp -1)              exp = 1
#                         1                         exp = 0     # base case returns 1, no recursion called.
#                                                                 values returned to previous calls
#                   2 * (1) = 2
#             2 * (2) = 4
#       2 * 4 = (8)
# 2 * 8 = 16




# same example from CupOfCode01, questions answered by watching Stanford vid
############################################################################


def recursion(num):
    if num == 0:                        # the base condition. i.e. (num - 1) always reaches 0 where num >= 0
        return 1                        # why does this return value signify to unwind the recursion?
#                                         because when its true, the recursive branch is no longer taken.
#                                         values are then passed back to the function that called it
    return num * recursion(num - 1)     # calling the function each time winds up recursion storing (num - 1)
#                                         unwinding then does num * (num-1) * (num-2) * (num-3) etc


num = int(input('Enter an integer'))
print(recursion(num))




# adding list items. simple version
###################################


def listSum(ls):
    # base condition
    if not ls:
        return 0

#   first element of list + result of calling listSum with rest of elements
    print(ls)
    print(ls[0])
    return ls[0] + listSum(ls[1:])


print(listSum([1, 3, 5, 6, 9, 23]))

# 1st time through, ls[0] = 1       & ls = [1, 3, 5, 6, 9, 23]
# 2nd time through, ls[0] = 3       & ls = [3, 5, 6, 9, 23]
# 3rd time through, ls[0] = 5       & ls = [5, 6, 9, 23]
# 4th time through, ls[0] = 6       & ls = [6, 9, 23]
# 5th time through, ls[0] = 9       & ls = [9, 23]
# 6th time through, ls[0] = 23      & ls = [23]
# 7th time through, ls[0] = None    & ls = None           # This is the base case so returns 0
# 23 + (0) = 23
# 9 + (23) = 32
# 6 + (32) = 38
# 5 + (38) = 43
# 3 + (52) = 46
# 1 + (45) = 47




# adding list items. tail call recursion
########################################


def listSumTail(ls, result):
    if not ls:
        return result
    return listSumTail(ls[1:], result + ls[0])


print(listSumTail([1, 3, 5, 6, 9, 23], 0))
