#include <stdio.h>
#include <pthread.h>

void printer()
{
    printf("Created\n");
}
int main()
{
    pthread_t thread;
    int number = 5; //default value
    scanf("How many threads do you want? %d", number);
    for(size_t i = 0; i != number; i++)
    {
        pthread_create(&thread, NULL, &printer, NULL);
        printf("It is %d thread", i);

    }
    pthread_join(thread, NULL);
    return 0;
}