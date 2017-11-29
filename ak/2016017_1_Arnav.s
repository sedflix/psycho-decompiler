mov r0, #0
swi 0x6c
mov r1, r0
mov r5, #0
mov r4, #0

loop:
	mov r0, #0
	swi 0x6c
	add r4, r4, r0
	add r5, r5, #1
	cmp r5, r1
ble loop @branch if r5<=r1
mov r1, r4
swi 0x6b
swi 0x11
