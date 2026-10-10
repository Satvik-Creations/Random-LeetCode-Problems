int climbStairs(int n) {
    int i;

    if (n<=2)
        return n;

    int stepA = 1, stepB = 2, stepC;

    for (i = 3; i<=n; i++) {
        stepC = stepA + stepB;
        stepA = stepB;
        stepB = stepC;
    }
    return stepB;
}

