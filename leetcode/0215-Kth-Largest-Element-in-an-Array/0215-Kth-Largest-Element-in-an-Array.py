class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        n = len(nums)
        k = n - k

        def quickSelect(l, r):
            pivot = nums[random.randint(l, r)]

            left, i, right = l, l, r
            while i <= right:

                if nums[i] < pivot:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
                    i += 1

                elif nums[i] > pivot:
                    nums[right], nums[i] = nums[i], nums[right]
                    right -= 1
                    
                else:
                    i += 1

            if k < left:
                return quickSelect(l, left - 1)
            elif k > right:
                return quickSelect(right + 1, r)
            else:
                return nums[k]

        return quickSelect(0, n - 1)