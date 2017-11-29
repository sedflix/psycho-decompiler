from DetectingLoops import *
from floats_chars import *


class Block(object):
    def __init__(self, start_line_no, end_line_no, whichBlock):
        self.start_line_no = start_line_no
        self.end_line_no = end_line_no
        self.whichBlock = whichBlock
        self.children = []
        self.parent = None

    def hasInside(self, item):
        if item.start_line_no > self.start_line_no and item.end_line_no < self.end_line_no:
            return True
        return False


class Tree(object):
    def __init__(self, root):
        self.root = root

    def add(self, block, root):
        if root.hasInside(block):
            for k in root.children:
                self.add(block, k)
        else:
            root.children.append(block)


if __name__ == "__main__":
    loops, ifelses, ifs = getLoopsAndIfs("loops3.s")
    functions = getFunctions("loops3.s")

    lines = dict()
    file = open("loops3.s")
    i = 0
    while True:
        line = file.readline().strip().lower()
        if line is '':
            break

        i += 1
    file.close()

    tree = Tree(Block(functions[0].start_line_no, functions[0].end_line_no, functions[0]))

    tree.add()
