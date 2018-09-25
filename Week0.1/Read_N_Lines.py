import os


def read_n(filename, n):
    ''' The function takes filename
    and no. of lines to read everytime is called. 
    It returns "n" of lines everytime it is called.'''

    f = open(filename)

    while True:
        output = "".join((f.readline() for i in range(n)))
        if not output:
            break

        yield output


filename = os.path.abspath("test")
for read_1_lines in read_n(filename, 3):
    print(read_1_lines)


