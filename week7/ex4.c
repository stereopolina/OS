#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
void*  reallocPolina(void *a1, size_t n2)
{
    size_t n1 = sizeof(a1);
    if (a1 == NULL)
    {
        return malloc(n2);
    }
    else if (n2 == 0)
    {
        free(a1);
        return NULL;
    }
    else if (n1 >= n2)
    {
        return a1;
    }
    else
    {
        void* a2 = malloc(n2);
        if (a2)
        {
            memcpy(a2, a1, n1);
            free(a1);
        }
        return a2;
    }
}
//did main from the previous exercise to check the work-ability
//int main(){
//    printf("Enter original array size:");
//    int n1=0;
//    scanf("%d",&n1);
//    int* a1 = malloc(n1* sizeof(int));
//    for(int i=0; i<n1; i++){
//        a1[i]=100;
//        printf("%d ",a1[i]);
//    }
//    printf("\nEnter new array size: ");
//    int n2=0;
//    scanf("%d",&n2);
//    a1 = (int*)reallocPolina(a1, n2);
//    if(n2 > n1)
//    {
//        for(int i=0; i<n2; i++){
//            a1[i]=0;
//        }
//    }
//    for(int i =0; i<n2;i++){
//        printf("%d ",a1[i]);
//    }
//    printf("\n");
//    free(a1);
//    return 0;
//}
