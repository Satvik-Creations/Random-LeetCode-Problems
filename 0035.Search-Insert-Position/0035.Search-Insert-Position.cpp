#include <iostream>
#include <vector>

class Solution {
public:
    int searchInsert(std::vector<int>& nums, int target) {
        int low = 0, mid, high = nums.size() - 1;

        while (low <= high) {
            mid = (low + high) / 2;

            if (target == nums[mid]) {
                return mid;
            }
            else if (target < nums[mid]) {
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return low;
    }
};

