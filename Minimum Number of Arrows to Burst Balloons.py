class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # we need to remove overlap intervals
        n = len(points)
        points.sort()
        non_overlap_points = [points[0]]

        for i in range(1,n):

            curr_start = points[i][0]
            curr_end = points[i][1]
            pre_start = non_overlap_points[-1][0]
            pre_end = non_overlap_points[-1][1]

            if curr_start <= pre_end: # minimizing the aim towards the common range
                non_overlap_points[-1][0] = max(curr_start,pre_start)
                non_overlap_points[-1][1] = min(curr_end,pre_end)

            else:
                non_overlap_points.append(points[i])


        return len(non_overlap_points)
