class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        boats = 0
        j = len(people)-1
        i = 0
        while i <= j:
            if people[i] == limit:
                boats += 1
            else:
                if people[i] + people[j] <= limit:
                    boats += 1
                    j -= 1
                else:
                    boats += 1
            i += 1
        return boats

