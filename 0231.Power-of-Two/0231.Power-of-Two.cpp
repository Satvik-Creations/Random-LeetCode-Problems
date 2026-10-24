#include <iostream>
#include <cmath>

using namespace std;
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0) {
            return false;
        }
        else if (n == 1) {
            return true;
        }
        else {
            int i = 1;
            while (pow(2,i) <= n) {
                if (pow(2,i) == n) {
                    return true;
                }
                i += 1;
            }
            return false;
        }
    }
};

