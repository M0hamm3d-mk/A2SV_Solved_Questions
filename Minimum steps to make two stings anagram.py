class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)
        steps = 0
        for i in t_counter:
            steps += max(0,t_counter[i] - s_counter[i])
        return steps
