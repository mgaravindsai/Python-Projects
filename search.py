import timeit
class search:
    def __init__(self,target,num):
        self.nums = num
        self.target = target

    def squentical_search_unsorted(self):
        found = False
        pos = 0
        while pos < len(self.nums) and not found:
            if self.nums[pos] == self.target:
                found = True
            else:
                pos+=1
            return found

    def squentical_search_sorted(self):
        nums = self.nums
        found = False
        stop = False
        pos = 0
        while pos < len(nums) and not found and not stop:
            if nums[pos] == self.target:
                found = True
            else:
                if nums[pos] > self.target:
                    stop = True
                else:
                    pos+=1
        return found

    def Binary_search(self,nums=[]):
        if nums==[]:
            nums = self.nums
        if len(nums)==0:
            return False
        midpoint = len(nums)//2
        if nums[midpoint]==self.target:
            return True
        elif self.target<midpoint:
            return self.Binary_search(nums[:midpoint])
        elif self.target>midpoint:
            return self.Binary_search(nums[midpoint+1:])


########################################################################################################

t1 = timeit.Timer("Search.squentical_search_unsorted()","from __main__ import Search")
Search = search(13,[1, 2, 32, 8, 17, 19, 42, 13, 0])
for i in range(10):
    x = t1.timeit(number=1000)
    print(x)
print()

########################################################################################################

t2= timeit.Timer("Search_sorted.squentical_search_sorted()","from __main__ import Search_sorted")
Search_sorted = search(13,[0, 1, 2, 8, 13, 17, 19, 32, 42])
for j in range(10):
    y = t2.timeit(number=1000)
    print(y)
print()

########################################################################################################

Binary = search(0,[0, 1, 2, 8, 13, 17, 19, 32, 42])
print(Binary.Binary_search())


        