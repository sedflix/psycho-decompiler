from utill import *

"""
    Think about blocks and visibility 
    association with r7,#4 and variables 
"""


class Function(object):
    def __init__(self, name, start_line_text, start_line_no, end_line_text, end_line_no):
        self.name = name
        self.start_line_text = start_line_text
        self.end_line_text = end_line_text
        self.start_line_no = start_line_no
        self.end_line_no = end_line_no
        self.parameters = []
        self.parameters_type = []
        self.return_ = []
        self.return_type = []
        self.callers_line_no = []


if __name__ == '__main__':
    file = open('examples/floats.s')

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

    functions = []

    for i in range(len(lines.keys())):
        if isLabel(lines[i]):
            print(lines[i])
            if getOpcode(lines[i + 1]) == "push" and getOpcode(lines[i + 2]) == "sub":
                x = getArgs(lines[i + 2])
                print("start @" + lines[i])
                j = i
                for j in range(i, len(lines.keys())):
                    if getOpcode(lines[j]) == "adds":
                        y = getArgs(lines[j])
                        if x[2] == y[2]:
                            print("ends @" + lines[j])
                            break
                functions.append(Function(
                    name=lines[i].replace(":", ""), start_line_text=lines[i + 1], start_line_no=i + 1,
                    end_line_text=lines[j + 2], end_line_no=j + 2
                ))
            pass

    for f in functions:
        rhs = dict()
        lhs = dict()
        for i in range(f.start_line_no, f.end_line_no):
            try:
                params = getArgs(lines[i])
                if not params[0] in lhs.keys():
                    lhs[params[0].strip()] = i
                if not params[1] in rhs.keys():
                    rhs[params[1].strip()] = i
                if not params[2] in rhs.keys():
                    rhs[params[1].strip()] = i
            except Exception:
                continue
        # print(rhs)
        # print(lhs)

        for var in lhs.keys():
            try:
                if lhs[var] < rhs[var]:
                    print(var)
            except Exception:
                print("err " + var)
                continue


    for i in range(len(lines.keys())):
        if "bl" in lines[i]:
            # it will branch to a function. Add as a calle
            pass
