# #find all numbers between 2000 and 3200, divisable by 7 but NOT multiple of 5
# #solution should be comma separated on a single line

empty_list = []

#iterate through the rangeof numbers

for i in range(2000, 3201):
    #if (i%7 == 0) and (i%5 != 0):          #use modulo to find the divisables
    if (i % 7 == 0) and not (i % 5 == 0):   #put the conditions into brackets, otherwise unpredictable
        empty_list.append(str(i))           #add items to the list as strings

print(','.join(empty_list))                 #use the string join method to create the format requested


empty_list = []

for i in range(10000, 100, -2):             #diferent range options
    if (i%3 == 0) and (i%7 != 0):
        empty_list.append(str(i))

print(', '.join(empty_list))                #alter the join character


def findModulo(r1, r2, r3=1):               #put it in a function

    empty_list = []
    for i in range(r1, r2, r3):             # diferent range options

        if (i % 4 == 0) and (i % 9 != 0):
            empty_list.append(str(i))

    return empty_list


print(', '.join(findModulo(3, 4000)))
