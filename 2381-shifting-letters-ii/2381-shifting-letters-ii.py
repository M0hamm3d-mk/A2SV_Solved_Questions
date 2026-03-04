class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n+1)
        for start,end,dxn in shifts:
            if dxn == 1:
                prefix[start] += 1
                prefix[end+1] -= 1
            else:
                prefix[start] -= 1
                prefix[end+1] += 1
        s = list(s)
        _sum = 0
        for i in range(n):
            _sum += prefix[i]
            char = s[i]
            s[i] = chr((ord(char)+ _sum - 97) % 26 +97)
        return "".join(s)