class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        s = 'abc'
        def backTrack(path):
            res.append("".join((path[:])))
            if len(path) == n:
                return
            for i in range(3):
                if not path or path[-1] != s[i]:
                    path.append(s[i])
                    backTrack(path)
                    path.pop()
        backTrack([])

        res.sort()
        # print(res)
        ans = []
        for i in res:
            if len(i) == n :
                for j in range(1,n):
                    if i[j-1] == i[j]:
                        break
                else:
                    ans.append(i)
        print(ans)

        return ans[k-1] if k-1 < len(ans) else ''