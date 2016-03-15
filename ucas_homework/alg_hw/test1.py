#! /usr/bin/python

def exchange(s = list(), start = 0, shift = 1):
    size = len(s)
    space = s[start]

    preIndex = start
    curIndex = start

    maxNum = 10

    for i in range(1, 15)[::-1]:
        curIndex = (preIndex + size - shift) % size

#        print "%d %d" %(preIndex, curIndex)
        if (curIndex == start):
#            print "%d = %d" %(preIndex, space)
            s[preIndex] = space
            break
        else:
#            print "%d = %d" %(preIndex, s[curIndex])
            s[preIndex] = s[curIndex]

        preIndex = curIndex

    print s

    return s


a = range(0, 10)
shift = 2

loopTime = shift
tmp = 0
while loopTime > 1:
    tmp = len(a) % loopTime
    if tmp == 0:
        break

    loopTime = tmp

print "Loop time is ", loopTime

for i in range(0, loopTime):
    a = exchange(a, i, shift)
