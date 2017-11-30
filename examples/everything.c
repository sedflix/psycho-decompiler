
int yehFunctionHain(int c) {
    c = c - 1;
    return c;
}

void main() {
    int a = 1;
    float b = 2;
    int c = 0;

    while ( a < 30) {
        a = a + 1;
        b = b + 1.0;
        if ( a < 20 ) {
            b = b + 1.0;
            if(a%2 == 0) {
                c = c + 1;
            }
        }
    }

    while(c > 0) {
        c = yehFunctionHain(c);
    }
}
