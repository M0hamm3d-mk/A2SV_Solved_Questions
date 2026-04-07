class Solution:
    def findMin(self, nums: List[int]) -> int:
        def devide(left,right):
            
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            return min(devide(left,mid),devide(mid+1,right))
        return devide(0,len(nums)-1)