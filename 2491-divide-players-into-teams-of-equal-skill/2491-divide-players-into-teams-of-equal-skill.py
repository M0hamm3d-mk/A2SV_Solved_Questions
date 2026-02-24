class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        mid = len(skill)//2
        left,right = 0,len(skill)-1
        chemistry = 0
        total_chemistry = 0

        while left < mid and right >= mid:
            if skill[left] + skill[right] != chemistry and chemistry != 0:
                return -1
            chemistry = skill[left] + skill[right]
            total_chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
            
        return total_chemistry

