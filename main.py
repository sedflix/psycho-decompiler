from utill import *

rzero = 0
nest = 0

def main(filename):
    op = open(filename)
    fn = open("op.s", "w")
    ln = op.readlines()
    getLoop(ln)
    for l in ln:
        l = l.lower()
        l = removeSpaces(l)
        if isComment(l) or isDotted(l):
            code = "ignored sad ://"
        elif isMove(l):
            fn.write(getMove(l) + "\n")
        elif isInterrupt(l):
            fn.write(getInterrupt(l) + "\n")
        elif isComparison(l):
            fn.write(getComparison(l) + "\n")
        elif isArithLogical(l):
            fn.write(getArithLogical(l) + "\n")
        else:
            fn.write("[Unimplemented] " + l + "\n")

def removeSpaces(text):
    text = text.replace("\t"," ")
    text = text.strip(" ")
    text = text.strip("\n")
    i = 0
    while(i != len(text)-1):
        if text[i] == " " and text[i+1] == " ":
            text = text[:i+1]+text[i+2:]
            continue
        i += 1
    return text

def getOpcode(text):
    op = text.split(" ")[0]
    return op

def getArgs(text):
    op = ''.join(text.split(" ")[1:])
    args = op.split(",")
    for i in range(len(args)):
        args[i].strip(" ")
        if args[i][0] == "#":
            args[i] = args[i][1:]
    return args

def getLoop(lines):
    loops = []
    ifs = []
    ifelses = []
    labels_by_name = dict()
    labels_by_line_no = dict()
    cmps = []
    branches_line_no = dict()
    branches_label = dict()
    i = 0
    for line in lines:
        if isLabel(line):
            label = Label(i, line)
            labels_by_name[label.text] = label
            labels_by_line_no[i] = label
        elif isComparison(line):
            cmps.append(CMP(i, line))
        elif isBranching(line):
            branch = Branch(i, line)
            branches_label[branch.label_text] = branch
            branches_line_no[i] = branch
        i += 1
    for cmp in cmps:
        cmp_line_no = cmp.line_no
        branch = branches_line_no[cmp_line_no + 1]
        label = labels_by_name[branch.label_text]
        branch.label = label
        if label.line_no < branch.line_no:
            loops.append(Loop(label, branch, cmp))
        else:
            if label.line_no - 1 in branches_line_no.keys():
                branch2End = branches_line_no[label.line_no - 1]
                label2End = labels_by_name[branch2End.label_text]
                ifelses.append(IfElse(cmp=cmp, branch_to_2nd_block=branch,branch_to_end=branch2End, block2_label=label, end_label=label2End))
            else:
                ifs.append(If(cmp=cmp, branch_to_end=branch, end_label=label))
    for loop in loops:
        print("Enter at " + str(loop.enterNode) + " and exits at " + str(loop.exitNode))

    for If in ifs:
        print("Enter at " + str(If.block1_start_line) + " and exits at " + str(If.block1_end_line))

    for ifelse in ifelses:
        print("If enter at " + str(ifelse.block1_start_line) + " and exits at " + str(ifelse.block1_end_line) +
              " -- Else enter at " + str(ifelse.block1_start_line) + " and exits at " + str(ifelse.block2_end_line))

def isComment(text):
    cmt = getOpcode(text)
    if cmt[0] == "@":
        return True
    return False

def isDotted(text):
    dot = getOpcode(text)
    if dot[0] == ".":
        return True
    return False

def isBranching(text):
    brn = getOpcode(text)
    if brn[0] == "b":
        return True
    return False

def isLabel(text):
    brn = getOpcode(text)
    if brn[-1] == ":":
        return True
    return False

def isInterrupt(line):
    swi = getOpcode(line)
    if swi == "swi":
        return True
    return False

def getInterrupt(line):
    args = getArgs(line)
    ans = ""
    #global rzero
    if args[0] == "0x6c":
        ans = "r0 = input()"
    elif args[0] == "0x6b":
        ans = "print(r1)"
    elif args[0] == "0x11":
        ans = "exit()"
    return ans

def isComparison(line):
    comp = getOpcode(line)
    comparisons = ["eq", "lt", "gt", "le", "ge", "ne"]
    if comp in comparisons:
        return True
    return False

def getComparison(cmp, branch):
    vars = getArgs(cmp)
    var1 = vars[0]
    var2 = vars[1]
    cond = getOpcode(branch)[1:]
    ans = ""
    if cond == "eq":
        ans = (str(var1) + " == " + str(var2))
    elif cond == "lt":
        ans = (str(var1) + " < " + str(var2))
    elif cond == "gt":
        ans = (str(var1) + " > " + str(var2))
    elif cond == "ge":
        ans = (str(var1) + " >= " + str(var2))
    elif cond == "le":
        ans = (str(var1) + " <= " + str(var2))
    elif cond == "ne":
        ans = (str(var1) + " != " + str(var2))
    return ans

def isArithLogical(text):
    comp = getOpcode(text)
    comparisons = ["add", "sub", "rsb", "and", "orr", "ne"]
    if comp in comparisons:
        return True
    return False

def getArithLogical(text):
    args = getArgs(text)
    opcode = getOpcode(text)
    ans = ""
    if opcode == "add" or opcode == "vadd.f32" or opcode == "vadd.f64":
        ans = str(args[0]) + " = " + str(args[1]) + " + " + str(args[2])
    elif opcode == "sub":
        ans = str(args[0]) + " = " + str(args[1]) + " - " + str(args[2])
    elif opcode == "rsb":
        ans = str(args[0]) + " = " + str(args[2]) + " - " + str(args[1])
    elif opcode == "and":
        ans = str(args[0]) + " = " + str(args[1]) + " && " + str(args[2])
    elif opcode == "orr":
        ans = str(args[0]) + " = " + str(args[1]) + " || " + str(args[2])
    return ans

def isMove(text):
    comp = getOpcode(text)
    comparisons = ["mov", "vmov.f32"]
    if comp in comparisons:
        return True
    return False

def getMove(text):
    args = getArgs(text)
    opcode = getOpcode(text)
    ans = ""
    global rzero
    if text == "mov r0, #0":
        rzero = 0
    if opcode == "mov" or opcode == "vmov.f32":
        ans = str(args[0]) + " = " + str(args[1])
    return ans

def getLdStr(text):
    args = getArgs(text)
    opcode = getOpcode(text)
    if opcode == "str":
        ans = str(args[1]) + " = " + str(args[0])
    elif opcode == "ldr":
        ans = "int " + str(args[0]) + " = " + str(args[1])
    elif opcode == "vldr.32":
        ans = "float " + str(args[0]) + " = " + str(args[1])
    elif opcode == "vldr.64":
        ans = "double " + str(args[0]) + " = " + str(args[1])
    elif opcode == "ldrb":
        ans = "char " + str(args[0]) + " = " + str(args[1])
    return ans