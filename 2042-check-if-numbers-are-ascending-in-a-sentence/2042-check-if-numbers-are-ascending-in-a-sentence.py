class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num = []
        temp = ''
        for i in range(len(s)):
            if s[i].isdigit():
                temp += s[i]
                # print(temp)
            else:
                if temp:
                    num.append(int(temp))
                    temp = ''
        if temp:
            num.append(int(temp))
        if len(set(num)) < len(num):
            return False
        return sorted(num) == num
            