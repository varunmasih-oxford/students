#include <stdio.h>


int main(){

    // To manage data - 1. data types 2. variables
    // text - char/string, number - int/float/double, boolean - 0/1
    
    // software - 1010 -> mechine store(location:101b01n) / retrive -> machine -> 1010

    // as developer - we use variables(named memory location) 
    
    // int num = 1010;
    // printf("%d", num*2);
    // int num = 1010;
    // int cal = num*2;

    // printf("%d\n", num);
    // printf("%d", cal);
    
    // char a = 'R';
    // printf("%c\n", a);

    // float b = 10.10;
    // printf("%.2f", b);

    // Operators & Expressions
    // Arithmetic Operators
    // printf("%d\n", 10+20);
    // printf("%d\n", 10*20);
    // // printf("%.2f\n", (float)11/2);
    // printf("%.d\n", 11%2);
    
    // Relational Operators
    // printf("%d\n", 11>2);
    // printf("%d\n", 11<2);
    // printf("%d\n", 11<=11);
    // printf("%d\n", 11==11);
    // printf("%d\n", 11!=110);
    
    // Logical Operators
    // printf("%d\n", 11>10 && 110<20);
    // &&
    // True + True = True
    // True + False = False
    // False + True = False
    // False + False = False
    
    // printf("%d\n", 11>10 || 110<20);
    // ||
    // True + True = True
    // True + False = True
    // False + True = True
    // False + False = False
    
    // printf("%d\n", !(11>10));
    // !
    // !True=False
    // !False=True
    
    // Assignment Operators
    // int a = 10;
    // a *=  100; // re-assign or update value
    // printf("%d\n", a);

    // conditions
    int x = 500;
    // printf("%d\n", x != 50);
    
    // if(x == 50){
    //     printf("Yess\n");
    // }
    
    // if(x>50){
    //     printf("%.2f\n", (float)x*0.1);
    // }
    
    // if(x>500){
    //     printf("%.2f\n", (float)x*0.1);
    // }else{
    //     printf("The value is not greater then 500");

    // }

    // int marks = 96;
    // if(marks>95){
    //     printf("Eligible");
    // }else{
    //     printf("Not Eligible");
    // }

    int rank = 5;
    if(rank == 1){
        printf("Rs 1000\n");
    }else if(rank == 2){
        printf("Rs 800\n");
    }else if(rank == 3){
        printf("Rs 500\n");
    }else{
        printf("Certificate\n");
    }
    return 0;
}
