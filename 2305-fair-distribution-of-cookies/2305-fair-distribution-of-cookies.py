class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        total = [0] * k
        ans = float('inf')
        def dfs(idx):
            nonlocal ans
            if idx == len(cookies):
                ans = min(ans,max(total))
                return
                
            seen = set()
            for i in range(k):
                if total[i] not in seen:
                    seen.add(total[i])
                    total[i] += cookies[idx]
                    dfs(idx + 1)
                    total[i] -= cookies[idx]
        dfs(0)
        return ans
