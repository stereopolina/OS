#include <stdio.h>
#include <ntsid.h>
#include <pthread.h>

#define n 20

char size[n];
long long int tim;
int place, csleeping, psleeping;
void* prod()
{
    while(1)
    {
        if(place == 20)
        {
            psleeping = 1;
            csleeping = 0;
            printf("done at %lld\n", tim++);
            continue;
        }
        if(psleeping)
            continue;
        size[place] = 'a' + place;
        place++;
    }
    pthread_exit(NULL);
    return NULL;

}
void* con()
{
    while(1)
    {
        if(place == 0)
        {
            psleeping = 0;
            csleeping = 1;
        }
        if(csleeping)
            continue;
        printf("%c", place);
        place--;
    }

}

int main()
{
    csleeping = 1;
    pthread_t pro, cons;
    pthread_create(&pro, NULL, prod, NULL);
    pthread_create(&cons, NULL, con, NULL);
    while(1);
    return 0;
}