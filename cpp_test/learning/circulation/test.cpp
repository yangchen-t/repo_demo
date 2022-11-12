#include <iostream>

using namespace std;

// int third_count(int a);
int mi(int a);
int computer(int a);
int function_get(int a);

int main(){
    
    function_get(999);

    return 0;
}


int function_get(int a){

    int number = 100; 
    do{
        computer(number);
        // cout << number << endl;
        number++;
    }while (number < a);
    return computer(number);
}
 
int computer(int a){
    int ge = 0;
    int bai = 0;
    int qian = 0;

    ge = a % 10;
    bai = a / 10 % 10;
    qian = a / 100;

    // cout << ge << bai << qian << endl;
    if (mi(ge) + mi(bai) + mi(qian) == a ){
        cout << a << endl; 
    }

    return a;
}

int mi(int a){
    return a * a * a;
}





// int third_count(int a){
//     int number = 1;
//     int count = 0;
//     int jishu = 0;

//     while (number < a){
//         count = mi(number);
//         ++number;
//         if (count < 1000){
//             if (count > 100){
//                 ++jishu;
//                 cout << "水仙花数： " << count << endl;
//             }
//         }
//         else{
//             cout << "共有： " << jishu << "水仙花数" << endl;
//             break;
//         }
//     }
//     return  0;
// }
