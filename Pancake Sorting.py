class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for n in range(len(arr),0,-1):
            index = arr.index(n)
            if index == n - 1:
                continue
            elif index == 0:
                arr = arr[:n][::-1] + arr[n:]
                flips.append(n)
            else:
                arr = arr[:index+1][::-1]+arr[index+1:]
                flips.append(index+1)
                arr = arr[:n][::-1] + arr[n:]
                flips.append(n)
        return flips
