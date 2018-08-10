# given integral number n, create a dictionary with key n, and value is the square of n
# integral is a number assigned to a function

import pprint

print('Enter an integer:')

n = int(input())
d = dict()

for i in range(1, n+1):
    d[i] = 2**i

print(d)
pprint.pprint(d)

dict_list = list(d.items())
print(dict_list)


# try updating dictionary values
d[45] = 'firstvalue'
print(d[45])
# print(type(d))
