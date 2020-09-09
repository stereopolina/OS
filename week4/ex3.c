#include <stdio.h>
#include <stdlib.h>

int main()
{
    int len = 256;
    char command[len];
    char* com = command;
    getline(&com, &len, stdin);
    system(command);

    return 0;
}
