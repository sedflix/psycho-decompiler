#include <stdio.h>

void main(){

int v1=0, v2=1, v3=0, v4;
scanf("%d",&v4);
do {
v1 = v1+v2;
v2 = v1-v2;
printf("%d",v1);
printf(" ");
v3 = v3+1;
} while(v3!=v4);

}
