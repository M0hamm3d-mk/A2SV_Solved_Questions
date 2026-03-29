class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = [[]]
        def backTrack(first,path):
            if path :
                res.append(path[:])

            

            for i in range(first,len(nums)):
                if i == first or i > first and  nums[i] != nums[i-1]:
                    path.append(nums[i])
                    backTrack(i+1,path)
                    path.pop()

        backTrack(0,[])
        return res

