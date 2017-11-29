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
	.global	add
	.syntax unified
	.thumb
	.thumb_func
	.fpu vfpv3-d16
	.type	add, %function
add:
	@ args = 0, pretend = 0, frame = 24
	@ frame_needed = 1, uses_anonymous_args = 0
	@ link register save eliminated.
	push	{r7}
	sub	sp, sp, #28
	add	r7, sp, #0
	vstr.32	s0, [r7, #20]
	vstr.32	s1, [r7, #16]
	vstr.32	s2, [r7, #12]
	vstr.32	s3, [r7, #8]
	vstr.32	s4, [r7, #4]
	vldr.32	s14, [r7, #20]
	vldr.32	s15, [r7, #16]
	vadd.f32	s15, s14, s15
	vstr.32	s15, [r7, #12]
	ldr	r3, [r7, #12]	@ float
	vmov	s15, r3
	vmov.f32	s0, s15
	adds	r7, r7, #28
	mov	sp, r7
	@ sp needed
	ldr	r7, [sp], #4
	bx	lr
	.size	add, .-add
	.align	1
	.global	main
	.syntax unified
	.thumb
	.thumb_func
	.fpu vfpv3-d16
	.type	main, %function
main:
	@ args = 0, pretend = 0, frame = 40
	@ frame_needed = 1, uses_anonymous_args = 0
	push	{r4, r7, lr}
	sub	sp, sp, #44
	add	r7, sp, #0
	adr	r4, .L4
	ldrd	r3, [r4]
	strd	r3, [r7, #8]
	adr	r4, .L4+8
	ldrd	r3, [r4]
	strd	r3, [r7, #16]
	vldr.64	d6, [r7, #8]
	vldr.64	d7, [r7, #16]
	vadd.f64	d7, d6, d7
	vstr.64	d7, [r7, #24]
	adr	r4, .L4+16
	ldrd	r3, [r4]
	strd	r3, [r7, #32]
	vldr.64	d7, [r7, #8]
	vcvt.f32.f64	s13, d7
	vldr.64	d7, [r7, #16]
	vcvt.f32.f64	s12, d7
	vldr.64	d7, [r7, #24]
	vcvt.f32.f64	s11, d7
	vldr.64	d7, [r7, #32]
	vcvt.f32.f64	s10, d7
	vldr.64	d7, [r7, #8]
	vcvt.f32.f64	s15, d7
	vmov.f32	s4, s15
	vmov.f32	s3, s10
	vmov.f32	s2, s11
	vmov.f32	s1, s12
	vmov.f32	s0, s13
	bl	add(PLT)
	vstr.32	s0, [r7, #4]
	nop
	adds	r7, r7, #44
	mov	sp, r7
	@ sp needed
	pop	{r4, r7, pc}
.L5:
	.align	3
.L4:
	.word	3607772529
	.word	1075114147
	.word	2824370494
	.word	1075399989
	.word	1264438372
	.word	1080887240
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.2.0-6ubuntu1) 7.2.0"
	.section	.note.GNU-stack,"",%progbits
