class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        directory = []
        for p in paths:
            directory.append(p.split())
        all_files = []
        for i in range(len(directory)):
            for j in range(1, len(directory[i])):
                all_files.append([directory[i][0]+'/'+directory[i][j][:directory[i][j].index(
                    '(')], directory[i][j][directory[i][j].index('('):]])
        duplicated = []
        all_files.sort(key=lambda a: a[1])
        curr = all_files[0][1]
        duplicated.append([all_files[0][0]])
        for i in range(1, len(all_files)):
            if all_files[i][1] != curr:
                duplicated.append([all_files[i][0]])
                curr = all_files[i][1]
            else:
                duplicated[-1].append(all_files[i][0])
        ans = []
        for d in duplicated:
            if len(d) >= 2:
                ans.append(d)
        return ans
