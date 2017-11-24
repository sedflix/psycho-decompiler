from utill import *


class Loop(object):
    def __init__(self, label, branch, cmp):
        self.label = label
        self.branch = branch
        self.cmp = cmp
        self.enterNode = label.line_no
        self.exitNode = branch.line_no


class If(object):
    def __init__(self, cmp, label_else, label_end, branch_to_else, branch_to_end):
        self.cmp = cmp
        self.label_else = label_else
        self.label_end = label_end
        self.branch_to_else = branch_to_else
        self.branch_to_end = branch_to_end


if __name__ == '__main__':
    file = open('examples/ifs.s')

    labels_by_name = dict()
    labels_by_line_no = dict()
    cmps = []
    branches_line_no = dict()
    branches_label = dict()

    i = 0
    while True:
        line = file.readline().strip().lower()
        if line is '':
            break

        i += 1

        if isLabel(line):
            label = Label(i, line)
            labels_by_name[label.text] = label
            labels_by_line_no[i] = label
        elif isConditional(line):
            cmps.append(CMP(i, line))
        elif isBranching(line):
            branch = Branch(i, line)
            branches_label[branch.label_text] = branch
            branches_line_no[i] = branch

    loops = []
    ifs = []

    """
        Now I will try to describe this really stupid algorithm.
        If finds the compare statements first.
        
        Assumption: In a case of Loop the line following cmp is branch statement.
        
        Now we get the branch statement from line_no + 1. We extract the label from branch.
        The label tells us the entry point of the loop.
        
    """

    # TODO: This will most probably tells if statements are loop. sometimes.
    # IDK. haven't thought about it or event tried testing it

    for cmp in cmps:

        cmp_line_no = cmp.line_no
        branch = branches_line_no[cmp_line_no + 1]
        label = labels_by_name[branch.label_text]
        branch.label = label

        """ 
            Assumption: In "loops" the label branching statement refers to 
            is located "above" the branching statement
            Assumption: In "if" statements the label of branching statement refers to 
            is located "below" the branching statement
        """
        if label.line_no < branch.line_no:
            loops.append(Loop(label, branch, cmp))
        else:

            if "label.line_no - 1" in branches_line_no.keys():
                # if and else block
                branch2End = branches_line_no[label.line_no - 1]
                label2End = labels_by_name[branch2End.label_text]
                ifs.append(If(cmp, label, label2End, branch, branch2End))
            else:
                # if only blocks
                ifs.append(If(cmp, label, None, None, branch))

    for loop in loops:
        print("Enter at " + str(loop.enterNode) + " and exits at " + str(loop.exitNode))

    for If in ifs:
        print(If)

    file.close()
