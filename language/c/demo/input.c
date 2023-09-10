#include <stdio.h>


int main()
{
    int score = 0;
    printf("input a numbers: ");
    scanf("%d", &score);
    int change = 100 - score;
    printf("%d\n",change);
    return 0;
}