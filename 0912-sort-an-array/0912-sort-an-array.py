class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            n = len(left)
            m = len(right)
            i = j = 0
            merged = []
            while i < n and j < m:
                if left[i] > right[j]:
                    merged.append(right[j])
                    j += 1
                else:
                    merged.append(left[i])
                    i += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged


        def mergeSort(arr):
            n = len(arr)
            if n <= 1:
                return arr
            mid = n//2
            left = arr[:mid]
            right = arr[mid:]

            return merge(mergeSort(left),mergeSort(right))
        return mergeSort(nums)