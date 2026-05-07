class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        print(stones)
        while stones:
            if len(stones) == 1:
                return stones[0]
            s1 = stones[0]
            s2 = stones[1]
            if s1 == s2:
                stones.remove(s1)
                stones.remove(s2)
            else:
                stones[0] = s1 - s2
                stones.remove(s2)
            stones.sort(reverse=True)
        return 0
            

