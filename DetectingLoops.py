class CMP(object):
    def __init__(self, line_no, text):
        self.line_no = line_no
        self.text = text

class Branch(object):
    def __init__(self, line_no, text, label=None):
        self.line_no = line_no
        self.text = text
        self.label_text = str.split(text, "\t")[1].replace(".", "").strip()
        self.label = label


class Label(object):
    def __init__(self, line_no, text):
        self.line_no = line_no
        self.text = text.replace(":", "").replace(".","")


class Loop(object):
    def __init__(self, label, branch, cmp):
        self.label = label
        self.branch = branch
        self.cmp = cmp
        self.enterNode = label.line_no
        self.exitNode = branch.line_no


def isLabel(text):
    if text.endswith(":"):
        return True


if __name__ == '__main__':
    file = open('examples/loops3.s')

    labels_by_name = dict()
    labels_by_line_no = dict()
    cmps = []
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
            cmps.append(CMP(i,line))
        elif line.startswith('b'):
            branch = Branch(i, line)
            branches_label[branch.label_text] = branch
            branches_line_no[i] = branch


    loops = []

    for cmp in cmps:
        cmp_line_no = cmp.line_no
        branch = branches_line_no[cmp_line_no+1]
        label = labels_by_name[branch.label_text]
        branch.label = label
        loops.append(Loop(label, branch, cmp))

    for loop in loops:
        print("Enter at " + str(loop.enterNode) + " and exits at " + str(loop.exitNode))

    file.close()
