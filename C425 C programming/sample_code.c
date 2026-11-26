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
    printf("%d\n", 10+20);
    printf("%d\n", 10*20);
    // printf("%.2f\n", (float)11/2);
    printf("%.d\n", 11%2);
    
    // Relational Operators
    printf("%d\n", 11>2);
    printf("%d\n", 11<2);
    printf("%d\n", 11<=11);
    printf("%d\n", 11==11);
    printf("%d\n", 11!=110);
    
    // Logical Operators
    printf("%d\n", 11>10 && 110<20);
    // &&
    // True + True = True
    // True + False = False
    // False + True = False
    // False + False = False
    
    printf("%d\n", 11>10 || 110<20);
    // ||
    // True + True = True
    // True + False = True
    // False + True = True
    // False + False = False
    
    printf("%d\n", !(11>10));
    // !
    // !True=False
    // !False=True
    
    // Assignment Operators
    int a = 10;
    a *=  100; // re-assign or update value
    printf("%d\n", a);

    return 0;
}