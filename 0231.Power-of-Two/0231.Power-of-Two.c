#include <stdio.h>
#include <stdbool.h>

bool isPowerOfTwo(int n) {
    if (n <= 0) {
        return false;
    }
    else if (n == 1) {
        return true;
    }
    else {
        int i = 0;
        while (pow(2,i) <= n) {
            if (pow(2,i) == n) {
                return true;
            }
            i += 1;
        }
        return false;
    }
}