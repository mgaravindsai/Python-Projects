import time
from random import randrange

def findmin(alist):
    ismin = alist[0]

    for i in alist:
        isSmaller = True
        for j in alist:
            if i > j:
                isSmaller = False
        if isSmaller:
            ismin = i
    return ismin

def findmin_n(alist):
    ismin = alist[0]
    for i in alist:
        if i < ismin:
            ismin = i
    return ismin

def Anagram(s1,s2):
    fnd = False
    for i in s1:
        if s2.count(i) >=1:
            fnd = True
        else:
            fnd = False
            break
    return fnd

print(Anagram('earth','heart'))

for listsize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listsize)]
    start = time.time()
    foundmin = findmin(alist)
    end = time.time()
    #print("size {} time {} foundvalue {}".format(listsize,end-start,foundmin))
    starts = time.time()
    foundminn = findmin_n(alist)
    ends = time.time()
    #print("size {} time {} foundminn {}".format(listsize,ends-starts,foundminn))
    