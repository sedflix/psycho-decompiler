main:
	push	{r4, r7, lr}
	sub	sp, sp, #28
	add	r7, sp, #0
	ldr	r4, .L4
.LPIC0:
	add	r4, pc
	ldr	r3, .L4+4
	ldr	r3, [r4, r3]
	ldr	r3, [r3]
	str	r3, [r7, #20]
	movs	r3, #0
	str	r3, [r7, #8]
	movs	r3, #1
	str	r3, [r7, #12]
	movs	r3, #0
	str	r3, [r7, #16]
	adds	r3, r7, #4
	mov	r1, r3
	ldr	r3, .L4+8
.LPIC1:
	add	r3, pc
	mov	r0, r3
	bl	__isoc99_scanf(PLT)
.L2:
	ldr	r2, [r7, #8]
	ldr	r3, [r7, #12]
	add	r3, r3, r2
	str	r3, [r7, #8]
	ldr	r2, [r7, #8]
	ldr	r3, [r7, #12]
	subs	r3, r2, r3
	str	r3, [r7, #12]
	ldr	r1, [r7, #8]
	ldr	r3, .L4+12
.LPIC2:
	add	r3, pc
	mov	r0, r3
	bl	printf(PLT)
	movs	r0, #32
	bl	putchar(PLT)
	ldr	r3, [r7, #16]
	adds	r3, r3, #1
	str	r3, [r7, #16]
	ldr	r3, [r7, #4]
	ldr	r2, [r7, #16]
	cmp	r2, r3
	bne	.L2
	nop
	ldr	r3, .L4+4
	ldr	r3, [r4, r3]
	ldr	r2, [r7, #20]
	ldr	r3, [r3]
	cmp	r2, r3
	beq	.L3
	bl	__stack_chk_fail(PLT)
.L3:
	adds	r7, r7, #28
	mov	sp, r7
	pop	{r4, r7, pc}