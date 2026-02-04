class Solution:
    def isCovered(ranges,left,right):
        for i in range(left,right+1):
            for j in ranges:
                if i in range(j[0],j[1]+1):
                    break
            else:
                return False
        return True