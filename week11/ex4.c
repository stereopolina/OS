#include <stdio.h>
#include <fcntl.h>
#include <zconf.h>
#include <string.h>
#include <sys/mman.h>
int main(){
        int from = open("/Users/beanie/Desktop/projects/OS/week11/br.txt", O_RDWR); //open from file
        int sz = lseek(from, 0, SEEK_END);
        char *a = (char*)mmap(NULL, sz, PROT_READ, MAP_SHARED, from, 0);
        int to = open("/Users/beanie/Desktop/projects/OS/week11/br.memcpy.txt", O_RDWR);
        ftruncate(to, sz);
        char *b =(char*)mmap(NULL, sz, PROT_READ|PROT_WRITE, MAP_SHARED, to, 0);
        memcpy(b, a, sz);
        return 0;
}


