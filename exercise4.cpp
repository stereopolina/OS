#include <stdio.h>
void swap (int& a, int& b)
{
    int c = a;
    a = b;
    b = c;
}
int main()
{
    int a, b;
    printf("Enter a, then enter b: ");
    scanf("%d", &a);
    scanf("%d", &b);
    swap(a, b);
    printf("Now a equals %d   ", a);
    printf("and b equals = %d", b);

    return 0;
}