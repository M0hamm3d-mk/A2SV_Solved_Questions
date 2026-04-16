class Solution:
    def findErrorNums(self, arr: List[int]) -> List[int]:
        i = 0
        dup = []
        while i < len(arr):
            correct_pos = arr[i] - 1
            if i != correct_pos:
                if arr[i] == arr[correct_pos]:
                    dup = arr[i]
                    i += 1
                else:
                    arr[i],arr[correct_pos] = arr[correct_pos],arr[i]
            else:
                i += 1

        i = 0 
        while i < len(arr):
            if arr[i] != i+1 :
                return [dup,i+1]
            i += 1
