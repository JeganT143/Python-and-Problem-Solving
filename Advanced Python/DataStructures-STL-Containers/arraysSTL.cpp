#include<array>
#include<iostream>
#include<algorithm>
using namespace std;

// All STL containers are passed by value, which means that a copy of the container is created when it is passed to a function.


void updateArray(array<int, 6> arr, int index, int value) {
    arr[index] = value; // Modifying the element at the specified index
}

void updateArrayByReference(array<int, 6>& arr, int index, int value) {
    arr[index] = value; // Modifying the element at the specified index
}

void printArray(const array<int, 6>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " "; // Output the elements of the array
    }
    cout << endl;
}

int main(){
    cout << "Elements of the array: ";
    array<int,6> arr = {1,2,3,4,5};
    updateArrayByReference(arr, 0, 101); // Modifying the first element of the array
    printArray(arr); // Printing the elements of the array
    
    // Sort the array
    sort(arr.begin(), arr.end());
    cout << "Sorted array: ";
    printArray(arr); // Printing the elements of the sorted array

    // Sorting on classical array sort(arr, arr+n)

    int classicalArr[] = {50, 4, 35, 2, 1};
    int n = sizeof(classicalArr) / sizeof(classicalArr[0]);
    sort(classicalArr, classicalArr + n); // Sorting the classical array
    cout << "Sorted classical array: ";
    for (int i = 0; i < n; i++) {
        cout << classicalArr[i] << " "; // Output the elements of the sorted classical array
    }


    array<int, 6> arr2;
    arr2.fill(10); // Filling the array with a specific value
    cout << "\nArray filled with 10: ";
    printArray(arr2); // Printing the elements of the filled array
    
    // for each loop
    for(auto element : arr) {
        cout << element << " "; // Output each element of the array
    }
    
    
    
    
    
    return 0;
}