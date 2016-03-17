#! /usr/bin/python

# Greatest common divisor;
def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a

# Exachange list number by couple
def exchange(s = list(), start = 0, shift = 1):
    size = len(s)
    space = s[start]

    preIndex = start
    curIndex = start

    maxNum = 10

    while True:
        curIndex = (preIndex + size - shift) % size

        if (curIndex == start):
            s[preIndex] = space
            break
        else:
            s[preIndex] = s[curIndex]

        preIndex = curIndex

    return s

# Generate loop times
def genLoop(length = 1, shift =1):
    loopTime = shift
    tmp = 0
    while loopTime > 1:
        tmp = length % loopTime
        if tmp == 0:
            break

        loopTime = tmp

    loopTime = loopTime / gcd(loopTime, length)

    print "Loop time is ", loopTime
    return loopTime

# Main function
if __name__ == "__main__":
    a = range(0, 100)
    shift = 7

    loopTime = genLoop(len(a), shift)

    for i in range(0, loopTime):
        a = exchange(a, i, shift)

    print a
