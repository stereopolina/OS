#include <stdio.h>
#include <zconf.h>

int main()
{
    int i = 0;
    while(i != 3)
    {
        fork();
        i++;
    }
    sleep(5);
    return 0;
}
