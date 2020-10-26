class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = [0 for i in range(len(nums))]
        mem[-1:] = [1]

        def can_jump(nums, mem):
            print(len(nums)-2)
            for i in range(len(nums)-2, -1, -1):
                furthest_jump = min(nums[i] + i, len(nums)-1)
                print(nums[i] + i, len(nums)-1-i)
                # breakpoint()
                for j in range(i+1, furthest_jump+1):
                    if(mem[j] == 1):
                        mem[i] = 1
                        break

            return mem[0] == 1

        return can_jump(nums, mem)
