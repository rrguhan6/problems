# https://leetcode.com/problems/permutations/submissions/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def fun(start, n, l):
            if(start == n):
                x = [*l]
                ans.append(x)
                return
            for i in range(start, n):
                l[i], l[start] = l[start], l[i]

                fun(start+1, n, l)

                l[i], l[start] = l[start], l[i]

        fun(0, len(nums), nums)
        return ans
