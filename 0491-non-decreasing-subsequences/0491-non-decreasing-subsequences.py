class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        # nums.sort()
        seen = set()
        def backTrack(index,path):
            if len(path) >= 2 and tuple(path) not in seen:
                for j in range(1,len(path)):
                    if path[j-1] > path[j]:
                        break
                else:
                    res.append(path[:])
                    seen.add(tuple(path[:]))
            if index == len(nums):
                return
            for i in range(index,len(nums)):
                path.append(nums[i])
                backTrack(i+1,path)
                path.pop()
        backTrack(0,[])

        return res
