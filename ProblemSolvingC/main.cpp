#include <iostream>
#include "Module1.cpp"
using namespace std;

int main() {
    int length = 0;
    cout << "Enter number count" << endl;
    cin >> length;
    int * values = new int[length];
    int i = 0;
    for (int value; cin >> value; i++) {
        values[i] = value;
        if(i == length - 1) {
            break;
        }
    }
    cout << addNumbers(values, length) << endl;
    return 0;
}