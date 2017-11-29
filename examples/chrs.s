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
	.file	"chars.c"
	.text
	.align	1
	.global	main
	.syntax unified
	.thumb
	.thumb_func
	.fpu vfpv3-d16
	.type	main, %function
main:
	push	{r7, lr}
	sub	sp, sp, #8
	add	r7, sp, #0
	movs	r3, #115
	strb	r3, [r7, #7]
	bl	lol(PLT)
	nop
	adds	r7, r7, #8
	mov	sp, r7
	@ sp needed
	pop	{r7, pc}
	.size	main, .-main
	.align	1
	.global	lol
	.syntax unified
	.thumb
	.thumb_func
	.fpu vfpv3-d16
	.type	lol, %function
lol:
	push	{r7}
	sub	sp, sp, #12
	add	r7, sp, #0
	movs	r3, #115
	strb	r3, [r7, #7]
	nop
	adds	r7, r7, #12
	mov	sp, r7
	@ sp needed
	ldr	r7, [sp], #4
	bx	lr
	.size	lol, .-lol
	.ident	"GCC: (Ubuntu/Linaro 7.2.0-6ubuntu1) 7.2.0"
	.section	.note.GNU-stack,"",%progbits
