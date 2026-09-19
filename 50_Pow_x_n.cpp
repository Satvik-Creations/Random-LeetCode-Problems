class Solution {
public:
    double myPow(double x, int n) {

        // General/Basic Cases
        if (x == 0) return 0.0;
        if (x == 1) return 1.0;
        if (n == 0) return 1.0;
        if (x == -1 && n%2 == 0) return 1.0;
        if (x == -1 && n%2 != 0) return -1.0;

        long BinForm = n;
        double ans = 1;

        // Negative Case Handling
        if (n<0) {
            x = 1/x;
            BinForm = -BinForm;
        }

        // Positive Case Handling
        while (BinForm > 0) {
            if (BinForm %2 == 1) {
                ans *= x;
            }

            x *= x;
            BinForm /= 2;
        }
        return ans;
    }
};