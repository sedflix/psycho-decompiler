main:
	push	{r7}
	sub	sp, sp, #20
	add	r7, sp, #0
	movs	r3, #1
	str	r3, [r7, #8]
	movs	r3, #2
	str	r3, [r7, #12]
	b	.L2
.L3:
	ldr	r3, [r7, #4]
	adds	r3, r3, #1
	str	r3, [r7, #4]
.L2:
	ldr	r2, [r7, #8]
	ldr	r3, [r7, #12]
	cmp	r2, r3
	bgt	.L3
	ldr	r3, [r7, #4]
	mov	r0, r3
	adds	r7, r7, #20
	mov	sp, r7
	ldr	r7, [sp], #4
	bx	lr
