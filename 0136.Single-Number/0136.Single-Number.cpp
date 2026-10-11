#include <vector>

using namespace std;
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int i;

        for (i=0; i < nums.size(); i++) {
            if (count(nums.begin(), nums.end(), nums[i]) == 1) {
                return nums[i];
            }
        }
        return 0;
    }
};

