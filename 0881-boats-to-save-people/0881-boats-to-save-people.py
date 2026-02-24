class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        boats = 0
        j = len(people)-1
        i = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            boats += 1
            i += 1
        return boats

