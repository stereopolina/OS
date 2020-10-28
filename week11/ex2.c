#include <stdio.h>
#include <zconf.h>

int main()
{
//    char text[5] = "Hello";
//    for(int i = 0; i != 5; ++i)
//    {
//        printf("%c", text[i]);
//        sleep(1);
//    }//that works as well, but a simplier approach seems attractive
    printf("H");
    sleep(1);
    printf("e");
    sleep(1);
    printf("l");
    sleep(1);
    printf("l");
    sleep(1);
    printf("o");
    sleep(1);
    setvbuf(stdout, NULL, _IOLBF, BUFSIZ);
    return 0;
}
