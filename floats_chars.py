from utill import *

"""
    Think about blocks and visibility 
    association with r7,#4 and variables 
"""

if __name__ == '__main__':
    file = open('examples/chars.s')

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
            agrs = getArgs(line)

            print("got a fucking float: " + str(agrs[1]))

            pass

        if getOpcode(line) == "strb" and getOpcode(lines[i - 1]) == "movs":
            # char
            # check same register
            # record stack address
            # add to variables
            print("got a char")
            pass

        if getOpcode(line) == "vldr.32":
            # loading a float
            pass

        if getOpcode(line) == "ldrb":
            # loading a char
            pass

        # if getOpcode(line)

        i += 1
        pass

    # function detection can be done in the following ways:
    # label -> push -> sub, sp, sp #? -> add r7, sp, 0
    # or
    # label -> sub, sp, sp #? -> add r7, sp, 0
    #
    # end withs adds r7, r7,  #? -> mov sp, r7
    # and maybe ldr r7, [sp], #4 -> bx	lr

    for i in range(len(lines.keys())):
        if isLabel(lines[i]):
            if getOpcode(lines[i + 1]) == "push" and getOpcode(lines[i + 2]) == "sub":
                x = getArgs(lines[i + 2])
                print("start @" + lines[i])
                for j in range(i, len(lines.keys())):
                    if getOpcode(lines[j]) == "adds":
                        y = getArgs(lines[j])
                        if x[2] == y[2]:
                            print("ends @" + lines[j])
            pass

    for i in range(len(lines.keys())):
        if isBranching(lines[i]):
            print(lines[i])
            print(getOpcode(lines[i]))
