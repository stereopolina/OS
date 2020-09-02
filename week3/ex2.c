#include <stdio.h>

void bubbleSort(int n, int* a)
{
    for (int i = n - 1; i != 0; i--)
    {
        for (int j = 0; j < i; j++)
        {
            if (a[j] > a[j + 1])
            {
                int copy = a[j];
                a[j] = a[j + 1];
                a[j+ 1] = copy;
            }
        }
    }
}


int main()
{
    int n, i, j;
    printf("Input the number of symbols: ");
    scanf("%d", &n);
    int a[n];
    printf("Now enter the array: ");
    for(i = 0 ; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    bubbleSort(n, a);
    printf("Now the result: ");
    for(int k = 0; k != n; k++)
    {
        printf(" %d", a[k]);
    }
    return 0;
}
