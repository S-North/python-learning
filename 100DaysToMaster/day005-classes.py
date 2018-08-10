# create a class that has 2 methods
# 1. getString: grabs string from input
# 2. printString: print that string in uppercase


class mama(object):
    def __init__(self):
        self.s = ''

    def __getString__(self):
        self.s = input('Give me a string:')

    def __printString__(self):
        print(self.s.upper())

    def __repeat__(self, num):
        t = ''
        for i in range(num):
            t = t + self.s + ', '
        self.s = t


x = mama()
print(x)
x.__getString__()
x.__printString__()
x.__repeat__(10)
x.__printString__()
print(x.__as_list__())