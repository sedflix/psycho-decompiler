from utill import *

def getLoopsAndIfs(filename):
    file = open(filename)

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
        label = labels_by_name[branch.label_text]
        branch.label = label

        """ 
            Assumption: In "loops" the label branching statement refers to 
            is located "above" the branching statement
            Assumption: In "if" statements the label of branching statement refers to 
            is located "below" the branching statement
        """

        if label.line_no < branch.line_no:
            # for loops
            loops.append(Loop(label, branch, cmp))

        else:
            # for different kinds of if blocks

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

                ifelses.append(IfElse(cmp=cmp, branch_to_2nd_block=branch,
                                      branch_to_end=branch2End, block2_label=label, end_label=label2End))
            else:
                # if only blocks

                ifs.append(If(cmp=cmp, branch_to_end=branch, end_label=label))

    for loop in loops:
        print("Enter at " + str(loop.enterNode) + " and exits at " + str(loop.exitNode))

    for If_ in ifs:
        print("Enter at " + str(If_.block1_start_line) + " and exits at " + str(If_.block1_end_line))

    for ifelse in ifelses:
        print("If enter at " + str(ifelse.block1_start_line) + " and exits at " + str(ifelse.block1_end_line) +
              " -- Else enter at " + str(ifelse.block1_start_line) + " and exits at " + str(ifelse.block2_end_line))

    file.close()

    return [loops, ifelses, ifs]


if __name__ == "__main__":
    getLoopsAndIfs("examples/sampleinput.s")
