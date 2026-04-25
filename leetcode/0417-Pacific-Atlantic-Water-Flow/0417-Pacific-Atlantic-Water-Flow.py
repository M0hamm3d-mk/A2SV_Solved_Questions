class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m

        pac = set()
        atl = set()
        ans = []
        def dfs(row,col,visit):
            stack = [[row,col]]
            while stack:
                r,c = stack.pop()
                h = heights[r][c]
                visit.add((r,c))
                for i,j in directions:
                    nr = r + i
                    nc =  c + j

                    if not inbound(nr,nc) or (nr,nc) in visit or heights[nr][nc] < h:
                        continue
                    else:
                        visit.add((nr,nc))
                        stack.append([nr,nc])


        for c in range(m):
            dfs(0,c,pac)
            dfs(n-1,c,atl)
        for r in range(n):
            dfs(r,0,pac)
            dfs(r,m-1,atl)

        for i in range(n):
            for j in range(m):
                if (i,j) in pac and (i,j) in atl:
                    ans.append([i,j])
        return ans