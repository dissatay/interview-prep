class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = a = lp = 0
        L = len(height)
        rp = L - 1

        while lp < rp:
            # get area
            h = min(height[lp], height[rp])
            w = rp - lp
            a = h * w
            # determine max
            maxArea = max(a, maxArea)
            # move one of the pointers
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1

        return maxArea