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
	.file	"everything2.c"
	.text
	.align	1
	.global	main
	.syntax unified
	.thumb
	.thumb_func
	.fpu vfpv3-d16
	.type	main, %function
main:
	push	{r7}
	sub	sp, sp, #28
	add	r7, sp, #0
	str	r0, [r7, #4]
	movs	r3, #0
	str	r3, [r7, #8]
	movs	r3, #3
	str	r3, [r7, #12]
	movw	r3, #46662
	movt	r3, 16825
	str	r3, [r7, #16]	@ float
	movw	r3, #62894
	movt	r3, 16037
	str	r3, [r7, #20]	@ float
	b	.L2
.L5:
	ldr	r3, [r7, #8]
	adds	r3, r3, #3
	str	r3, [r7, #8]
	b	.L3
.L4:
	ldr	r3, [r7, #12]
	adds	r3, r3, #2
	str	r3, [r7, #12]
	ldr	r3, [r7, #12]
	and	r3, r3, #1
	cmp	r3, #0
	bne	.L3
	vldr.32	s15, [r7, #16]
	vmov.f32	s14, #1.0e+0
	vadd.f32	s15, s15, s14
	vstr.32	s15, [r7, #16]
.L3:
	ldr	r3, [r7, #12]
	cmp	r3, #39
	ble	.L4
.L2:
	ldr	r3, [r7, #8]
	cmp	r3, #19
	ble	.L5
	movs	r3, #0
	str	r3, [r7, #8]
	movs	r3, #0
	str	r3, [r7, #12]
	movw	r3, #59245
	movt	r3, 15867
	str	r3, [r7, #16]	@ float
	movw	r3, #57672
	movt	r3, 16586
	str	r3, [r7, #20]	@ float
	b	.L6
.L10:
	ldr	r3, [r7, #12]
	adds	r3, r3, #3
	str	r3, [r7, #12]
	b	.L7
.L9:
	ldr	r3, [r7, #12]
	and	r3, r3, #1
	cmp	r3, #0
	bne	.L8
	vldr.32	s15, [r7, #20]
	vmov.f32	s14, #1.0e+0
	vadd.f32	s15, s15, s14
	vstr.32	s15, [r7, #20]
.L8:
	ldr	r3, [r7, #8]
	adds	r3, r3, #2
	str	r3, [r7, #8]
.L7:
	ldr	r3, [r7, #8]
	cmp	r3, #39
	ble	.L9
.L6:
	ldr	r3, [r7, #12]
	cmp	r3, #19
	ble	.L10
	movs	r3, #0
	mov	r0, r3
	adds	r7, r7, #28
	mov	sp, r7
	@ sp needed
	ldr	r7, [sp], #4
	bx	lr
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.2.0-6ubuntu1) 7.2.0"
	.section	.note.GNU-stack,"",%progbits
