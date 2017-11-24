	.arch armv7-a
	.eabi_attribute 28, 1
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 2
	.eabi_attribute 30, 6
	.eabi_attribute 34, 1
	.eabi_attribute 18, 4
	.file	"loops.c"
	.text
	.align	1
	.global	main
	.syntax unified
	.thumb
	.thumb_func
	.fpu vfpv3-d16
	.type	main, %function
main:
	@ args = 0, pretend = 0, frame = 16
	@ frame_needed = 1, uses_anonymous_args = 0
	@ link register save eliminated.
	push	{r7}
	sub	sp, sp, #20
	add	r7, sp, #0
	movs	r3, #0
	str	r3, [r7]
	movs	r3, #0
	str	r3, [r7, #4]
	movs	r3, #56
	str	r3, [r7, #8]
	b	.L2
.L6:
	ldr	r3, [r7, #8]
	adds	r3, r3, #1
	str	r3, [r7, #8]
	ldr	r3, [r7, #4]
	adds	r3, r3, #1
	str	r3, [r7, #4]
	b	.L4
.L5:
	ldr	r3, [r7, #8]
	adds	r3, r3, #1
	str	r3, [r7, #8]
	ldr	r3, [r7, #4]
	adds	r3, r3, #1
	str	r3, [r7, #4]
	movw	r3, #23234
	str	r3, [r7, #12]
.L4:
	ldr	r3, [r7, #8]
	cmp	r3, #99
	ble	.L5
.L3:
	ldr	r3, [r7, #4]
	cmp	r3, #2
	ble	.L6
	ldr	r3, [r7]
	adds	r3, r3, #1
	str	r3, [r7]
.L2:
	ldr	r3, [r7]
	cmp	r3, #9
	ble	.L3
	nop
	adds	r7, r7, #20
	mov	sp, r7
	@ sp needed
	ldr	r7, [sp], #4
	bx	lr
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.2.0-6ubuntu1) 7.2.0"
	.section	.note.GNU-stack,"",%progbits
