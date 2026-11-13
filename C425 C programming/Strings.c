#include<stdio.h>
#include<string.h>

int main(){
// char a = 'A';
// printf("%c" , a);

// output string
char a[] = "A little boy\n";
printf("%s" , a);

// input string

// char s[25]; //declaration of string
// scanf("%s", s); //input string
// printf("%s" , s);

// char name[25];
// scanf("%s", name);
// printf("hello %s", name);

// string methods
char name[25] = "laddu bhai";
// printf("Length of string: %d", strlen(name));
// char second_name[25];
// strcpy(second_name, name);
// printf("Copied string: %s", second_name);
// int result = strcmp(name, "laddu"); // 0 or 1
// printf("Result of comparison: %d", result);
char x[20] = "Hello ";
char y[] = "World";

strcat(x, y);
printf("%s", x);

return 0;
}