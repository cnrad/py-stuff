import sys, math

for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print (u"\u001b[0m")

# ansi colors: 0-16 base colors. 17+ are gradients in groups of 5
# idea: split string into 5 sections, gradient it


def gradient(string):
    length = len(string)
    index = 0
    section = math.ceil(length/5) + index
    array = []

    for i in range(0, 5):
        array.append(string[index:section])
        index += math.ceil(length/5)
        section = math.ceil(length/5) + index

    print(array)


gradient("testerbob i suppose")
