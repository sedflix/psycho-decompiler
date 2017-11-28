from utill import *

"""
    Think about blocks and visibility 
    association with r7,#4 and variables 
"""
if __name__ == '__main__':
    file = open('examples/ifs.s')

    labels_by_name = dict()
    labels_by_line_no = dict()
    cmps = []
    branches_line_no = dict()
    branches_label = dict()

    lines = dict()
    variables = []

    i = 0
    while True:
        line = file.readline().strip().lower()
        if line is '':
            break
        lines[i] = line

        if getOpcode(line) == "str" and getOpcode(lines[i - 1]) == 'movt' and getOpcode(lines[i - 2]) == 'movw':
            # float
            # check all of them points to the same register (like r3)
            # record stack address
            # add to variable
            pass

        if getOpcode(line) == "strb" and getOpcode(lines[i - 1]) == "movs":
            # char
            # check same register
            # record stack address
            # add to variables
            pass

        # if getOpcode(line)

        i += 1
        pass
