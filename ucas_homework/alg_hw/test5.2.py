#! /usr/bin/python

import random

nums = random.sample(range(1, 100), 5)

print "Generate ", nums

if nums[0] > nums[1]:
    tmp = nums[1]
    nums.remove(tmp)
    nums.insert(0, tmp)

if nums[2] > nums[3]:
    tmp = nums[3]
    nums.remove(tmp)
    nums.insert(2, tmp)

save_num = 0
if nums[0] < nums[2]:
    save_num = nums[1]
else:
    save_num = nums[3]
    tmp = nums[2]
    nums.remove(tmp)
    nums.insert(0,tmp) 

nums.remove(save_num)


tmp = nums[3]
nums.remove(tmp)
if tmp < nums[1]:
    if tmp < nums[0]:
        nums.insert(0, tmp)
    else:
        nums.insert(1, tmp)
else:
    if tmp < nums[2]:
        nums.insert(2, tmp)
    else:
        nums.insert(3, tmp)

if save_num < nums[2]:
    if save_num < nums[1]:
        nums.insert(1, save_num)
    else:
        nums.insert(2, save_num)
else:
    if save_num < nums[3]:
        nums.insert(3, save_num)
    else:
        nums.insert(4, save_num)

print "Final ", nums

