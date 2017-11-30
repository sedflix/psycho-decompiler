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
	.file	"everything.c"
	.text
	.align	1
	.global	yehFunctionHain
	.syntax unified
	.thumb
	.thumb_func
	.fpu vfpv3-d16
	.type	yehFunctionHain, %function
yehFunctionHain:
	push	{r7}
	sub	sp, sp, #12
	add	r7, sp, #0
	str	r0, [r7, #4]
	ldr	r3, [r7, #4]
	subs	r3, r3, #1
	str	r3, [r7, #4]
	ldr	r3, [r7, #4]
	mov	r0, r3
	adds	r7, r7, #12
	mov	sp, r7
	@ sp needed
	ldr	r7, [sp], #4
	bx	lr
	.size	yehFunctionHain, .-yehFunctionHain
	.align	1
	.global	main
	.syntax unified
	.thumb
	.thumb_func
	.fpu vfpv3-d16
	.type	main, %function
main:
	push	{r7, lr}
	sub	sp, sp, #16
	add	r7, sp, #0
	movs	r3, #1
	str	r3, [r7, #4]
	mov	r3, #1073741824
	str	r3, [r7, #8]	@ float
	movs	r3, #0
	str	r3, [r7, #12]
	b	.L4
.L5:
	ldr	r3, [r7, #4]
	adds	r3, r3, #1
	str	r3, [r7, #4]
	vldr.32	s15, [r7, #8]
	vmov.f32	s14, #1.0e+0
	vadd.f32	s15, s15, s14
	vstr.32	s15, [r7, #8]
	ldr	r3, [r7, #4]
	cmp	r3, #19
	bgt	.L4
	vldr.32	s15, [r7, #8]
	vmov.f32	s14, #1.0e+0
	vadd.f32	s15, s15, s14
	vstr.32	s15, [r7, #8]
	ldr	r3, [r7, #4]
	and	r3, r3, #1
	cmp	r3, #0
	bne	.L4
	ldr	r3, [r7, #12]
	adds	r3, r3, #1
	str	r3, [r7, #12]
.L4:
	ldr	r3, [r7, #4]
	cmp	r3, #29
	ble	.L5
	b	.L6
.L7:
	ldr	r0, [r7, #12]
	bl	yehFunctionHain(PLT)
	str	r0, [r7, #12]
.L6:
	ldr	r3, [r7, #12]
	cmp	r3, #0
	bgt	.L7
	nop
	adds	r7, r7, #16
	mov	sp, r7
	@ sp needed
	pop	{r7, pc}
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.2.0-6ubuntu1) 7.2.0"
	.section	.note.GNU-stack,"",%progbits
