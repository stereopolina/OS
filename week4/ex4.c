#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(void)
{
    int len = 256;
    char command[len];
    char* com = command;
    getline(&com, &len, stdin);
    while(1)
    {
        printf(">>");
        fgets(command, len, stdin);
        system(command);


    }

    //return 0;
}

