class CMP(object):
    def __init__(self, line_no, text):
        self.line_no = line_no
        self.text = text

class Branch(object):
    def __init__(self, line_no, text, label=None):
        self.line_no = line_no
        self.text = text
        self.label_text = str.split(text, "\t")[1].replace(".", "")
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


def isLabel(text):
    if text.endswith(":"):
        return True


if __name__ == '__main__':
    file = open('examples/loops3.s')

    labels_by_name = dict()
    labels_by_line_no = dict()
    cmps = dict()
    branches_line_no = dict()
    branches_label = dict()


    i = 0
    while True:
        line = file.readline().strip()
        if line is '':
            break

        i += 1

        if isLabel(line):
            label = Label(i,line)
            labels_by_name[label.text] = label
            labels_by_line_no[i] = label
        elif line.startswith('cmp'):
            cmp = CMP(i,line)
            cmps[i] = cmp
        elif line.startswith('b'):
            branch = Branch(i, line)
            branches_label[branch.label_text] = branch
            branches_line_no[i] = branch

    print(labels_by_name)

    file.close()
