# https://leetcode.com/problems/jump-game/
# best solution
# 0   unknown
# 1   good
# 2   bad

import json
import time

start = time.time()


def can_jump(nums, p, mem):
    last_pos = len(nums)-1

    for i in range(len(nums) - 1, -1, -1):
        if(i + nums[i] >= last_pos):
            last_pos = i
    return last_pos == 0


# with open("./input.json", "r") as f:
#     nums = json.load(f)

nums = [9, 4, 2, 1, 0, 2, 0]

print(nums)

mem = [0 for i in range(len(nums))]
mem[-1:] = [1]


print(can_jump(nums, 0, mem))

print(mem)
print(time.time()-start)
