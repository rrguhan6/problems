# https://leetcode.com/problems/first-missing-positive/submissions/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        if(len(nums) == 0):
            return 1
        for i in range(0, len(nums)):
            if(smallest in nums):
                smallest = smallest+1
            else:
                return smallest

        return smallest
