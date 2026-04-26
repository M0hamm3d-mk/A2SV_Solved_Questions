class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero,one,two = 0,0,n-1

        while one <= two:
            if nums[one] == 0:
                nums[one],nums[zero] = nums[zero],nums[one]

                zero += 1
                one += 1
            elif nums[one] == 2:
                nums[one],nums[two] = nums[two],nums[one]
                two -= 1
            else:
                one += 1