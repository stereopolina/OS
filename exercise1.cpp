#include <stdio.h>
#include <float.h>
#include <limits.h>
int main()
{
    int i = INT_MAX;
    float f = FLT_MAX;
    double d = DBL_MAX; //found out how to declare - need to include limits.h
    printf("Sizes of int, float and double are, respectively, \n %lu\n %lu\n %lu\n",
            sizeof(i),
            sizeof(f),
            sizeof(d));
    printf(" max.int = %d\n max.float = %lf\n max.double = %lf\n", i, f, d);

    return 0;
}