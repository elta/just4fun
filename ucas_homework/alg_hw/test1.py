#! /usr/bin/python

def exchange(s = list(), start = 0, shift = 1):
    size = len(s)
    space = s[start]

    stepLen = size
    stepTmp = size

    preIndex = start
    curIndex = start

    maxNum = 10

    for i in range(1, 15)[::-1]:
        curIndex = (preIndex + size - shift) % size

        print "%d %d" %(preIndex, curIndex)
        if (curIndex == start):
            print "%d = %d" %(preIndex, space)
            s[preIndex] = space
            break
        else:
            print "%d = %d" %(preIndex, s[curIndex])
            s[preIndex] = s[curIndex]

        stepTmp = size - curIndex
        if stepTmp < stepLen:
            stepLen = stepTmp

        preIndex = curIndex

    if stepLen != 1:
        print "Need loop, step len is %d" %stepLen

    print s

    return stepLen

a = range(0, 10)
shift = 4

stepLen = exchange(a, 0, shift)

for i in range(1, stepLen):
    exchange(a, i, shift)
