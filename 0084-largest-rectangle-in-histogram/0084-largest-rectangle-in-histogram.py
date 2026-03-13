class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pre_smaller = [-1] * n
        next_smaller = [-1] * n

        # for each height find where that height is minimum of all others

        # first how far can it be  minimum to the left 
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                pre_smaller[i] = 0
            else:
                pre_smaller[i] = stack[-1] + 1
            stack.append(i)

        # then how far can it be  minimum to the right 
        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                next_smaller[i] = n-1
            else:
                next_smaller[i] = stack[-1] - 1
            stack.append(i)
        # print(pre_smaller)
        # print(next_smaller)
        # the area for a particular height at i is area = heights[i] * (next_smaller[i] - pre_smaller + 1)

        max_area = 0
        for i in range(n):
            max_area = max(max_area,heights[i] * (next_smaller[i] - pre_smaller[i]+1))

        return max_area

        
