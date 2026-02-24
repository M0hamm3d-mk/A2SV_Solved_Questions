class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if sum(skill) % (len(skill) / 2) != 0:
            return -1
        target = sum(skill) / (len(skill) / 2)
        skill.sort()
        left = 0
        sums = 0
        right = len(skill) - 1
        single = 0
        while left < right:
            if skill[left] + skill[right] == target:
                sums += (skill[left] * skill[right])
                left += 1 
                right -= 1
            elif skill[left] + skill[right] > target:
                right -= 1
                single += 1
            elif skill[left] + skill[right] < target:
                single += 1
                left += 1
        if single > 0:
            return -1
        return sums
