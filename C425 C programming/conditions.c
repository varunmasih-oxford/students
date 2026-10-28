#include <stdio.h>

int main() {
    int x = 10;
    int y = 20;
    // True - 1
    // False - 0
    
    // if (x > y) {
    //     x = x*x;
    //     printf("x(%d) is greater than y(%d)\n", x, y);
    // } else {
    //     printf("y(%d) is greater than x(%d)\n", y, x);
    // }

    // Age group classification
    // 0-19: Teenager
    // 20-39: Young Adult
    // 40-120: old age Adult


    int age = 25;
    if(age >0 && age <=19){
        printf("Teenager\n");
    }else if(age >=20 && age <=39){
        printf("Young Adult\n");
    }else if(age >=40 && age <=120){
        printf("Old Age Adult\n");
    }else{
        printf("Invalid Age\n");
    }
    // switch Statement


    // int num = 1;
    int num = 1;
    printf("Enter a number (1-3): ");
    scanf("%d", &num);



    switch (num) {
        case 1:
            printf("Day 1\n");
            break;
        case  2:
            printf("Day 2\n");
            break;
        case  3:
            printf("Day 3\n");
            break;
        default:
            printf("Invalid Day\n");
    }

    return 0;
}