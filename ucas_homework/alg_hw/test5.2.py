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

if nums[3] < nums[0]: # Ordered
    tmp0 = nums[2]
    tmp1 = nums[3]

    nums.remove(tmp0)
    nums.remove(tmp1)

    nums.insert(0, tmp1)
    nums.insert(0, tmp0)
elif nums[0] < nums[2]:
    tmp0 = nums[2]
    if nums[1] < nums[3]:
        nums.remove(tmp0)
        nums.insert(1, tmp0)
    else:
        tmp1 = nums[3]
        nums.remove(tmp0)
        nums.remove(tmp1)
        nums.insert(1, tmp1)
        nums.insert(1, tmp0)
elif nums[2] < nums[0]:
    tmp0 = nums[2]
    if nums[1] < nums[3]:
        nums.remove(tmp0)
        nums.insert(0, tmp0)
    else:
        tmp1 = nums[3]
        nums.remove(tmp0)
        nums.remove(tmp1)
        nums.insert(0, tmp0)
        nums.insert(2, tmp1)



tmp = nums[4]
nums.remove(tmp)

if tmp < nums[1]:
    if tmp < nums[0]:
        nums.insert(0, tmp)
    else:
        nums.insert(1, tmp)
else:
    if tmp < nums[3]:
        if tmp < nums[2]:
            nums.insert(2, tmp)
        else:
            nums.insert(3, tmp)
    else:
        nums.insert(4, tmp)

print "Final ", nums

