class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        op = 0
        if maxDoubles == 0:
            return target - 1
        while target > 1:
            if target % 2 == 0 and maxDoubles:
                target //= 2
                maxDoubles -= 1
                if not maxDoubles:
                    return target + op
            else:
                target -= 1
            op += 1
        return op