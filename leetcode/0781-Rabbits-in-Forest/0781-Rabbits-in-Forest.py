class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        ans = 0
        for k,v in freq.items():
            ans += (v*k) % (k+1)
        return ans + len(answers)