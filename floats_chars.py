"""
    Think about blocks and visibility 
    association with r7,#4 and variables 
"""
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

        pass
