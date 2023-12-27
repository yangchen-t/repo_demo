#include <stdio.h>

int main()
{
    const float OFFSET = 0.3048;
    float CI = 0;
    float YI = 0;
    scanf("%f %f",&YI, &CI);
    float hight = ((YI + CI / 12)*OFFSET);
    printf("%f",hight);
    return 0;
}