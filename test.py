from utill import *
op = open("examples//chrs.s")
fn = open("chrs.s", "w")
ln = op.readlines()
for l in ln:
    fn.write(getOpcode(l))
    fn.write("\n")