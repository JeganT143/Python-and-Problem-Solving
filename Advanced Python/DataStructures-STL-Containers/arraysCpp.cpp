#include<iostream>
using namespace std;


// Passing array to a function
// Array is passed by reference

void updateArray(int arr[], int i, int value){
    arr[i] = value;
}

// Size of the array should be passed as a separate parameter to the function, because the array decays to a pointer when passed to a function, and we lose the information about its size.
void printArray(int arr[], int size){
    for(int i=0; i<size; i++){
        cout<<arr[i]<<" ";
    }
}

int main(){
    int arr[6] = {1,2,3,4,5};
    int num_of_ele = sizeof(arr)/sizeof(arr[0]);

    printArray(arr, num_of_ele);

    updateArray(arr, 0, 10);

    cout<<endl;

    printArray(arr, num_of_ele);

}