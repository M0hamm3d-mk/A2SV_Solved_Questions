class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I' : 1,
            'V' : 5,
            'X'  : 10,
            'L'  : 50,
            'C'  : 100,
            'D' : 500,
            'M'  : 1000
                    }
        res = 0
        i = 0
        while i < len(s):
            if s[i:i+2] == 'IV':
                res +=  4
                i += 2
            elif s[i:i+2] == 'IX':
                res +=  9
                i += 2
            elif s[i:i+2] == 'XL':
                res +=  40
                i += 2
            elif s[i:i+2] == 'XC':
                res +=  90
                i += 2
            elif s[i:i+2] == 'CD':
                res +=  400
                i += 2
            elif s[i:i+2] == 'CM':
                res +=  900
                i += 2
            else:
                res += roman_to_int[s[i]]
                i += 1
        return res
