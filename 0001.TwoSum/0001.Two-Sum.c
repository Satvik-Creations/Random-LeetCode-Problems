/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = malloc(2*sizeof(int));

    for (int i = 0; i < numsSize; i++) {
        for (int j = i+1; j < numsSize; j++) {
            if ((nums[i] + nums[j]) == target) {
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    *returnSize = 0;
    return result;
}

// int main() {
//     int nums[] = {2, 7, 11, 15};
//     int target = 9;
//     int returnSize = 0;

//     int* result = twoSum(nums, 4, target, &returnSize);

//     if (returnSize == 2) {
//         printf("Indices: [%d, %d]\n", result[0], result[1]);
//     } else {
//         printf("No valid pair found.\n");
//     }

//     free(result);
//     return 0;
// }

