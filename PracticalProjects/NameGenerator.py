####################################################
##
##  Projects suggested by CupOfCode01
##  Name Generator using random, string
##
####################################################

import random, string, pprint, sys

#### quick create random string lowercase ascii of user selectable length
# length = input("how many letters?")
# name = ""
# for i in range(int(length)):
#     name += random.choice(string.ascii_lowercase)
# print(name)
#
#
# #### generate variable number of names where user can select vowels and consonants
# def generator(length):
#
#     vowel = "aeiou"
#     cons = "bcdfghjklmnpqrstvwxyz"
#     name = ""
#
#     while length > 0:
#         type = input("Do you want a vowel or a consonant? (v, c)")
#         if type == "v":
#             choice = random.choice(vowel)
#             print("you got", choice)
#             name += choice
#             length -= 1
#         elif type == "c":
#             choice = random.choice(cons)
#             print("you got", choice)
#             name += choice
#             length -= 1
#         else:
#             print("That's not a letter. Please try again")
#     return name
#
#
# length = input("How long a name do you want:  ")
# name = generator(int(length))
#
# print("\nThe name you generated is", name.capitalize())
#
#
# #### user can select number of names generated and provide a mask for vowels and consonants
# #### e.g. cvvvccv


def nameGen(length, number, mask=""):

    vowel = "aeiou"
    cons = "bcdfghjklmnpqrstvwxyz"
    name = ""
    names = []

    for i in range(int(number)):
        name = ""
        for i in mask:
            if i == "v":
                choice = random.choice(vowel)
                name += choice
            elif i == "c":
                choice = random.choice(cons)
                name += choice
            elif i == "l":
                choice = random.choice(string.ascii_lowercase)
                name += choice
            else:
                name += i
        names.append(name.capitalize())
    return names


while True:
    number = input("How many suggestions do you want?:  ")
    mask = input("Enter a mask where 'c' = consonants, 'v' = vowels, and 'l'= a random letter\ne.g. vcvvclson\n:  ")
    print("\nThis will create", str(number), "names that are", str(len(mask)), "letters long.")
    correct = input("Is this correct?")
    if correct.lower() == "y" or correct.lower() == "yes":
        names = nameGen(len(mask), number, mask)
        pprint.pprint(names)
        #sys.exit()
        print("\nYou can keep generating more names,\nor press CTRL+C to end the program\n")
    else:
        break

#### Generate a 5 letter name where user can specify a letter or v=vowel, c=consonant, l=random letter


# def userinput(length):
#     vowel = "aeiou"
#     cons = "bcdfghjklmnpqrstvwxyz"
#     name = ""
#
#     for i in range(int(length)):
#         print("Chose a letter... \n'v' for vowel, 'c' for consonant, 'l' for any other letter")
#         letter = input()
#         if letter.lower() == "v":
#             letter = random.choice(vowel)
#             name += letter
#         elif letter.lower() == "c":
#             letter = random.choice(cons)
#             name += letter
#         elif letter.lower() == "l":
#             letter = random.choice(string.ascii_lowercase)
#             name += letter
#         else:
#             name += letter
#     return name
#
# length = input("how long a name do you want?\n:")
# print(userinput(length))