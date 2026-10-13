class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums2 = sorted(nums1)
        n = len(nums2)-1
        if (n+1) % 2 == 0:
            return (nums2[n//2]+nums2[(n//2)+1])/2
        else:
            return nums2[(n+1)//2]


# print(Solution().findMedianSortedArrays([1, 3], [2])) #3
# print(Solution().findMedianSortedArrays([1, 2], [3,4])) #2.5
