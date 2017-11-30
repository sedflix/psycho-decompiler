main:
	push	{r7}
	sub	sp, sp, #12
	add	r7, sp, #0
	movs	r3, #0
	str	r3, [r7]
	movs	r3, #1
	str	r3, [r7, #4]
	ldr	r3, [r7]
	cmp	r3, #1
	ble	.L3
	ldr	r3, [r7]
	addw	r3, r3, #465
	str	r3, [r7]
	ldr	r3, [r7, #4]
	cmp	r3, #1
	ble	.L3
	ldr	r3, [r7]
	adds	r3, r3, #2
	str	r3, [r7]
.L3:
	nop
	adds	r7, r7, #12
	mov	sp, r7
	ldr	r7, [sp], #4
	bx	lr
