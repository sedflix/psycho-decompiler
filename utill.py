"""

"""

# TODO: make this list complete [exclude stuffs ending with 's']
conditionals = [
    "cmp",
    "cmn",
    "tst",
    "teq"
]


class CMP(object):
    def __init__(self, line_no, text):
        self.line_no = line_no
        self.text = text


class Branch(object):
    def __init__(self, line_no, text, label=None):
        text = text.strip()
        self.line_no = line_no
        self.text = text
        # dealing with space
        self.label_text = getArgs(text)[0]
        self.label = label


class Label(object):
    def __init__(self, line_no, text):
        self.line_no = line_no
        self.text = text.replace(":", "")


class Loop(object):
    def __init__(self, label, branch, cmp):
        self.label = label
        self.branch = branch
        self.cmp = cmp
        self.enterNode = label.line_no
        self.exitNode = branch.line_no


class If(object):
    def __init__(self, cmp, branch_to_end, end_label):
        self.cmp = cmp

        self.cmp_branch = branch_to_end
        self.branch_to_end = branch_to_end

        self.end_label = end_label

        self.block1_start_line = branch_to_end.line_no + 1
        self.block1_end_line = end_label.line_no - 1


class IfElse(object):
    def __init__(self, cmp, branch_to_2nd_block, branch_to_end, block2_label, end_label):
        self.cmp = cmp

        self.cmp_branch = branch_to_2nd_block
        self.branch_to_2nd_Block = branch_to_2nd_block

        self.block1_start_line = branch_to_2nd_block.line_no + 1

        assert branch_to_end.line_no - 1 == block2_label.line_no - 2
        self.block1_end_line = branch_to_end.line_no - 1
        self.block2_start_line = block2_label.line_no + 1
        self.block2_end_line = end_label.line_no - 1

        self.block2_start_label = block2_label
        self.block2_label = block2_label

        self.block2_end_label = end_label
        self.end_label = end_label


def isLabel(text):
    if text.strip().endswith(":"):
        return True


def isConditional(text):
    text = getOpcode(text)
    # if text.endswith("s"):
    #     return True
    print(text)
    if text in conditionals:
        return True
    return False


# TODO: make this more robust
def isBranching(text):
    if text.strip().startswith("b"):
        return True
    return False

def removeSpaces(text):
    text = text.replace("\t"," ")
    text = text.strip(" ")
    i = 0
    while(i != len(text)-1):
        if text[i] == " " and text[i+1] == " ":
            text = text[:i+1]+text[i+2:]
            continue
        i += 1
    return text

def getOpcode(text):
    text = removeSpaces(text)
    op = text.split(" ")[0]
    return op


def getArgs(text):
    text = removeSpaces(text)
    op = ''.join(text.split(" ")[1:])
    args = op.split(",")
    return args

def getComparision(cmp, branch):
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

def getOpDesc(text):
    text = text.upper()
    args = getArgs(text)
    opcode = getOpcode(text)
    if opcode == "add" or opcode == "vadd.f32" or opcode == "vadd.f64":
        print(str(args[0]) + " = " + str(args[1]) + " + " + str(args[2]))
    elif opcode == "sub":
        print(str(args[0]) + " = " + str(args[1]) + " - " + str(args[2]))
    elif opcode == "rsb":
        print(str(args[0]) + " = " + str(args[2]) + " - " + str(args[1]))
    elif opcode == "and":
        print(str(args[0]) + " = " + str(args[1]) + " && " + str(args[2]))
    elif opcode == "orr":
        print(str(args[0]) + " = " + str(args[1]) + " || " + str(args[2]))
    elif opcode == "mov" or opcode == "vmov.f32":
        print(str(args[0]) + " = " + str(args[1]))
    elif opcode == "str":
        print(str(args[1]) + " = " + str(args[0]))
    elif opcode == "ldr":
        print("int " + str(args[0]) + " = " + str(args[1]))
    elif opcode == "vldr.32":
        print("float " + str(args[0]) + " = " + str(args[1]))
    elif opcode == "vldr.64":
        print("double " + str(args[0]) + " = " + str(args[1]))
    elif opcode == "ldrb":
        print("char " + str(args[0]) + " = " + str(args[1]))