#include <stdio.h>
#include <float.h>
#include <limits.h>
#include <string.h>

int main()
{
    unsigned short n;
    scanf("%u", &n);
    short i,j;
    for(i = 1;i <= n; i++)
    {
        for(j = 1; j <= 2*n - 1; j++)
        {
            if (j < (n - i + 1) || j > (n + i - 1))
                printf("%c", ' ');
            else
                printf("%c", '*');
        }
        puts("");
    }
    return 0;
}
