# https://leetcode.com/problems/jump-game/
# best solution


def can_jump(nums):
    last_pos = len(nums)-1

    for i in range(len(nums) - 1, -1, -1):
        if(i + nums[i] >= last_pos):
            last_pos = i
    return last_pos == 0


nums = [9, 4, 2, 1, 0, 2, 0]


print(can_jump(nums))
