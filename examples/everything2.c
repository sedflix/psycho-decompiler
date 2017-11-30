
int main(int argc) {
  int int_1 = 0;
  int int_2 = 3;
  float float_1 = 23.214;
  float float_2 = 0.32414;

  while (int_1 < 20) {
  int_1 = int_1 + 3;
    while (int_2 < 40) {
        int_2 = int_2 + 2;
       if (int_2%2 == 0) {
          float_1 = float_1 + 1;
       }
    }
  }

  int_1 = 0;
  int_2 = 0;
  float_1 = 0.123;
  float_2 = 6.34;

  while (int_2 < 20) {
   int_2 = int_2 + 3;
    while (int_1 < 40) {
       if (int_2%2 == 0) {
          float_2 = float_2 + 1;
       }
       int_1 = int_1 + 2;
    }
  }

  return 0;
}
