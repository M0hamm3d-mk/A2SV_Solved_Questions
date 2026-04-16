class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        i = 0
        dup = []
        while i < len(arr):
            correct_pos = arr[i] - 1
            if i != correct_pos:
                if arr[i] == arr[correct_pos]:
                    dup.append(arr[i])
                    i += 1
                else:
                    arr[i],arr[correct_pos] = arr[correct_pos],arr[i]
            else:
                i += 1
        return list(set(dup))