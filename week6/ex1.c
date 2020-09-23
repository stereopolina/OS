#include <stdio.h>

void WT(int *t,  int n, int *a)
{
    t[0] = 0;
    for (int i=1; i<n; i++ )
        t[i] = a[i - 1] + t[i - 1];
}//waiting time

void TAT(int *t, int n, int *a, int *tat)
{
    for (int i = 0;i < n ; i++)
        tat[i] = a[i] + t[i];
}//turn around time

void avgT(int *num, int n, int *ct)
{
    int wt[n], tat[n], totwt = 0, tott = 0;
    WT(num, ct, wt);
    TAT(num, ct, wt, tat);
    printf("Number  CT  TAT  WT \n");
    for (int i=0; i<n; i++)//to find averages
    {
        totwt = totwt + wt[i];
        tott = tott + tat[i];
        printf("%d\t\t%d\t%d\t%d\n", i+1, ct[i], tat[i], wt[i]);
    }
    printf("Average Turnaround time = %d\n", tott/ n);
    printf("Average waiting time = %d\n", totwt/ n);
}


int main()
{
    int num[] = {1, 2, 3, 4, 5};
    int n = sizeof num / sizeof num[0];
    int ct[] = {13, 245, 11, 153, 3};
    avgT(num, n, ct);
    return 0;
}