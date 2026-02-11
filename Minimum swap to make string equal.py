class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        n = len(s2)
        total = Counter(s1+s2)
        freq1 = Counter(s1)
        freq2 = Counter(s2)
        new_s1,new_s2 = [],[]
        for j in range(n):
            if s1[j] != s2[j]:
                new_s1.append(s1[j])
                new_s2.append(s2[j])
        new_s1,new_s2 = "".join(new_s1),"".join(new_s2)
        new_n = len(new_s1)
        xy = True
        i = 0
        print(new_s1)
        print(new_s2)
        i = 0
        swap = 0
        new_n = len(new_s1)
        while i < new_n:
            curr1 = new_s1[i:i+2]
            curr2 = new_s2[i:i+2]
            if curr1 == 'xy' and curr2 == 'yx' or curr2 == 'xy' and curr1 == 'yx':
                swap += 1
                i += 2
            elif curr1 == 'xx' and curr2 == 'yy' or curr2 == 'xx' and curr1 == 'yy':
                i += 2
            else:
                i+=1
        if new_n % 2 :
            return -1
        return  new_n // 2 + 1 if swap % 2 else new_n//2
        
        
