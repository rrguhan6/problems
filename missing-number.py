# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n*(n+1))/2
        cur_sum = sum(nums)
        return int(total-cur_sum)
