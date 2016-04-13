#! /usr/bin/python
import copy;

# Split list to two new list
# [[0, 0], [1, 2], [2, 3], [3, 4], [0, 0]]
# ==>   [[0, 0], [1, 2], [2, 0]] with [[0, 3], [3, 4], [0, 0]]
# and   [[0, 0], [1, 2], [3, 0]] with [[0, 2], [3, 4], [0, 0]]
def splitList(lst=list()):
    length = len(lst)
    length = length / 2

    # Two new list
    la = copy.deepcopy(lst[:length + 1])
    lb = copy.deepcopy(lst[length:])

    # Two copied list, and reverse last value
    lra = copy.deepcopy(la[:])
    lrb = copy.deepcopy(lb[:])

    # Make head and tail to zero
    la[length][1] = 0
    lb[0][0] = 0

    lra[length][0] = lra[length][1]
    lra[length][1] = 0

    lrb[0][1] = lrb[0][0]
    lrb[0][0] = 0

    return [la, lb, lra, lrb]

def sumVal(l=list()):
    retVal = 0
    retLst = list()
    if len(l) > 2:
        splits = splitList(l)

        vAL = sumVal(splits[0])
        vAR = sumVal(splits[1])

        vBL = sumVal(splits[2])
        vBR = sumVal(splits[3])

        sumA = vAL[0] + vAR[0]
        sumB = vBL[0] + vBR[0]

        if sumA > sumB:
            retVal = sumA
            vAL[1][-1][1] = vAR[1][0][1]
            retLst = vAL[1][:] + vAR[1][1:]
        else:
            vBL[1][-1][1] = vBR[1][0][1]
            retLst = vBL[1][:] + vBR[1][1:]
            retVal = sumB
    elif len(l) == 2:
        retVal = l[0][1] * l[1][0]
	retLst = l
    else:
        print "Error!"
        retVal = -1

    return [retVal, retLst]

def countW(lst=list()):
    ret = list()
    for tmp in lst:
        if tmp[0] <= tmp[1]:
	    ret.append(0)
        else:
            ret.append(1)
    return ret

if __name__ == '__main__':
    a = [[0, 0], [5, 8], [4, 2], [9, 6], [7, 7], [3, 9], [11, 10], [0, 0]]

    ret = sumVal(a)

    print "Max value is:", ret[0]
    print "Final order is:", ret[1][1:-1]
    print "Final W value is:", countW(ret[1][1:-1])
