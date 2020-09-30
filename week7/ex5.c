#include <stdio.h>
int main() {
    char *s;
    char foo[] = "Hello World";
    s = foo;
    printf("s is %s\n", s);
    s = &foo; //Here we store the adress of the foo var
    printf("s[0] is %d\n",s[0]); //here the ascii code is printed
    return(0);
}