from DetectingLoops import getLoopsAndIfs

rzero = 0
cond = 0
loop = 0
tocmp = []
ifbranch = ""

def main(filename):
    op = open(filename)
    fn = open("op.s", "w")
    ln = op.readlines()
    #getLoop(ln)
    for l in ln:
        l = l.lower()
        l = removeSpaces(l)
        tabs = "  " * (cond+loop)
        fn.write(tabs)
        if tocmp != []:
            fn.write(getBranch(l) + "\n")
        elif isIf(l):
            getIf(l)
        elif isBranching(l):
            if cond == 1:
                endIf(l)
            elif loop == 1:
                startLoop(l)
        if isMove(l):
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

#def getLoop(lines):


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

def isIf(text):
    cmp = getOpcode(text)
    if cmp == "cmp" and loop == 0:
        return True
    return False

def getIf(text):
    args = getArgs(text)
    global tocmp
    tocmp = [args[0], args[1]]
    return


def endIf(text):
    global ifbranch, cond
    if ifbranch == getOpcode(text)[:-1]:
        cond = 0
        ifbranch = ""
    return

def startLoop(text):
    global loop, ifbranch
    loop = 1
    ifbranch = getOpcode(text)[:-1]
    return

def getBranch(line):
    global tocmp, ifbranch, cond
    var1 = tocmp[0]
    var2 = tocmp[1]
    tocmp = []
    cond = getOpcode(line)[1:]
    ifbranch = getArgs(line)
    cond == 1
    ans = ""
    if cond == "eq":
        ans = "if " + str(var1) + " != " + str(var2) + ":"
    elif cond == "lt":
        ans = "if " + str(var1) + " >= " + str(var2) + ":"
    elif cond == "gt":
        ans = "if " + str(var1) + " <= " + str(var2) + ":"
    elif cond == "ge":
        ans = "if " + str(var1) + " < " + str(var2) + ":"
    elif cond == "le":
        ans = "if " + str(var1) + " > " + str(var2) + ":"
    elif cond == "ne":
        ans = "if " + str(var1) + " == " + str(var2) + ":"
    return ans

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

def getComparison(line):
    vars = getArgs(line)
    var1 = vars[0]
    var2 = vars[1]
    cond = getOpcode(line)
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