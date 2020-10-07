#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/resource.h>
#include <string.h>
#include <math.h>
#include <zconf.h>

extern int errno;

int main()
{
    struct rusage * usg = malloc(sizeof(struct rusage));
    for(int i = 0; i != 10; i++)
    {
        memset(calloc(pow(2, 20) * 10, 1), 0, 10 * pow(2, 20));
        if(getrusage(RUSAGE_SELF, usg))
            printf ("Error %d\n", errno);
        printf("ru_maxrss = %ld\n", (*usg).ru_maxrss);
        sleep(1);
    }
    return 0;
}