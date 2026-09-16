int mySqrt(int x) {
    long long low = 0, high = x, mid;
    
    while (low <= high) {
        mid = (low + high)/2;
        if (mid*mid == x) {
            return mid;
            break;
        }
        else if (x < mid*mid) {
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
    }
    return high;
}