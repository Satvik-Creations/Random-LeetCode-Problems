#include <iostream>
#include <cmath>

using namespace std;
class Solution {
public:
    double myPow(double x, int n) {
        return std::pow(x,n);
    }
};

int main() {
    Solution sol;
    double result = sol.myPow(2.0,3);
    cout << result << endl;
    return 0;
}
