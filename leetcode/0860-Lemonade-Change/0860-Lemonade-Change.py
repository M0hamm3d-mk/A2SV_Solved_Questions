class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10 :
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten == 0 and five <= 2:
                    return False
                elif ten >= 1:
                    ten -= 1
                    if five >= 1:
                        five -= 1
                    else:
                        return False
                elif five >= 3:
                    five -= 3
        return True