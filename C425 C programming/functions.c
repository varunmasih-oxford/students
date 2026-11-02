#include<stdio.h>

int main(){

    // functions 
    
    // void abc(){
    //     printf("Hello World");
    // }    

    //  abc();
    //  abc();
    //  abc();

    // 1. No Arguments, No Return Value

    // void abc(){
    //     printf("Hello World\n");
    // }
    // abc();


    // // 2. With Arguments, No Return Value
    // void abc(int x){
    //     printf("%d\n", x);
    // }
    // abc(10);
    // abc(100);
    // abc(1000);

    // 3. With Arguments, With Return Value
    // int abc(int x){
    //     int y = x*x;
    //     return y;
    // }

    
    // printf("%d\n", abc(4));
    
    // 4. No Arguments, With Return Value
    int abc(){
        
        return 500;
    }

    
    printf("%d\n", abc());

    
    
    return 0;
}