from utill import *

def getLoopsAndIfs(lines):
    labels_by_name = dict()
    labels_by_line_no = dict()
    cmps = []
    branches_line_no = dict()
    branches_label = dict()

    i = 0
    for line in lines:
        line = removeSpaces(line.lower())
        i += 1
        if isLabel(line):
            line = line[:-1]
            label = Label(i, line)
            labels_by_name[line] = label
            labels_by_line_no[i] = label
        elif isConditional(line):
            cmps.append(CMP(i, line))
        elif isBranching(line):
            branch = Branch(i, line)
            branches_label[line] = branch
            branches_line_no[i] = branch

    loops = []
    ifs = []
    ifelses = []

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
        print(labels_by_name)
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
            """
                Shitty yet a working way to know if the conditional block is if or if-else block
                Assumption: If the label has a line before it which is branching statement, then it is a if-else block.
                Like: 
                	 b	.L4
                    .L3:
                is sign of an if else statement
                    >any statement other than branch>
                .L4                
                is a sign that  .L4 is the ending label                 
            """
            if label.line_no - 1 in branches_line_no.keys():
                # if and else block
                branch2End = branches_line_no[label.line_no - 1]  # branch statement in block one that leads to end
                label2End = labels_by_name[branch2End.label_text]  # label at which everything ends
                ifelses.append(IfElse(cmp=cmp, branch_to_2nd_block=branch, branch_to_end=branch2End, block2_label=label, end_label=label2End))
            else:
                # if only blocks
                ifs.append(If(cmp=cmp, branch_to_end=branch, end_label=label))

    return [loops, ifelses, ifs]