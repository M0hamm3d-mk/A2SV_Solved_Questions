class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            i = j = 0
            n = len(left)
            m = len(right)
            merged = []
            while i < n and j < m:
                if nums[left[i]] > nums[right[j]]:
                    res[left[i]] += m-j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        def devide(arr):
            n = len(arr)
            if n == 1:
                return arr
            mid = n // 2
            return merge(devide(arr[:mid]),devide(arr[mid:]))
        res = [0] * len(nums)

        devide([i for i in range(len(nums))])

        return res