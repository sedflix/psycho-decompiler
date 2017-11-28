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
	.file	"floats.c"
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
	sub	sp, sp, #24
	add	r7, sp, #0
	mov	r3, #1065353216
	str	r3, [r7, #4]	@ float
	mov	r3, #1065353216
	str	r3, [r7, #8]	@ float
	movw	r3, #8126
	movt	r3, 17238
	str	r3, [r7, #12]	@ float
	movw	r3, #52429
	movt	r3, 15820
	str	r3, [r7, #16]	@ float
	vldr.32	s14, [r7, #4]
	vldr.32	s15, [r7, #8]
	vadd.f32	s15, s14, s15
	vstr.32	s15, [r7, #20]
	vldr.32	s15, [r7, #12]
	vcvt.f64.f32	d7, s15
	vldr.32	s13, [r7, #16]
	vcvt.f64.f32	d6, s13
	vmov.f64	d1, d6
	vmov.f64	d0, d7
	bl	add(PLT)
	nop
	adds	r7, r7, #24
	mov	sp, r7
	@ sp needed
	pop	{r7, pc}
	.size	main, .-main
	.align	1
	.global	add
	.syntax unified
	.thumb
	.thumb_func
	.fpu vfpv3-d16
	.type	add, %function
add:
    push {r7}
	sub	sp, sp, #20
	add	r7, sp, #0
	vstr.32	s0, [r7, #4]
	vstr.32	s1, [r7]
	vldr.32	s14, [r7, #4]
	vldr.32	s15, [r7]
	vadd.f32	s15, s14, s15
	vstr.32	s15, [r7, #12]
	nop
	adds	r7, r7, #20
	mov	sp, r7
	@ sp needed
	ldr	r7, [sp], #4
	bx	lr
	.size	add, .-add
	.ident	"GCC: (Ubuntu/Linaro 7.2.0-6ubuntu1) 7.2.0"
	.section	.note.GNU-stack,"",%progbits
