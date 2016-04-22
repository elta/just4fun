#! /usr/bin/python

import random

nums = random.sample(range(1, 100), 5)

print nums

if nums[0] > nums[1]:
    tmp = nums[1]
    nums.remove(tmp)
    nums.insert(0, tmp)

if nums[1] > nums[2]:
    tmp = nums[2]
    nums.remove(tmp)
    if nums[0] > nums[2]:
        nums.insert(0, tmp)
    else:
        nums.insert(1, tmp)


if nums[3] > nums[4]:
    tmp = nums[4]
    nums.remove(tmp)
    nums.insert(3, tmp)

if nums[1] < nums[3]:
    if nums[2] < nums[3]:
        print nums[2]
    else:
        print nums[3]
else:
    if nums[1] < nums[4]:
        print nums[1]
    else:
        print nums[4]
