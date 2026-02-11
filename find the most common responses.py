class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        temp = []
        for i in responses:
            temp.extend(list(set(i)))
        freq = Counter(temp)
        temp.sort(key=lambda a:(-freq[a],a))
        return temp[0]
