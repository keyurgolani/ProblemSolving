//
// Created by Keyur Golani on 5/31/17.
//

#include <iostream>
using namespace std;

static int addNumbers(int * values, int length) {
    int answer = 0;
    for(int i = 0; i < length; i++) {
        answer += values[i];
    }
    return answer;
}
