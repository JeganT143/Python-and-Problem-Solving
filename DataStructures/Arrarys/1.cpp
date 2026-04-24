#include <iostream>
using namespace std;

int main(){
    int a[5] = {2,4,6,8,10};
    cout << a[2] << endl;
    cout << *(a+2) << endl;
    cout << 2[a] << endl;

    return 0;
}