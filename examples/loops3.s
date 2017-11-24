        MOV R0, #1024          ; R0 is input, decreases by factors of 10
        MOV R1, #0             ; R1 is sum of digits
        MOV R2, #0x19000000    ; R2 is constantly 0x1999999A
        ORR R2, R2, #0x00990000
        ORR R2, R2, #0x00009900
        ORR R2, R2, #0x0000009A
        MOV R3, #10            ; R3 is constantly 10
loop:
    UMULL R4, R5, R0, R2   ; R5 is R0 / 10
        UMULL R4, R6, R5, R3   ; R4 is now 10 * (R0 / 10)
        SUB R4, R0, R4         ; R5 is now one's digit of R0
        ADD R1, R1, R4         ; add it into R1
        MOVS R0, R5
        BNE loop
halt:
    B halt