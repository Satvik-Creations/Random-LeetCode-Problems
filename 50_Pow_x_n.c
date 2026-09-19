double myPow(double x, int n) {
    if (x == 0) return 0.0;
    if (n == 0) return 1.0;
    if (x == 1) return 1.0;
    if (x == -1 && n%2 == 0) return 1.0;
    if (x == -1 && n%2 != 0) return -1.0;

    long BinForm = n;
    if (n<0) {
        x = 1/x;
        BinForm = -BinForm;
    }

    double ans = 1;

    while (BinForm > 0) {
        if (BinForm %2 == 1) {
            ans *= x;
        }
        x = x*x;
        BinForm /= 2;
    }

    return ans;
}