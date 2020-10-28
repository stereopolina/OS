#include <stdio.h>
#include <zconf.h>
#include <string.h> // found header and function on http://all-ht.ru/inf/prog/c/func/strlen.html
#include <fcntl.h>
#include <unistd.h> //found headers in https://www.opennet.ru/man.shtml?topic=mmap&category=2&russian=0
#include <sys/mman.h>

int main()
{
    char *str = "This is a nice day";
    FILE *f = fopen("/Users/beanie/Desktop/projects/OS/week11/br.txt", "w");
    ftruncate(fileno(f), strlen(str) + 1);
    int num = open("/Users/beanie/Desktop/projects/OS/week11/br.txt", O_RDWR);
    char *res = mmap(NULL, strlen(str) + 1, PROT_READ|PROT_WRITE, MAP_SHARED, num, 0);
    int i = 0;
    while(i < strlen(str) + 1)
    {
        res[i] = str[i];
        i++;
    }
    fclose(f);
    return 0;
}
