#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n = 1;
    printf("Please, enter the nimber of digits:");
    scanf("%d", &n);
    int* data = malloc(n * sizeof(int));
    for(int i = 0; i != n; i++)
    {
        data[i] = i;
        printf("%d", data[i]);
    }
    free(data);

}
