class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # used = [False] * len(nums)

        res = [[]]
        seen = set()
        def backTrack(first,path):
            if path and tuple(path) not in seen:
                seen.add(tuple(path))
                res.append(path[:])

            

            for i in range(first,len(nums)):
             
                    path.append(nums[i])
                    backTrack(i+1,path)
                    path.pop()

        backTrack(0,[])
        return res

