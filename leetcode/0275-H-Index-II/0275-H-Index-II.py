class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations)-1
        lower = -1
        while low <= high:
            mid = (low+high)//2

            if citations[mid] >= len(citations)-mid :
                lower = mid 
                high = mid-1
            else:
                low = mid + 1
        # lower = high

        upper = -1
        low = 0
        high = len(citations)-1
        while low <= high:
            mid = (low+high)//2

            if citations[mid] >= len(citations)-mid :
                upper = mid
            low = mid + 1

        # upper = high
        print(lower,upper)
        return upper - lower + 1 if lower > -1 and upper > -1 else 0