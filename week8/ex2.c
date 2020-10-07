#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/resource.h>
#include <string.h>
#include <math.h>
#include <zconf.h>

int main()
{
    for(int i = 0; i != 10; i++)
    {
        memset(calloc(pow(2, 20) * 10, 1), 0, 10 * pow(2, 20));
        sleep(1);
    }

    return 0;
}

//ex2: after running with vm_stat it seems like so& si are 0-s (I am not sure
//was it correct or not), free memory seems to decrease(not always) and active decreases.



//ex3:MEM increases, cpu usage percentage increases, the number of processes +2, sys and idle decrease
//VM decreases and the amount of physical memory used grows