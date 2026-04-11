class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = nums
        ans = [0] * len(arr)
        def merge(left_ptr,right_ptr):
            n,m = len(left_ptr),len(right_ptr)
            i = j = 0
            
            merged_arr = []
            # print(left_ptr,'----',right_ptr)
            # cnt = 0
            while i < n and j < m:
                if arr[left_ptr[i]] > arr[right_ptr[j]]:
                    merged_arr.append(right_ptr[j])
                    j += 1
                else:
                    ans[left_ptr[i]] += j
                    merged_arr.append(left_ptr[i])
                    i += 1
            while i < n:
                ans[left_ptr[i]] += j
                merged_arr.append(left_ptr[i])
                i += 1
            merged_arr.extend(right_ptr[j:])
            
            return merged_arr

        def divide(arr):
            n = len(arr)
            if n == 1:
                return arr
            mid = n // 2
            left = divide(arr[:mid])
            right = divide(arr[mid:])
            
            return merge(left,right)

        divide([x for x in range(len(arr))])

        return ans
        
    


                    