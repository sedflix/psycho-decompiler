from utill import *


def getVarRelations(filename):
    file = open(filename)
    lines = dict()
    i = 0

    while True:
        line = file.readline().strip().lower()
        if line is '':
            break
        i = i + 1

    for i in range(len(lines)):
        print(lines[i])
        if "ldr" in lines[i]:
            print("Asfd")
            print(get2ndArg(lines[i]))


def get2ndArg(text):
    text = removeSpaces(text)
    return find_between(text, "[", "]").strip()


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


if __name__ == '__main__':
    getVarRelations("examples/floats.s")
