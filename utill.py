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
        self.label_text = text[text.rfind(" ") - 2:]
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
    if text in conditionals:
        return True
    return False


# TODO: make this more robust
def isBranching(text):
    if text.strip().startswith("b"):
        return True
    return False


def getOpcode(text):
    text = text.strip()
    a = text.find(" ")
    b = text.find("\t")
    if a > b: a = b
    return text[0:a + 1].strip()
