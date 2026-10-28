#include<stdio.h>

int main(){
    // Looping Statements

    // printf("line of code\n");
    // printf("line of code\n");
    // printf("line of code\n");
    // printf("line of code\n");
    // printf("line of code\n");
    
    // loops
    // initialization; condition; increment/decrement
    
    // for loop
    // for(int x = 11; x <= 15; x++){
    //     printf("line of code %d\n", x);
    // }
    
    // while loop
    // int x = 1;
    // while(x<=5){
        //     printf("line of code %d\n", x);
    //     x++;
    // }
    // do while loop
    // int x = 10;
    // do{
    //     printf("line of code %d\n", x);
    //     x++;
    // }while(x<=5);


    // Break Statement

    // for(int x = 11; x <= 15; x++){
    //     printf("line of code %d\n", x);
    //     if(x == 13){
    //         break;
    //     }
    // }
    
    // continue Statement
    // for(int x = 11; x <= 15; x++){
    //     if(x == 14){
    //         continue;
    //     }
    //     printf("line of code %d\n", x);
    // }

    for(int x = 11; x <= 15; x++){
        if(x % 2 == 0){
            continue;
        }
        printf("line of code %d\n", x);
    }
    return 0;
}