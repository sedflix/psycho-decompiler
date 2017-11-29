r7 = 0
r0 = 0
r0 = input()
r6 = r0
r1 = 0
r2 = 1
[Unimplemented] cmp r6, #0
[Unimplemented] bne loop
r6 = 20
[Unimplemented] loop:
r1 = r2 + r1
r2 = r1 - r2
r0 = 1
print(r1)
r0 = ''

r7 = r7 + 1
[Unimplemented] cmp r7, r6
[Unimplemented] bne loop
exit()
