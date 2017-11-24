"""

"""

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
        self.line_no = line_no
        self.text = text
        self.label_text = str.split(text, " ")[1].replace(".", "").strip()
        self.label = label


class Label(object):
    def __init__(self, line_no, text):
        self.line_no = line_no
        self.text = text.replace(":", "").replace(".", "")


def isLabel(text):
    if text.strip().endswith(":"):
        return True


def isConditional(text):
    text = getOpcode(text)
    if text.endswith("s"):
        return True
    if text in conditionals:
        return True
    return False


def isBranching(text):
    if text.strip().startswith("b"):
        return True
    return False


def getOpcode(text):
    text = text.strip()
    return text[0: text.find(" ") + 1].strip()
