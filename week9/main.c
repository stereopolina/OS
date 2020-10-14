#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
    int num = 0;
    printf("How many pages do you want: \n");
    scanf("%d",&num);
    int m = 0;
    int h = 0;
    FILE *file;
    file = fopen("osLab9.txt", "r");
    int *frames = (int*)calloc(num, sizeof(int));
    memset(frames, 0, num);
    int *ages = (int*)calloc(num, sizeof(int));
    memset(ages, 0, num);
    int checker = -432;
    printf("%d", fscanf(file, "%d", &checker));
    while (fscanf(file, "%d", &checker) != EOF) {
        int numf = -432;
        for (int i = 0; i < num; i++) {
            if (checker == frames[i]) {
                numf = i;
                break;
            }
        }
        if(numf != -432)
        {
            h++;
            ages[numf] >>= 1;
            ages[numf] |= 1 << 7;
        }
        else{
            m++;
            int minim = 0;
            for (int i = 0; i < num; i++)
            {
                if (ages[i] < ages[minim])
                {
                    minim = i;
                }
            }
            frames[minim] = checker;
            ages[minim] = 0;
            ages[minim]  |= 1 << 7;
        }
    }
    if(m != 0){
        double h1 = h;
        double m1 = m;
        printf("hit/miss ratio: %lf\n", h1 / m1);
    }
    fclose(file);
    return 0;
}
