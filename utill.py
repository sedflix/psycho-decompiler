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
