#include <stdio.h>
#include <float.h>
#include <limits.h>
#include <string.h>
int main()
{
    char a[100];
    char b[100];
    scanf("%s", a);
    int j = strlen(a);
    for(int i = strlen(a) - 1; i >= 0; i--)
    {
        //printf("%c\n", a[i - 1]); //it outputs chars line by line
        // - wanted to make a single word instead - another char array
        b[j - i - 1] = a[i];
    }
    printf("%s", b);
    return 0;
}