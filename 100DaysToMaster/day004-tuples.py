# tuples are like lists, but they are immutable. whereas lists are mutable
# for a given input of comma separated numbers, store each number in a list element
# convert the list into a tuple, then print the list and the tuple
# note the different way they are expressed

values = input('give me some comma seperated values')
list = values.split(',')                # .split & .join are string methods
tuple = tuple(list)

print(tuple, list)
