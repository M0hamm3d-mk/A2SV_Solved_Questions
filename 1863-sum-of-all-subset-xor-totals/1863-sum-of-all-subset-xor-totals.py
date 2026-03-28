class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        def backTrack(first,path):
            temp = 0
            for p in path[:]:
                temp ^= p
            res.append(temp)
            for i in range(first,len(nums)):
                path.append(nums[i])
                backTrack(i + 1 ,path)
                path.pop()
        backTrack(0,[])

        return sum(res)
        