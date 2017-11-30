from DetectingLoops import *
from FunctionDetection import *

fl = open("op.s", "w")

def writeFunction(f):
    if len(f.return_type) == 0:
        final_str = "void"
    else:
        final_str = f.return_type[0]
    final_str = final_str + " " + f.name + " ( "
    for i in range(len(f.parameters_type)):
        if not i == 0:
            final_str = final_str + ", "
        final_str = final_str + f.parameters_type[i] + " " + f.parameters[i]
    final_str = final_str + " ) {"
    fl.write(final_str + "\n")
    linenext = lines[f.start_line_no + 1 : f.end_line_no + 1]
    writeBlock(linenext)
    if len(f.return_) == 0:
        final_str = "return;"
    else:
        final_str = "return " + f.return_[0]
    final_str = final_str + "\n}"
    fl.write(final_str + "\n")

def writeBlock(lines):
    [loops, ifelses, ifs] = getLoopsAndIfs(lines)
    outer = getOuterBlocks(loops, ifs)
    i = 0
    for bl in outer:
        j = bl.getStart()
        parse(lines[i:j-1])
        if type(bl).__name__ == "Loop":
            writeLoop(bl, lines)
        elif type(bl).__name__ == "If":
            writeIf(bl, lines)
        i = bl.getEnd()+1
    j = len(lines)
    parse(lines[i:j])

def getOuterBlocks(loops, ifs):
    arr = loops + ifs
    for l in loops:
        for i in loops + ifs:
            if i.contains(l.enterNode, l.exitNode):
                arr.remove(l)
                break
    for l in ifs:
        for i in loops + ifs:
            if i.contains(l.block1_start_line, l.block1_end_line):
                arr.remove(l)
                break
    return arr


def parse(lines):
    for l in lines:
        fn = ""
        if isIgnore(l):
            fn = ""
        elif isMove(l):
            fn = getMove(l) 
        elif isInterrupt(l):
            fn = getInterrupt(l) 
        elif isComparison(l):
            fn = getComparison(l) 
        elif isArithLogical(l):
            fn = getArithLogical(l) 
        elif isLdStr(l):
            fn = getLdStr(l)
        else:
            fn = ""
        fl.write(fn + "\n")

def writeIf(ifx, l):
    vl = getArgs(removeSpaces(l[ifx.block1_start_line-3]))
    op = getOpcode(removeSpaces(l[ifx.block1_start_line-2]))
    fl.write("if (" + branch_statement(vl, op) + ") { \n")
    writeBlock(l[ifx.block1_start_line:ifx.block1_end_line])
    fl.write("} \n")

def writeLoop(loop, l):
    fl.write("do { \n")
    writeBlock(l[loop.enterNode: loop.exitNode-2])
    vl = getArgs(removeSpaces(l[loop.exitNode-2]))
    op = getOpcode(removeSpaces(l[loop.exitNode-1]))
    fl.write("} while (" + branch_statement_2(vl, op) + ") \n")

def branch_statement(vl, cond):
    cond = cond[1:]
    var1 = vl[0]
    var2 = vl[1]
    ans = ""
    if cond == "eq":
        ans = str(var1) + " != " + str(var2)
    elif cond == "lt":
        ans = str(var1) + " >= " + str(var2)
    elif cond == "gt":
        ans = str(var1) + " <= " + str(var2)
    elif cond == "ge":
        ans = str(var1) + " < " + str(var2)
    elif cond == "le":
        ans = str(var1) + " > " + str(var2)
    elif cond == "ne":
        ans = str(var1) + " == " + str(var2)
    return ans

def branch_statement_2(vl, cond):
    cond = cond[1:]
    var1 = vl[0]
    var2 = vl[1]
    ans = ""
    if cond == "eq":
        ans = str(var1) + " == " + str(var2)
    elif cond == "lt":
        ans = str(var1) + " < " + str(var2)
    elif cond == "gt":
        ans = str(var1) + " > " + str(var2)
    elif cond == "ge":
        ans = str(var1) + " >= " + str(var2)
    elif cond == "le":
        ans = str(var1) + " <= " + str(var2)
    elif cond == "ne":
        ans = str(var1) + " != " + str(var2)
    return ans

def isIgnore(line):
    if "sp" in line:
        return True
    line = removeSpaces(line)
    if line[0] == "." or line[0]  == "@":
        return True
    if "nop" in line:
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
        ans = "printf(r1)"
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
    comparisons = ["add", "sub", "rsb", "mul", "and", "orr"]
    for c in comparisons:
        if c in comp:
            return True
    return False

def getArithLogical(text):
    args = getArgs(text)
    opcode = getOpcode(text)
    ans = ""
    if "add" in opcode:
        ans = str(args[0]) + " = " + str(args[1]) + " + " + str(args[2])
    elif "sub" in opcode:
        ans = str(args[0]) + " = " + str(args[1]) + " - " + str(args[2])
    elif "rsb" in opcode:
        ans = str(args[0]) + " = " + str(args[2]) + " - " + str(args[1])
    elif "mul" in opcode:
        ans = str(args[0]) + " = " + str(args[2]) + " * " + str(args[1])
    elif "and" in opcode:
        ans = str(args[0]) + " = " + str(args[1]) + " && " + str(args[2])
    elif "orr" in opcode:
        ans = str(args[0]) + " = " + str(args[1]) + " || " + str(args[2])
    return ans

def isMove(text):
    comp = getOpcode(text)
    if "mov" in comp:
        return True
    return False

def getMove(text):
    args = getArgs(text)
    opcode = getOpcode(text)
    ans = ""
    if "mov" in opcode:
        ans = str(args[0]) + " = " + str(args[1])
    return ans

def isLdStr(text):
    comp = getOpcode(text)
    if "ldr" in comp or "str" in comp:
        return True
    return False

def getLdStr(text):
    args = getArgs(text)
    reg = args[0]
    if len(args) > 2:
        mem1 = args[1]
        mem2 = args[2]
        mem = mem1[1:] + "_" + mem2[:-1]
    else:
        mem = args[1]
    opcode = getOpcode(text)
    ans = ""
    if "ldr" in opcode:
        ans = reg + " = " + mem
    elif "str" in opcode:
        ans = mem + " = " + reg
    return ans

if __name__ == "__main__":
    lines = open("ip.s").readlines()
    functions = getFunctions(lines)
    function_list = []
    for f in functions:
        func_scope = lines[f.start_line_no:f.end_line_no+1]
        writeFunction(f)