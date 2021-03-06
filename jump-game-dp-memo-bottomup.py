# https://leetcode.com/problems/jump-game/
# dp bottom up approuch
# 0   unknown
# 1   good
# 2   bad

import json
import time

start = time.time()


def can_jump(nums, p, mem):
    print(len(nums)-2)
    for i in range(len(nums)-2, -1, -1):
        furthest_jump = min(nums[i] + i, len(nums)-1-i)
        print(nums[i] + i, len(nums)-1-i)
        # breakpoint()
        for j in range(i+1, furthest_jump+1):
            if(mem[j] == 1):
                mem[i] = 1
                break

    return mem[0] == 1


with open("./input.json", "r") as f:
    nums = json.load(f)

nums = nums["input"]


mem = [0 for i in range(len(nums))]
mem[-1:] = [1]


print(can_jump(nums, 0, mem))

print(mem)
print(time.time()-start)
