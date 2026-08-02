class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        while r > l:
            area = (r - l) * min(heights[r], heights[l])
            max_area = max(max_area, area)
            # print(r, l, "area: ", area, " max area: ", max_area)
            if heights[r] <= heights[l]:
                r -= 1
            else:
                l += 1
        return max_area
        