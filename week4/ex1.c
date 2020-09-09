#include <stdio.h>
#include <zconf.h>
#include <stdlib.h>

int main()
{
    pid_t var;
    var = fork();
    int i = 0;
    while(i != 10)
    {
        if(var == 0)
            printf("Hello from child [%d - %d]\n", var, i);
        if(var > 0)
            printf("Hello from parent [%d - %d]\n", var, i);
        if(var < 0)
            return EXIT_FAILURE;
        i++;
    }
    return 0;
}
